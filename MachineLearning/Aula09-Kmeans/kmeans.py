import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

plt.ion()
base = pd.read_csv("docs/compras_supermercado.csv", sep=",")

#print(base.shape)

# Cria uma instância do algoritmo K-means para agrupamento
# n_clusters=4: Define que o algoritmo deve formar 4 clusters (grupos) distintos
# max_iter=1000: Define o número máximo de iterações para o algoritmo ajustar os centróides dos clusters
kmeans = KMeans(n_clusters=4, max_iter=1000)

kmeans.fit(base)

## Exibe os rótulos dos clusters atribuídos pelo algoritmo K-means após o treinamento
## Cada número em kmeans.labels_ corresponde ao cluster ao qual o respectivo ponto de dados foi atribuído
#print(kmeans.labels_)

## Exibe as coordenadas dos centróides dos clusters gerados pelo K-means
## Cada linha de kmeans.cluster_centers_ representa a posição central de um cluster
#kmeans.cluster_centers_

## Exibe os centróides dos clusters em formato de DataFrame para melhor visualização
#print(pd.DataFrame(kmeans.cluster_centers_, columns=base.columns))

# Usa a função np.unique para encontrar os clusters únicos e a frequência de cada um
# return_counts=True: retorna a contagem de elementos em cada cluster
grupo, frequencia = np.unique(kmeans.labels_,
                              return_counts=True)

# Filtra os dados da base para incluir apenas os pontos de dados pertencentes ao cluster 0
# kmeans.labels_ == 0: seleciona os pontos que foram atribuídos ao cluster 0
# .hist(): cria o histograma das colunas numéricas desses dados
h = base[kmeans.labels_ == 0].hist()
plt.show(block=True)

