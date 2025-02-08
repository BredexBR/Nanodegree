import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

# ------------------------------ EXPLORAÇÃO DOS DADOS ----------------------------- #

plt.ion() # Ativa o modo interativo do Matplotlib para exibir gráficos dinamicamente

base = pd.read_csv("docs/modelagem_rh.csv")
exibirGraficos = 1
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
# base = pd.get_dummies(base, drop_first=True)

## Cria um DataFrame que mostra o valor máximo e mínimo de cada coluna da base de dados
# pd.DataFrame([base.max(), base.min()], index=["max", "min"]).T

# Extrai os valores numéricos da base para uma matriz de numpy
x = base.values

# Aplica a transformação Min-Max (escalonamento) aos dados
x_scaled = minmax.fit_transform(x)

# Cria um novo DataFrame com os dados escalonados, mantendo os nomes das colunas originais
base = pd.DataFrame(x_scaled, columns=base.columns)

# Cria um DataFrame que mostra o valor máximo e mínimo de cada coluna após o escalonamento
pd.DataFrame([base.max(), base.min()], index=["max", "min"]).T
