import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_graphviz

base = pd.read_excel("docs/jogadores.xlsx")
del base["Unnamed: 0"]

print(base.head())

x = base.iloc[:, :-1]
y = base.iloc[:, -1]

# Cria um modelo de árvore de regressão
# min_samples_leaf=2: Define que cada nó folha deve ter pelo menos 2 amostras
# Isso ajuda a evitar overfitting ao impedir nós com poucos dados
tree = DecisionTreeRegressor(min_samples_leaf=2)

tree.fit(x, y)

amostra = base.sample()

print(tree.predict(amostra.iloc[:, :-1]))

print(tree.predict([[1, 0, 1, 0, 1, 1]]))

arquivo = open("arvoreRegressao.txt", "w")

export_graphviz(tree, out_file= arquivo, 
                feature_names=x.columns)

# Caso não queira ficar gerando arquivos descomente a linha a seguir:
# arquivo.close() 

# Para melhor visualização copie o conteudo do arquivo txt e adicione ao campo no site:
# https://dreampuf.github.io/GraphvizOnline/?engine=dot#digraph%20G%20%7B%0A%0A%20%20subgraph%20cluster_0%20%7B%0A%20%20%20%20style%3Dfilled%3B%0A%20%20%20%20color%3Dlightgrey%3B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%2Ccolor%3Dwhite%5D%3B%0A%20%20%20%20a0%20-%3E%20a1%20-%3E%20a2%20-%3E%20a3%3B%0A%20%20%20%20label%20%3D%20%22process%20%231%22%3B%0A%20%20%7D%0A%0A%20%20subgraph%20cluster_1%20%7B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%5D%3B%0A%20%20%20%20b0%20-%3E%20b1%20-%3E%20b2%20-%3E%20b3%3B%0A%20%20%20%20label%20%3D%20%22process%20%232%22%3B%0A%20%20%20%20color%3Dblue%0A%20%20%7D%0A%20%20start%20-%3E%20a0%3B%0A%20%20start%20-%3E%20b0%3B%0A%20%20a1%20-%3E%20b3%3B%0A%20%20b2%20-%3E%20a3%3B%0A%20%20a3%20-%3E%20a0%3B%0A%20%20a3%20-%3E%20end%3B%0A%20%20b3%20-%3E%20end%3B%0A%0A%20%20start%20%5Bshape%3DMdiamond%5D%3B%0A%20%20end%20%5Bshape%3DMsquare%5D%3B%0A%7D
