# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt

# Nome do arquivo CSV
# Corrija o caminho PATH para o seu diretorio
arquivo = "PATH/Caixeiro-viajante/data/coordsFront.csv"

# Coordenadas das cidades (armazenadas em uma lista de dicionários)
cidades = []
grafo = {}

# Leitura do arquivo CSV e armazenamento das coordenadas em 'cidades' e grafo de conexões
with open(arquivo, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        try:
            indice = int(row[0])
            latitude = float(row[1]) / 10
            longitude = float(row[2]) / 10
            vizinhos = [int(vizinho) for vizinho in row[3].split('.')]
            
            cidades.append({"latitude": latitude, "longitude": longitude})
            grafo[indice] = vizinhos
        except (ValueError, IndexError) as e:
            print(f"Erro ao processar linha: {row} - {e}")

# Função para plotar os pontos iniciais e suas conexões
def plotar_pontos_e_conexoes(cidades, grafo):
    plt.figure(figsize=(10, 6))
    
    # Plotar os pontos
    for idx, cidade in enumerate(cidades):
        plt.scatter(cidade["latitude"], cidade["longitude"], color='red', marker='o')
        plt.annotate(str(idx+1), (cidade["latitude"], cidade["longitude"]), textcoords="offset points", xytext=(0, 5), ha='center')
    
    # Plotar as conexões
    for cidade, vizinhos in grafo.items():
        if cidade >= len(cidades):
            continue
        lat1 = cidades[cidade]["latitude"]
        lon1 = cidades[cidade]["longitude"]
        for vizinho in vizinhos:
            if vizinho < len(cidades):
                lat2 = cidades[vizinho]["latitude"]
                lon2 = cidades[vizinho]["longitude"]
                plt.plot([lat1, lat2], [lon1, lon2], color='blue')
    
    plt.title("Pontos Iniciais das Cidades e suas Conexões")
    plt.grid(True)
    plt.show()

# Plotar os pontos e suas conexões
plotar_pontos_e_conexoes(cidades, grafo)
