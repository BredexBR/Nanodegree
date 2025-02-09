# 📌 Projeto Machine Learning - Predição de Demissões

## 📌 Objetivo

Este projeto tem como objetivo auxiliar a equipe de Recursos Humanos (RH) a prever quais funcionários têm maior probabilidade de pedir demissão. Dessa forma, a empresa pode agir de forma preventiva, oferecendo incentivos para a retenção de talentos.

## 📌 Tecnologias e Bibliotecas Utilizadas

- **Pandas**: Leitura e manipulação de dados.
- **Scikit-Learn**: Implementação dos algoritmos de Machine Learning.
- **Matplotlib**: Visualização gráfica dos dados.
- **Pickle**: Serialização do modelo treinado.

## 📌 Descrição do Problema

A rotatividade de funcionários pode gerar altos custos para a empresa. Para minimizar esse impacto, utilizamos técnicas de Machine Learning para identificar padrões em dados históricos e prever se um funcionário tem tendência a sair da empresa.

## 📌 Fluxo do Projeto

1. **Coleta de Dados**: Os dados são carregados do arquivo `modelagem_rh.csv`.
2. **Análise Exploratória**: Gráficos e estatísticas são gerados para entender a distribuição e padrões nos dados.
3. **Pré-processamento**: Tratamento de valores nulos, conversão de variáveis categóricas e normalização dos dados.
4. **Treinamento de Modelos**: Foram utilizados os algoritmos K-Nearest Neighbors (KNN) e Decision Tree.
5. **Validação**: Avaliação da performance dos modelos com métricas como acurácia e matriz de confusão.
6. **Deploy do Modelo**: O modelo treinado é salvo para uso futuro.