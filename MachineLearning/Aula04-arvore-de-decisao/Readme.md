# **Árvore de Decisão (Decision Tree)**

A **Árvore de Decisão** é um algoritmo de aprendizado supervisionado usado tanto para **classificação** quanto para **regressão** em Machine Learning. Ele é baseado na estrutura de uma árvore, onde cada nó representa uma decisão baseada em um atributo dos dados.

---

## **Como funciona:**
1. **Construção da Árvore:**  
   - O algoritmo divide o conjunto de dados em subconjuntos menores com base nos atributos que maximizam a separação dos dados (geralmente usando métricas como **Gini** ou **Entropia** para classificação e **Erro Quadrático Médio** para regressão).
   - Cada divisão cria novos nós e ramos, formando uma estrutura hierárquica.

2. **Classificação ou Regressão:**  
   - Para prever um novo dado, ele percorre a árvore seguindo os critérios de decisão de cada nó até chegar a um nó folha, onde a resposta final é determinada.

---

## **Exemplo Simples:**
Imagine que queremos prever se um cliente comprará um produto baseado em sua renda e idade. A árvore pode ter a seguinte estrutura:

```
         Compra?
        /      \
      Sim       Não
     /   \      /   \
 Renda Alta  Idade < 25
```

Neste caso, a decisão de compra será feita com base nesses critérios de divisão.

---

## **Vantagens:**
- Fácil de interpretar e visualizar.
- Requer pouca preparação dos dados (não exige normalização).
- Funciona bem com dados categóricos e numéricos.

## **Desvantagens:**
- Pode sofrer de **overfitting**, criando árvores muito complexas.
- Sensível a pequenas variações nos dados, o que pode gerar árvores muito diferentes (solução: **poda** ou uso de **Random Forest**).
- Não é ideal para dados muito grandes devido à complexidade da árvore.

---

## **Critérios de Divisão:**
Os principais critérios para divisão dos nós incluem:
- **Gini:** Mede a impureza dos nós (usado no algoritmo CART).
- **Entropia:** Mede a incerteza dos dados (usado no ID3 e C4.5).
- **Redução do Erro Quadrático Médio:** Usado para problemas de regressão.

---
