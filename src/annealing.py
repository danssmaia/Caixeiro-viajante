import haversine as hs
import csv
import random
import math

# Nome do arquivo CSV
arquivo = "C:/Users/cliente/Desktop/Cursos aleatorios/Caixeiro-viajante/data/coords.csv"

# Coordenadas das cidades (armazenadas em uma lista de dicionários)
cidades = []

# Leitura do arquivo CSV e armazenamento das coordenadas em 'cidades'
with open(arquivo, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        latitude = float(row[0])
        longitude = float(row[1])
        cidades.append({"latitude": latitude, "longitude": longitude})

# Função para calcular a distância total de um determinado percurso
def calcular_distancia_total(percurso, cidades):
    distancia_total = 0
    for i in range(len(percurso) - 1):
        ponto1 = (cidades[percurso[i]]["latitude"], cidades[percurso[i]]["longitude"])
        ponto2 = (cidades[percurso[i + 1]]["latitude"], cidades[percurso[i + 1]]["longitude"])
        distancia_total += hs.haversine(ponto1, ponto2)
    # Adicionar a distância de volta ao ponto inicial
    ponto_inicial = (cidades[percurso[0]]["latitude"], cidades[percurso[0]]["longitude"])
    ponto_final = (cidades[percurso[-1]]["latitude"], cidades[percurso[-1]]["longitude"])
    distancia_total += hs.haversine(ponto_final, ponto_inicial)
    return distancia_total

# Função para gerar uma solução inicial aleatória fixando a cidade de partida
def gerar_solucao_inicial(num_cidades, cidade_partida):
    solucao = list(range(num_cidades))
    solucao.remove(cidade_partida)
    random.shuffle(solucao)
    solucao.insert(0, cidade_partida)
    return solucao

# Função para realizar uma perturbação na solução (vizinho) mantendo a cidade de partida fixa
def gerar_vizinho(solucao):
    vizinho = solucao[1:]  # Exclui a cidade de partida
    i, j = random.sample(range(len(vizinho)), 2)
    vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
    vizinho.insert(0, solucao[0])  # Reinsere a cidade de partida
    return vizinho

# Função de probabilidade de aceitação
def probabilidade_aceitacao(delta, temperatura):
    if delta < 0:
        return 1.0
    else:
        return math.exp(-delta / temperatura)

# Algoritmo Simulated Annealing
def simulated_annealing(cidades, cidade_partida, temperatura_inicial, taxa_resfriamento, num_iteracoes):
    num_cidades = len(cidades)
    solucao_atual = gerar_solucao_inicial(num_cidades, cidade_partida)
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
    
    return melhor_solucao, menor_distancia

# Solicitar ao usuário que escolha a cidade de partida
print("Escolha uma cidade de partida pelo índice:")
for idx, cidade in enumerate(cidades):
    print(f"{idx}: ({cidade['latitude']}, {cidade['longitude']})")

cidade_partida = int(input("Digite o índice da cidade de partida: "))

# Parâmetros do Simulated Annealing
temperatura_inicial = 10000
taxa_resfriamento = 0.995
num_iteracoes = 10000

# Executar o Simulated Annealing
melhor_percurso, menor_distancia = simulated_annealing(cidades, cidade_partida, temperatura_inicial, taxa_resfriamento, num_iteracoes)

# Imprimir o melhor percurso e a menor distância
print("Melhor percurso:", melhor_percurso)
print("Menor distância:", menor_distancia, "km")
