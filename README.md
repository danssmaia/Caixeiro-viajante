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
│   ├── coordsFront.csv   # Arquivo CSV contendo os indices, coordenadas e indices que fazem fronteira
│   ├── custo.csv         # Arquivo CSV contendo o custo de deslocamento entre as regiões
├── src
│   ├── algoritmos        # Arquivo responsável por calcular a melhor rota para o TSP, utilizando o algortimo Simulated Annealing
│   ├── distancia.py      # Arquivo utilizado para gerar a matriz de custos
│   └── distanciaA.py     # Arquivo responsável por calcular a melhor rota entre 2 pontos, utilizando o algortimo A*
│   └── distanciaSA.py    # Arquivo responsável por calcular a melhor rota entre 2 pontos, utilizando o algortimo Simulated Annealing
│   └── grafo.py          # Arquivo responsável por plotar um grafo com os pontos e as suas fronteiras
│   └── pntosIniciais.py  # Arquivo responsável por plotar a posição dos pontos iniciais
├── README.md
```

## Tecnologias Utilizadas

- Python  3.8
- Bibliotecas:
  - csv
  - random
  - math
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

O Simulated Annealing é um algoritmo de otimização meta-heurística inspirado no processo de recozimento de materiais. 
Sua estrutura matemática é baseada na minimização de uma função de custo, 
geralmente representada pela função de energia E(x), onde x é o conjunto de variáveis de decisão.

A atualização da solução segue a seguinte equação:

ΔE = E(x') - E(x)

onde:
- ΔE é a variação de energia entre a nova solução (x') e a solução atual (x).
- E(x') é a energia da nova solução.
- E(x) é a energia da solução atual.

O Simulated Annealing aceita soluções piores com uma probabilidade P(ΔE, T), 
onde T é a temperatura atual do sistema, de acordo com a função de probabilidade de Boltzmann:

P(ΔE, T) = exp(-ΔE / T)

À medida que a temperatura diminui, a probabilidade de aceitar soluções piores também diminui, 
permitindo que o algoritmo explore o espaço de soluções de maneira mais intensiva.

Essa abordagem permite que o Simulated Annealing escape de mínimos locais e 
explore o espaço de busca de maneira mais ampla, eventualmente convergindo para a solução ótima ou próxima dela.


### A*

O algoritmo A* é um algoritmo de busca heurística que é amplamente utilizado em 
problemas de busca de caminho em grafos ou espaços de estados. Ele é eficiente e 
garante encontrar o caminho mais curto de um ponto de partida a um ponto de chegada, 
desde que determinadas condições sejam atendidas.

A* utiliza duas funções para encontrar o caminho ótimo:
- G(n): o custo do caminho do ponto inicial até o nó n.
- H(n): uma estimativa do custo do caminho mais curto do nó n até o destino.

Essas funções são combinadas em uma função de avaliação F(n) = G(n) + H(n), que é usada para decidir qual nó explorar em seguida.

O algoritmo A* mantém uma lista de nós a serem avaliados, ordenados pelo valor de F(n). 
Em cada iteração, o nó com o menor valor F(n) é retirado da lista e seus vizinhos são avaliados. 
Se um vizinho ainda não foi avaliado, ele é adicionado à lista; se já foi avaliado, o algoritmo atualiza suas informações se um caminho melhor for encontrado.

A* continua esse processo até que o destino seja alcançado ou até que todos os nós tenham sido explorados 
e nenhum caminho viável seja encontrado. Uma das principais vantagens do A* é sua capacidade de encontrar 
o caminho mais curto de forma eficiente, especialmente quando uma heurística admissível é utilizada, ou seja, 
quando a função H(n) nunca superestima o custo para alcançar o destino.

