import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


# Retorna o tamanho da tabela do arquivo excel
base = pd.read_excel("docs/funcionarios.xlsx")
print("Tamanho da tabela:")
print(base.shape)
print("-----------------------------------------------------------------------------------------------------")

# Deletara a coluna Unnamed: 0
del base["Unnamed: 0"]

print("Primeiras 5 ocorrências:")
# Imprime as 5 primeiras ocorrências do arquivo excel
print(base.head())
print("-----------------------------------------------------------------------------------------------------")

# Seleciona todas as colunas da base de dados, exceto a última.
# O iloc é usado para indexação baseada em posição:
# - ":" significa todas as linhas
# - ":-1" indica todas as colunas até a penúltima (a última coluna é excluída)
x = base.iloc[:, :-1]

# Seleciona apenas a última coluna da base de dados.
# O iloc é usado para indexação baseada em posição:
# - ":" significa todas as linhas
# - "-1" refere-se à última coluna
y = base.iloc[:, -1]

# Cria um objeto KNeighborsClassifier, que é um modelo de aprendizado supervisionado 
# baseado no algoritmo KNN.
# O parâmetro n_neighbors=3 define que o modelo usará os 3 vizinhos mais próximos para 
# determinar a classe de uma amostra.
knn = KNeighborsClassifier(n_neighbors=3)

#O método .fit() é usado para treinar o modelo KNN com os dados de treinamento.
knn.fit(x, y)

# O método .sample() seleciona uma amostra aleatória de uma linha ou mais da DataFrame 'base'.
# Neste caso, ele seleciona uma única linha de forma aleatória da base de dados carregada do 
# arquivo Excel.
amostra = base.sample()


# O método .predict() faz uma previsão usando o modelo KNN treinado. 
# O código seleciona todas as colunas de 'amostra' exceto a última (assumindo que a última é 
# a coluna de rótulos),
# e utiliza essas colunas para prever a classe correspondente.
print(knn.predict(amostra.iloc[:, :-1]))

# O método .predict() também pode ser utilizado passando uma lista de valores diretamente.
# Nesse caso, o modelo prevê a classe para os dados [2,1,0,0,1,0], que representam as 
# características de uma nova amostra.
print(knn.predict([2, 1, 0, 0, 1, 0]))
print("-----------------------------------------------------------------------------------------------------")