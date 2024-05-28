import haversine as hs
import csv

# Nome do arquivo CSV
arquivo = "C:/Users/cliente/Desktop/Cursos aleatorios/Caixeiro-viajante/data/coords.csv"

# Coordenadas dos pontos vermelhos (armazenadas em uma lista de dicionários)
pontos = []

# Leitura do arquivo CSV e armazenamento das coordenadas em 'pontos'
with open(arquivo, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        latitude = float(row[0])
        longitude = float(row[1])
        pontos.append({"latitude": latitude, "longitude": longitude})

# Matriz para armazenar as distâncias
num_pontos = len(pontos)
distancias = [[0 for _ in range(num_pontos)] for _ in range(num_pontos)]

# Cálculo das distâncias entre todos os pontos
for i in range(num_pontos):
    for j in range(num_pontos):
        if i == j:
            distancias[i][j] = 0  # Distância para si mesmo é zero
        else:
            ponto1 = (pontos[i]["latitude"], pontos[i]["longitude"])
            ponto2 = (pontos[j]["latitude"], pontos[j]["longitude"])
            distancia_km = hs.haversine(ponto1, ponto2)
            distancias[i][j] = distancia_km

# Imprimir a matriz de distâncias
for linha in distancias:
    print(linha)
