import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import warnings

# Removerá *warnings* que aparecem no terminal
warnings.filterwarnings("ignore")

exibirGraficoScatter = 1

plt.ion() # Ativa o modo interativo do Matplotlib para exibir gráficos dinamicamente

base = pd.read_excel("docs/casas.xlsx")
del base["Unnamed: 0"]

if exibirGraficoScatter == 1:
    # Cria um gráfico de dispersão (scatter plot)
    # O eixo X representa os "metros quadrados" e o eixo Y representa o "preço"
    base.plot(kind="scatter", x="metros quadrados", y="preco")

if exibirGraficoScatter == 1:
    # Exibe o gráfico e mantém a janela aberta até ser fechada pelo usuário
    plt.show(block=True) 

x = base[["metros quadrados"]]
y = base[["preco"]]

# Criação de um modelo de regressão linear utilizando a classe 
# LinearRegression da biblioteca scikit-learn
regressao = LinearRegression()

regressao.fit(x, y)

regressao.predict([[1500]]) # São iguais

print("-----------------------------------------------------------------------------------------------------")
print("Valor regressão 1:")
print(regressao.coef_[0] * 1500 + regressao.intercept_[0]) # São iguais
print("-----------------------------------------------------------------------------------------------------")

# tanto o regressao.predict... quanto o regrassao.coef_... dariam o mesmo resultado

base2 = pd.read_excel("docs/casas_mult.xlsx")
del base2["Unnamed: 0"]

x2 = base2[["metros quadrados", "banheiros", "metros sem porao", "nota"]]
y2 = base2[["preco"]]

regressao2 = LinearRegression()

regressao2.fit(x2, y2)

print("-----------------------------------------------------------------------------------------------------")
print("Valor regressão 2:")
print(regressao2.predict([[1500, 1, 160, 7]]))
print("-----------------------------------------------------------------------------------------------------")