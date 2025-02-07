# **K-Means**

O **K-Means** é um algoritmo de aprendizado não supervisionado utilizado para **agrupamento de dados** (clustering). Ele particiona um conjunto de dados em **K clusters** com base na similaridade entre os pontos, sendo amplamente utilizado em tarefas como segmentação de clientes, compressão de imagens e análise de padrões.

---

## **Como funciona:**
1. **Escolha do número de clusters (K):**  
   - Define-se o número de clusters desejados (K).

2. **Inicialização dos centróides:**  
   - Seleciona-se aleatoriamente **K pontos** como centróides iniciais.

3. **Atribuição dos pontos aos clusters:**  
   - Cada ponto de dado é atribuído ao cluster cujo centróide estiver mais próximo (usando a distância Euclidiana).

4. **Atualização dos centróides:**  
   - Para cada cluster, calcula-se a **média dos pontos atribuídos a ele**, e o centróide é atualizado para essa média.

5. **Repetição do processo:**  
   - Os passos 3 e 4 são repetidos até que os centróides não mudem significativamente ou um critério de parada seja atingido.

---

## **Exemplo Simples:**
Imagine um conjunto de dados representando a altura e o peso de pessoas. O K-Means pode agrupá-los em **três clusters** representando diferentes categorias de constituição física:

```
  Cluster 1: Pessoas mais baixas e leves
  Cluster 2: Pessoas de altura e peso médios
  Cluster 3: Pessoas mais altas e pesadas
```

Após várias iterações, cada pessoa será atribuída ao grupo ao qual mais se assemelha.

---

## **Vantagens:**
- Simples e eficiente para grandes volumes de dados.
- Rápido na convergência, principalmente com otimizações como **K-Means++**.
- Funciona bem quando os clusters possuem formas circulares ou esféricas.

## **Desvantagens:**
- O número de clusters (**K**) deve ser definido manualmente.
- Sensível a valores extremos e à inicialização dos centróides.
- Pode ter dificuldades em identificar clusters de formatos não esféricos.

---

## **Critérios de Avaliação:**
Após a execução do K-Means, algumas métricas podem ser usadas para avaliar a qualidade dos clusters:
- **Inércia (Soma dos Erros Quadráticos - SSE):** Mede a coesão dentro dos clusters.
- **Índice de Silhueta:** Mede a separação entre os clusters.
- **Método do Cotovelo:** Ajuda a escolher um bom valor de **K** observando a variação da inércia.

---

## **Otimização do K-Means:**
Algumas variações do K-Means melhoram sua eficiência:
- **K-Means++:** Inicializa os centróides de forma mais inteligente para evitar más escolhas iniciais.
- **Mini-Batch K-Means:** Usa amostras menores dos dados para acelerar a convergência em grandes datasets.
- **K-Medoids:** Utiliza objetos reais como centróides, tornando-o mais robusto contra outliers.
