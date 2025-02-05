import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

base = pd.read_excel("../Aula03-KNN/docs/funcionarios.xlsx")
del base["Unnamed: 0"]

x = base.iloc[:, :-1]
y = base.iloc[:, -1]

tree = DecisionTreeClassifier()

tree.fit(x, y)

amostra = base.sample()

print("-----------------------------------------------------------------------------------------------------")
print(tree.predict(amostra.iloc[:, :-1]))
print("-----------------------------------------------------------------------------------------------------")
print(tree.predict([[2, 0, 0, 1, 1, 0]]))
print("-----------------------------------------------------------------------------------------------------")

arquivo = open("arvore.txt", "w")

# print(x.columns) # Vai mostrar as colunas presentes no arquivo

# print(base.linguagem.unique()) # Vai mostrar quais são os atributos sem se repetir 
# presentes na coluna linguagem

# Vai criar um arquivo chamado arvore.txt com o codigo referente a árvore de decisão
export_graphviz(tree, out_file= arquivo, 
                feature_names=x.columns,
                class_names=base.linguagem.unique())

# Caso não queira ficar gerando arquivos descomente a linha a seguir:
# arquivo.close() 

# Para melhor visualização copie o conteudo do arquivo txt e adicione ao campo no site:
# https://dreampuf.github.io/GraphvizOnline/?engine=dot#digraph%20G%20%7B%0A%0A%20%20subgraph%20cluster_0%20%7B%0A%20%20%20%20style%3Dfilled%3B%0A%20%20%20%20color%3Dlightgrey%3B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%2Ccolor%3Dwhite%5D%3B%0A%20%20%20%20a0%20-%3E%20a1%20-%3E%20a2%20-%3E%20a3%3B%0A%20%20%20%20label%20%3D%20%22process%20%231%22%3B%0A%20%20%7D%0A%0A%20%20subgraph%20cluster_1%20%7B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%5D%3B%0A%20%20%20%20b0%20-%3E%20b1%20-%3E%20b2%20-%3E%20b3%3B%0A%20%20%20%20label%20%3D%20%22process%20%232%22%3B%0A%20%20%20%20color%3Dblue%0A%20%20%7D%0A%20%20start%20-%3E%20a0%3B%0A%20%20start%20-%3E%20b0%3B%0A%20%20a1%20-%3E%20b3%3B%0A%20%20b2%20-%3E%20a3%3B%0A%20%20a3%20-%3E%20a0%3B%0A%20%20a3%20-%3E%20end%3B%0A%20%20b3%20-%3E%20end%3B%0A%0A%20%20start%20%5Bshape%3DMdiamond%5D%3B%0A%20%20end%20%5Bshape%3DMsquare%5D%3B%0A%7D
