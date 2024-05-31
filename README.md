# Projeto Caixeiro Viajante 

## Descrição

Este projeto tem como objetivo resolver o problema do Caixeiro Viajante (Travelling Salesman Problem - TSP) especificamente para o estado da Bahia, Brasil. O TSP é um dos problemas mais clássicos e estudados em otimização combinatória, onde o desafio é encontrar o menor caminho que passa por todas as cidades exatamente uma vez e retorna à cidade de origem.

A ideia é utilizar o mapa das regiões da bahia como referência.
![Mapa das Regiões da Bahia](mapa.PNG)

URL: http://www.cultura.ba.gov.br/modules/conteudo/conteudo.php?conteudo=314
## Estrutura do Projeto

```
.
├── data
│   ├── coords.csv        # Arquivo CSV contendo as coordenadas das regiões da Bahia
│   ├── custo.csv         # Arquivo CSV contendo o custo de deslocamento entre as regiões
├── src
│   ├── algoritmos        # Arquivo responsável por calcular a melhor rota para o TSP, utilizando o algortimo Simulated Annealing
│   ├── distancia.py      # Arquivo utilizado para gerar a matriz de custos
│   └── distanciaSA.py    # Arquivo responsável por calcular a melhor rota entre 2 pontos, utilizando o algortimo Simulated Annealing
├── README.md
```

## Tecnologias Utilizadas

- Python 
- Bibliotecas:
  - pandas
  - numpy
  - matplotlib
  - haversine

## Como Usar

1. Clone o repositório:

   ```sh
   git clone https://github.com/seu_usuario/caixeiro-viajante-bahia.git
   cd caixeiro-viajante-bahia
   ```

## Organização dos Dados

Os dados das regiões da Bahia estão armazenados nos arquivos do folder `data`.

## Algoritmos Implementados

### Simulated Annealing

É uma técnica probabilística usada para encontrar uma aproximação da solução 
ótima ou aproximadamente ótima para um problema de otimizaçã. Ele é particularmente útil em problemas onde 
a função de custo é complicada, multimodal, ou possui muitos mínimos locais.

Como parte de sua natureza probabilística, cada vez que você executa o algoritmo 
Simulated Annealing, ele pode convergir para uma solução diferente. 
Isso ocorre porque as escolhas feitas durante a execução, como a seleção de vizinhos 
e a aceitação de soluções piores, são influenciadas por fatores aleatórios, 
como a temperatura e números aleatórios gerados.

### A*
Em andamento .....