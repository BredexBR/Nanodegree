# **Árvore de Regressão (Regression Tree)**

A **Árvore de Regressão** é um algoritmo de aprendizado supervisionado usado especificamente para **tarefas de regressão** em Machine Learning. Ela é uma variante da árvore de decisão, onde a saída prevista é um valor contínuo, e não uma classe discreta.

---

## **Como funciona:**
1. **Construção da Árvore:**  
   - O algoritmo divide o conjunto de dados em subconjuntos menores com base em critérios que minimizam a variação dentro de cada subconjunto.
   - Geralmente, utiliza métricas como **Erro Quadrático Médio (MSE)** ou **Erro Absoluto Médio (MAE)** para encontrar os pontos ótimos de divisão.

2. **Predição:**  
   - Para prever o valor de uma nova entrada, o algoritmo percorre a árvore com base nos critérios de decisão de cada nó até chegar a um nó folha.
   - O valor retornado é a média ou mediana dos valores das amostras presentes nesse nó folha.

---

## **Exemplo Simples:**
Imagine que queremos prever o valor de uma casa com base em sua metragem e localização. A árvore pode ter a seguinte estrutura:

```
         Preço?
        /      \
   Área > 100m²   Área ≤ 100m²
   /      \       /       \
 Localização A  Média   Localização B

```

Neste exemplo, a decisão é baseada em critérios contínuos como área e localização, e os nós folha fornecem valores médios de preços.

---

## **Vantagens:**
- Simples de interpretar e visualizar.
- Requer pouca preparação dos dados (não exige normalização).
- Funciona bem com dados contínuos e não lineares.
- Boa flexibilidade para capturar relações complexas nos dados.

## **Desvantagens:**
- Propensa a **overfitting** se a árvore não for podada.
- Sensível a pequenas variações nos dados, podendo gerar árvores muito diferentes.
- Não ideal para dados muito grandes, devido ao aumento da complexidade.

---

## **Critérios de Divisão:**
Os principais critérios para divisão dos nós incluem:
- **Erro Quadrático Médio (MSE):** Minimiza a média dos quadrados dos erros.
- **Erro Absoluto Médio (MAE):** Minimiza a média dos valores absolutos dos erros.
- **Redução de Variância:** Escolhe a divisão que reduz a variância dos valores nos nós filhos.

---

## **Poda de Árvores:** 
Para evitar **overfitting**, técnicas de poda podem ser aplicadas, como:
- **Poda Pré-pruning:** Limita a profundidade da árvore durante a construção.
- **Poda Pós-pruning:** Remove divisões irrelevantes após a construção da árvore.