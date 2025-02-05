# **Regressão Linear (Linear Regression)**

A **Regressão Linear** é um algoritmo de aprendizado supervisionado utilizado para **previsão** e **modelagem** de dados em Machine Learning, sendo amplamente utilizado em problemas de regressão. O objetivo principal da regressão linear é modelar a relação entre uma variável dependente (também chamada de variável alvo) e uma ou mais variáveis independentes (também chamadas de preditores ou características).

---

## **Como funciona:**
1. **Modelo de Relação Linear:**
   - O modelo assume que existe uma relação linear entre a variável dependente e as variáveis independentes. Ou seja, o valor da variável dependente é uma combinação linear dos preditores.
   - A fórmula do modelo é:  
     \[
     y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n + \epsilon
     \]
     Onde:
     - \( y \) é a variável dependente (o que queremos prever).
     - \( x_1, x_2, \dots, x_n \) são as variáveis independentes (as características ou preditores).
     - \( \beta_0 \) é o intercepto (onde a linha cruza o eixo Y).
     - \( \beta_1, \dots, \beta_n \) são os coeficientes, que representam o impacto de cada variável independente.
     - \( \epsilon \) é o erro (resíduo).

2. **Ajuste do Modelo:**
   - O algoritmo encontra os valores dos coeficientes \( \beta_0, \beta_1, \dots, \beta_n \) que minimizam a diferença entre os valores preditos e os reais. Isso é feito através da minimização da soma dos quadrados dos resíduos (erro quadrático médio).

3. **Predição:**
   - Após o ajuste, o modelo pode ser usado para prever novos valores da variável dependente \( y \) com base em valores conhecidos das variáveis independentes.

---

## **Exemplo Simples:**
Suponha que queremos prever o preço de uma casa com base em sua metragem quadrada. O modelo de regressão linear pode ser representado por:

\[
\text{Preço} = \beta_0 + \beta_1 \times \text{Metragem}
\]

Onde \( \beta_0 \) é o valor base do preço e \( \beta_1 \) é a variação do preço para cada metro quadrado adicional.

---

## **Vantagens:**
- Simples de entender e implementar.
- Requer pouca computação, sendo eficiente para problemas simples.
- Produz resultados interpretáveis, pois os coeficientes mostram a contribuição de cada variável independente.

## **Desvantagens:**
- Sensível a outliers, que podem distorcer o modelo.
- Só é aplicável quando a relação entre as variáveis é realmente linear (caso contrário, o modelo pode ser ineficaz).
- Não funciona bem com dados que têm alta multicolinearidade (quando as variáveis independentes estão altamente correlacionadas entre si).

---

## **Usos Comuns:**
- Previsão de vendas com base em variáveis como publicidade e preço.
- Previsão de valores de mercado financeiro, como o preço de ações.
- Previsão de desempenho acadêmico com base em variáveis como horas de estudo e frequência em aulas.

---