# **KNN (K-Nearest Neighbors)**

O **KNN (K-Nearest Neighbors)** é um algoritmo de aprendizado supervisionado usado tanto para classificação quanto para regressão em Machine Learning. Ele é baseado na ideia de que objetos semelhantes tendem a estar próximos uns dos outros.

---

## **Como funciona:**
1. **Treinamento:**  
   O KNN não realiza nenhum aprendizado explícito durante essa etapa. Ele apenas armazena os dados de treinamento.

2. **Classificação ou Regressão:**  
   Quando uma nova amostra é apresentada:
   - O algoritmo calcula a **distância** entre a nova amostra e todas as amostras no conjunto de dados (geralmente usando a distância Euclidiana).
   - Seleciona os **K vizinhos mais próximos** (onde K é um número inteiro definido pelo usuário).
   - **Classificação:** A classe mais frequente entre os vizinhos é atribuída à nova amostra.  
   **Regressão:** A média dos valores dos K vizinhos é usada como a previsão.

---

## **Exemplo Simples:**  
Imagine um conjunto de dados com informações sobre frutas, onde as características são peso e cor. O KNN pode classificar uma nova fruta com base nas frutas mais próximas em termos dessas características.

---

## **Vantagens:**
- Simples de entender e implementar.
- Bom desempenho com dados bem distribuídos.
- Não requer treinamento explícito.

## **Desvantagens:**
- Lento para grandes conjuntos de dados, pois precisa calcular distâncias para todos os pontos.
- Sensível a ruídos e ao valor de K escolhido.
- Pode ser influenciado pela escala das variáveis (normalização é recomendada).

---

## **Escolha do K:**  
Um valor pequeno de K pode levar a um modelo com alta variância (overfitting), enquanto um valor grande pode levar a alta tendência (underfitting). Valores ímpares geralmente são preferidos para evitar empates.

---
