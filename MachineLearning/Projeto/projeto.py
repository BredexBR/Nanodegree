import pandas as pd

import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import confusion_matrix, accuracy_score
import pickle

# ------------------------------ EXPLORAÇÃO DOS DADOS ----------------------------- #

plt.ion() # Ativa o modo interativo do Matplotlib para exibir gráficos dinamicamente

base = pd.read_csv("docs/modelagem_rh.csv")
exibirGraficos = 0
# print(base.shape)
# print(base.head())

## Exibe a proporção percentual de valores distintos na coluna 'saiu'
## base.saiu.value_counts(): conta a frequência de cada valor na coluna 'saiu'
## len(base): obtém o total de registros no DataFrame
## Multiplica por 100 para exibir como porcentagem
# print(base.saiu.value_counts()/len(base)*100)

# Cria um gráfico de barras com a contagem dos valores na coluna 'saiu'
base.saiu.value_counts().plot(kind="bar")

# Define os rótulos personalizados para o eixo X
# (0, 1) são os índices das barras correspondentes às classes
# ["Não saiu", "Saiu"] são os rótulos a serem exibidos
plt.xticks((0,1), ["Não saiu", "Saiu"])

if exibirGraficos == 1:    
    plt.show(block=True)

## Cria uma tabela cruzada (contingência), que mostra a contagem de registros para 
## cada combinação de valores entre as colunas departamento e saiu.
# print(pd.crosstab(base.departamento, base.saiu))
valores = pd.crosstab(base.departamento, base.saiu)

# Calcula a soma dos valores ao longo do eixo 1 (linhas) e armazena em 'soma'
soma = valores.sum(axis=1)

# print(soma)

# print(valores.divide(soma, axis=0)*100)

valores_salario = pd.crosstab(base.salario, base.saiu)
soma_salario = valores_salario.sum(axis=1)

porc_salario =  valores_salario.divide(soma_salario, axis=0)*100

# stacked=True: Empilha as barras, mostrando os dados acumulados em cada 
# categoria ao longo de uma barra única. Isso facilita a visualização de proporções.
porc_salario.plot(kind="bar", stacked=True)

if exibirGraficos == 1:    
    plt.show(block=True)

#------------------------ TRATANDO VALORES NULOS ------------------------- #

## Exibe informações sobre o DataFrame 'base', incluindo tipo de dados e valores não nulos
# print(base.info())

## Retorna a soma de valores nulos (NaN) por coluna no DataFrame 'base'
# print(base.isnull().sum())

# Preenche os valores ausentes (NaN) na coluna 'nivel_satisfacao' com a média dessa coluna
base.loc[base.nivel_satisfacao.isnull(),'nivel_satisfacao'] = base.nivel_satisfacao.mean()

# print(base.isnull().sum()) # Agora não é apresentado mais dados nulos

# ------------------------ PREPARAÇÃO DOS DADOS VARIÁVEIS CATEGÓRICAS E NORMALIZAÇÃO ------------------------ # 

# Cria variáveis dummy para as colunas categóricas em 'base', excluindo a primeira coluna de cada 
## variável (drop_first=True)
base = pd.get_dummies(base, drop_first=True)

## Cria um DataFrame que mostra o valor máximo e mínimo de cada coluna da base de dados
pd.DataFrame([base.max(), base.min()], index=["max", "min"]).T

# Extrai os valores numéricos da base para uma matriz de numpy
x = base.values

minmax = preprocessing.MinMaxScaler()

# Aplica a transformação Min-Max (escalonamento) aos dados
x_scaled = minmax.fit_transform(x)

# Cria um novo DataFrame com os dados escalonados, mantendo os nomes das colunas originais
base = pd.DataFrame(x_scaled, columns=base.columns)

# Cria um DataFrame que mostra o valor máximo e mínimo de cada coluna após o escalonamento
pd.DataFrame([base.max(), base.min()], index=["max", "min"]).T

# ------------------------ MODELAGEM ------------------------  #

cols = list(base.columns)
cols.remove("saiu")

x = base[cols]
y = base["saiu"]

knn = KNeighborsClassifier(n_neighbors=3)

tree = DecisionTreeClassifier()

# Divide os dados em conjuntos de treinamento (X_train, y_train) e 
# teste (X_test, y_test) com 80% para treino e 20% para teste
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

knn.fit(X_train, y_train)

# predicted = knn.predict(X_test)

## Calcula a acurácia do modelo comparando as previsões com os valores reais (y_test)
# print(accuracy_score(predicted, y_test))

## Calcula a matriz de confusão comparando as previsões (predicted) com os valores reais (y_test)
# print(confusion_matrix(predicted, y_test))

tree.fit(X_train, y_train)

## Calcula a acurácia do modelo comparando as previsões com os valores reais (y_test)
# print(accuracy_score(tree.predict(X_test), y_test))

## Calcula a matriz de confusão comparando as previsões (predicted) com os valores reais (y_test)
# print(confusion_matrix(tree.predict(X_test), y_test))

# Realiza a validação cruzada para avaliar o modelo 'knn' usando 5 divisões e a métrica de acurácia
scores = cross_val_score(knn, x, y, cv=5, scoring='accuracy')

## Exibe a média das acurácias obtidas nas 5 divisões (folds) da validação cruzada
# print(scores.mean())

## Exibe o desvio padrão das acurácias obtidas nas 5 divisões (folds) da validação cruzada
# print(scores.std())

scores_tree = cross_val_score(tree, x, y, cv=5, scoring='accuracy')

## Exibe a média das acurácias obtidas nas 5 divisões (folds) da validação cruzada
# print(scores_tree.mean())

## Exibe o desvio padrão das acurácias obtidas nas 5 divisões (folds) da validação cruzada
# print(scores_tree.std())


# ------------------- DEPLOY -------------------  #
# Cria um DataFrame para visualizar a importância das features
# 'tree.feature_importances_' contém a importância de cada variável no modelo de árvore de decisão
# 'x.columns' contém os nomes das variáveis que foram usadas no modelo

# Cria um DataFrame onde as linhas são as features e as colunas contêm suas importâncias
# A indexação [:5] seleciona as primeiras 5 features com maior importância
# Isso ajuda a entender quais variáveis têm maior influência no modelo
pd.DataFrame(tree.feature_importances_, index=x.columns)[:5].plot(kind="bar")

if exibirGraficos == 1:    
    plt.show(block=True)

tree.fit(x, y)

# Salva o modelo treinado 'tree' no arquivo 'modeloRH.pickle'
# 'wb' indica que o arquivo será aberto em modo de escrita binária (write binary)
pickle.dump(tree, open("docs/modeloRH.pickle", "wb"))

# Carrega o modelo de árvore de decisão treinado a partir do arquivo 'modeloRH.pickle'
# 'rb' indica que o arquivo será aberto em modo de leitura binária (read binary)
treeSalva = pickle.load(open("docs/modeloRH.pickle", "rb"))

treeSalva.predict(X_test) # Nesse caso X_test poderia ser outros conjuntos de treinamento.