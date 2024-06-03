# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt

# Nome do arquivo CSV
arquivo = "C:/Users/cliente/Desktop/Cursos aleatorios/Caixeiro-viajante/data/coords.csv"

# Coordenadas das cidades (armazenadas em uma lista de dicionários)
cidades = []

# Leitura do arquivo CSV e armazenamento das coordenadas em 'cidades'
with open(arquivo, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        latitude = float(row[0]) / 10
        longitude = float(row[1]) / 10
        cidades.append({"latitude": latitude, "longitude": longitude})

def plotar_pontos_iniciais(cidades):
    latitudes = [cidade["latitude"] for cidade in cidades]
    longitudes = [cidade["longitude"] for cidade in cidades]
    
    plt.figure(figsize=(10, 6))
    plt.scatter( latitudes, longitudes, color='red', marker='o')
    plt.title("Pontos Iniciais das Cidades")
    
    # Índices das cidades
    for idx, (lon, lat) in enumerate(zip(latitudes, longitudes)):
        plt.annotate(str(idx), (lon, lat), textcoords="offset points", xytext=(0, 5), ha='center')
    
    # Inverter o eixo Y para que o ponto (0,0) esteja no canto superior esquerdo
    
    plt.grid(True)
    plt.show()

plotar_pontos_iniciais(cidades)
