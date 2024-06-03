import haversine as hs
import csv
import random
import math
import matplotlib.pyplot as plt

# Nome do arquivo CSV
arquivo = "C:/Users/cliente/Desktop/Cursos aleatorios/Caixeiro-viajante/data/coords.csv"

# Coordenadas das cidades (armazenadas em uma lista de dicionários)
cidades = []

# Leitura do arquivo CSV e armazenamento das coordenadas em 'cidades'
with open(arquivo, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        latitude = float(row[0])/10
        longitude = float(row[1])/10
        cidades.append({"latitude": latitude, "longitude": longitude})

# Função para calcular a distância entre duas cidades
def calcular_distancia(cidade1, cidade2):
    ponto1 = (cidade1["latitude"], cidade1["longitude"])
    ponto2 = (cidade2["latitude"], cidade2["longitude"])
    return hs.haversine(ponto1, ponto2)

# Função para calcular a distância total de um determinado percurso
def calcular_distancia_total(percurso, cidades):
    distancia_total = 0
    for i in range(len(percurso) - 1):
        distancia_total += calcular_distancia(cidades[percurso[i]], cidades[percurso[i + 1]])
    return distancia_total

# Função para gerar uma solução inicial aleatória
def gerar_solucao_inicial(num_cidades):
    solucao = list(range(num_cidades))
    random.shuffle(solucao)
    return solucao

# Função para realizar uma perturbação na solução (vizinho)
def gerar_vizinho(solucao):
    vizinho = solucao[:]
    i, j = random.sample(range(len(vizinho)), 2)
    vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
    return vizinho

# Função de probabilidade de aceitação
def probabilidade_aceitacao(delta, temperatura):
    if delta < 0:
        return 1.0
    else:
        return math.exp(-delta / temperatura)

# Algoritmo Simulated Annealing
def simulated_annealing(cidades, cidade_origem, cidade_destino, temperatura_inicial, taxa_resfriamento, num_iteracoes):
    num_cidades = len(cidades)
    solucao_atual = gerar_solucao_inicial(num_cidades)
    distancia_atual = calcular_distancia_total(solucao_atual, cidades)
    
    melhor_solucao = solucao_atual
    menor_distancia = distancia_atual
    
    temperatura = temperatura_inicial
    
    for _ in range(num_iteracoes):
        vizinho = gerar_vizinho(solucao_atual)
        distancia_vizinho = calcular_distancia_total(vizinho, cidades)
        
        delta = distancia_vizinho - distancia_atual
        
        if probabilidade_aceitacao(delta, temperatura) > random.random():
            solucao_atual = vizinho
            distancia_atual = distancia_vizinho
            
            if distancia_atual < menor_distancia:
                melhor_solucao = solucao_atual
                menor_distancia = distancia_atual
        
        temperatura *= taxa_resfriamento
    
    # Verificar se a solução encontrada inclui as duas cidades específicas
    if cidade_origem in melhor_solucao and cidade_destino in melhor_solucao:
        idx_origem = melhor_solucao.index(cidade_origem)
        idx_destino = melhor_solucao.index(cidade_destino)
        if idx_origem < idx_destino:
            melhor_rota = melhor_solucao[idx_origem:idx_destino+1]
        else:
            melhor_rota = melhor_solucao[idx_destino:idx_origem+1][::-1] 
        menor_distancia = calcular_distancia_total(melhor_rota, cidades)
        return melhor_rota, menor_distancia
    else:
        return [], float('inf')

# Solicitar ao usuário que escolha as cidades de origem e destino
print("Escolha as cidades de origem e destino pelo índice:")
for idx, cidade in enumerate(cidades):
    print(f"{idx}: ({cidade['latitude']}, {cidade['longitude']})")

cidade_origem = int(input("Digite o índice da cidade de origem: "))
cidade_destino = int(input("Digite o índice da cidade de destino: "))

# Parâmetros do Simulated Annealing
temperatura_inicial = 10000
taxa_resfriamento = 0.995
num_iteracoes = 10000

# Executar o Simulated Annealing para encontrar a melhor rota entre as cidades escolhidas
melhor_rota, menor_distancia = simulated_annealing(cidades, cidade_origem, cidade_destino, temperatura_inicial, taxa_resfriamento, num_iteracoes)

# Imprimir a melhor rota e a menor distância
if melhor_rota:
    print("Melhor rota:", melhor_rota)
    print("Menor distância:", menor_distancia, "km")
else:
    print("Não foi possível encontrar uma rota que conecte as duas cidades especificadas.")


# Função para plotar o melhor percurso
def plotar_percurso(cidades, percurso):
    latitudes = [cidades[i]["latitude"] for i in percurso] + [cidades[percurso[0]]["latitude"]]
    longitudes = [cidades[i]["longitude"] for i in percurso] + [cidades[percurso[0]]["longitude"]]
    
    plt.figure(figsize=(10, 6))
    plt.plot(longitudes, latitudes, 'o-', markersize=5, color='blue')
    plt.title("Melhor Percurso do Caixeiro Viajante")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    
    # Adicionar anotações com os índices das cidades
    for i, (lat, lon) in enumerate(zip(latitudes, longitudes)):
        plt.annotate(str(percurso[i % len(percurso)]), (lon, lat))
    
    plt.grid(True)
    plt.show()

# Plotar o melhor percurso
plotar_percurso(cidades, melhor_rota)

# -*- coding: utf-8 -*-

