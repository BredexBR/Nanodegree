# **Apriori**

O **Apriori** é um algoritmo clássico de aprendizado de máquina utilizado para **mineração de regras de associação**. Ele é amplamente empregado em análise de padrões de compra, recomendação de produtos e descoberta de relações entre itens em grandes bases de dados transacionais.

---

## **Como funciona:**
1. **Cálculo do suporte para os itens individuais:**  
   - O suporte de um item é a frequência com que ele aparece nas transações.
   
2. **Geração de conjuntos de itens frequentes:**  
   - Combina os itens que possuem suporte acima de um determinado limiar.
   
3. **Construção das regras de associação:**  
   - Para cada conjunto de itens frequentes, são geradas regras do tipo `A → B`, onde **A implica B**.

4. **Cálculo da confiança e validação das regras:**  
   - A confiança mede a probabilidade de B estar presente, dado que A já está presente.
   - Apenas as regras que atingem um valor mínimo de confiança são mantidas.

---

## **Exemplo Simples:**
Imagine um supermercado analisando compras de clientes. O Apriori pode identificar padrões como:

- Se um cliente compra pão e manteiga, ele tem alta probabilidade de comprar leite.

Essas regras podem ser usadas para **ofertas personalizadas** e **recomendações de produtos**.

---

## **Métricas Utilizadas:**
- **Suporte:** Frequência de ocorrência do conjunto de itens.
- **Confiança:** Probabilidade condicional de um item estar presente, dado outro item.
- **Lift:** Mede a relação entre a ocorrência conjunta e a ocorrência esperada, ajudando a identificar relações realmente significativas.

---

## **Vantagens:**
- Fácil interpretação e implementação.
- Eficiente para análise de grandes bases transacionais.
- Gera regras úteis para estratégias de recomendação e marketing.

## **Desvantagens:**
- Pode ser computacionalmente custoso para grandes bases de dados.
- Gera muitas regras, exigindo filtragem para selecionar as mais relevantes.
- Sensível ao ajuste dos parâmetros de suporte e confiança.

---

## **Otimização do Apriori:**
Para melhorar a eficiência, algumas otimizações podem ser aplicadas:
- **Redução da dimensionalidade:** Remover itens irrelevantes antes do processamento.
- **Aproveitamento de padrões fechados e máximos:** Para evitar redundâncias.
- **Uso de implementações otimizadas:** Como o **FP-Growth**, que elimina a necessidade de geração de candidatos.


