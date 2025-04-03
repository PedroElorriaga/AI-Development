import pandas as pd

dict_infos = {
    'ages': [10, 13, 15, 19, 20, 22, 44, 45, 67, 67],
    'height': [1.6, 1.63, 1.69, 1.72, 1.72, 1.78, 1.82, 1.83, 1.85, 1.85]
}
dataframe_infos = pd.DataFrame.from_dict(dict_infos)

# MÉDIA
data_age_media = dataframe_infos['ages'].mean()
# print(data_age_media) -> 32.2


# MEDIANA (é um valor que se encontra no centro de um conjunto de números ordenados, dividindo-o em duas partes iguais)
data_age_mediana = dataframe_infos['ages'].median()
# print(data_age_mediana) -> 21.0


# MODA
data_age_moda = dataframe_infos['ages'].mode()
# print(data_age_moda) -> 67


# VARIÂNCIA (é um conceito estatístico que diz respeito à distância que um valor médio apresenta do demais valores de um conjunto de dados.)
data_age_variance = dataframe_infos['ages'].var()
# print(data_age_variance) -> 478.8444444444445


# DESVIO PADRÃO
data_age_desv_padrao = dataframe_infos['ages'].std()
# print(data_age_desv_padrao) -> 21.882514582297084


# COEFICIENTE DE VARIAÇÃO
data_age_coef_var = data_age_desv_padrao / data_age_media * 100
# print(data_age_coef_var) -> 67.95811982079839


# ASSIMETRICA
data_age_assimetric = dataframe_infos['ages'].skew()
# print(data_age_assimetric) -> 0.7919017145680367


# CURTOSE
data_age_curtose = dataframe_infos['ages'].kurtosis()
# print(data_age_curtose) -> -0.999100756785587


# OBTER MEDIDAS ESTATISTICAS
data_age_statistics = dataframe_infos['ages'].describe()
# print(data_age_statistics)
# - > count    10.000000
# mean     32.200000
# std      21.882515
# min      10.000000
# 25%      16.000000
# 50%      21.000000
# 75%      44.750000
# max      67.000000
