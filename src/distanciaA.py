# -*- coding: utf-8 -*-

import csv
import heapq
import math
import matplotlib.pyplot as plt

# Nome do arquivo CSV
# Corrija o caminho PATH para o seu diretorio
arquivo = "PATH/Caixeiro-viajante/data/coordsFront.csv"

cidades = []
grafo = {}

# Leitura do arquivo CSV e armazenamento das coordenadas em 'cidades' e grafo de conexões
with open(arquivo, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        indice = int(row[0])
        latitude = float(row[1]) / 10
        longitude = float(row[2]) / 10
        vizinhos = [int(vizinho) for vizinho in row[3].split('.')]
        
        cidades.append({"latitude": latitude, "longitude": longitude})
        grafo[indice] = vizinhos

# Função de distância de Haversine
def distancia_haversine(ponto1, ponto2):
    R = 6371  # Raio da Terra em km
    lat1, lon1 = math.radians(ponto1["latitude"]), math.radians(ponto1["longitude"])
    lat2, lon2 = math.radians(ponto2["latitude"]), math.radians(ponto2["longitude"])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c

# Função A*
def a_star(cidades, grafo, inicio, objetivo):
    def heuristica(cidade_atual, cidade_objetivo):
        return distancia_haversine(cidades[cidade_atual], cidades[cidade_objetivo])
    
    open_set = []
    heapq.heappush(open_set, (0, inicio))
    
    g_score = {i: float('inf') for i in range(len(cidades))}
    g_score[inicio] = 0
    
    f_score = {i: float('inf') for i in range(len(cidades))}
    f_score[inicio] = heuristica(inicio, objetivo)
    
    came_from = {}
    
    while open_set:
        _, atual = heapq.heappop(open_set)
        
        if atual == objetivo:
            path = []
            while atual in came_from:
                path.append(atual)
                atual = came_from[atual]
            path.append(inicio)
            path.reverse()
            return path
        
        for vizinho in grafo[atual]:
            distancia = distancia_haversine(cidades[atual], cidades[vizinho])
            tentative_g_score = g_score[atual] + distancia
            
            if tentative_g_score < g_score[vizinho]:
                came_from[vizinho] = atual
                g_score[vizinho] = tentative_g_score
                f_score[vizinho] = g_score[vizinho] + heuristica(vizinho, objetivo)
                if not any(item[1] == vizinho for item in open_set):
                    heapq.heappush(open_set, (f_score[vizinho], vizinho))
    
    return []

def plotar_rota(cidades, rota):
    latitudes = [cidades[i]["latitude"] for i in rota]
    longitudes = [cidades[i]["longitude"] for i in rota]
    
    plt.figure(figsize=(10, 6))
    plt.plot(latitudes, longitudes, marker='o', color='red')
    plt.title("Rota entre as Cidades")
    
    for idx, (lat, lon) in enumerate(zip(latitudes, longitudes)):
        plt.annotate(str(rota[idx]+1), (lat, lon), textcoords="offset points", xytext=(0, 5), ha='center')
    
    plt.grid(True)
    plt.show()

# Solicitar ao usuário que escolha as cidades de origem e destino
print("Escolha as cidades de origem e destino pelo índice:")
for idx, cidade in enumerate(cidades):
    print(f"{idx+1}: ({cidade['latitude']}, {cidade['longitude']})")

inicio = int(input("Digite o índice da cidade de origem: "))
objetivo = int(input("Digite o índice da cidade de destino: "))

rota = a_star(cidades, grafo, inicio-1, objetivo-1)
plotar_rota(cidades, rota)
