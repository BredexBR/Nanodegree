import pandas as pd

def regras_tam_2(base, itens, taxa_sup, taxa_conf):
    """
    Gera e exibe regras de associação de tamanho 2 com base na base de dados fornecida.

    Parâmetros:
    - base: DataFrame contendo os itens e suas ocorrências (1 para presente, 0 para ausente).
    - itens: Lista de itens que serão analisados para formar regras.
    - taxa_sup: Suporte mínimo necessário para considerar a regra válida.
    - taxa_conf: Confiança mínima necessária para validar a regra.
    """

    # Percorre todos os itens na lista
    for i, item in enumerate(itens):
        # Percorre os itens seguintes na lista para formar pares (item, itens[j])
        for j in range(i + 1, len(itens)):
            # Conta quantas vezes os dois itens aparecem juntos na base de dados
            count_regra = len(base[(base[item] == 1) & (base[itens[j]] == 1)])

            # Calcula o suporte da regra (proporção de registros que contêm ambos os itens)
            suporte = count_regra / len(base)

            # Verifica se o suporte atende ao mínimo exigido
            if suporte >= taxa_sup:
                # Conta quantas vezes o primeiro item aparece na base
                count_a = len(base[base[item] == 1])

                # Calcula a confiança da regra (probabilidade de encontrar o segundo item, dado que o primeiro está presente)
                confianca = count_regra / count_a

                # Verifica se a confiança atende ao mínimo exigido
                if confianca >= taxa_conf:
                    # Exibe a regra de associação junto com seus valores de suporte e confiança
                    print(item, "-->", itens[j], 
                          "| suporte: ", suporte, 
                          "| confianca: ", confianca)

# Carrega a base de dados
base_transacional = pd.read_csv("docs/lista_compras.csv", sep=",")

# Calcula o suporte para cada item (soma dos 1s dividida pelo total de transações)
sup = base_transacional.sum() / len(base_transacional)

# Filtra os itens com suporte maior ou igual a 0.5
sup_itens = sup >= 0.5

regras = regras_tam_2(base_transacional, sup_itens.index, 0.02, 0.4)

# Chama a função com os parâmetros desejados (taxa de suporte e confiança)
print(regras)
