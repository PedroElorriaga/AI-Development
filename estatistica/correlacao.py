import pandas as pd

dict_infos = {
    'salary': [1900, 2000, 2500, 3200, 3900, 4100, 5000],
    'time-worked': [6, 10, 18, 24, 30, 40, 45]
}
dataframe_infos = pd.DataFrame.from_dict(dict_infos)


# CORRELAÇÃO PEARSON
data_pearson = dataframe_infos['salary'].corr(
    dataframe_infos['time-worked'], method='pearson')
# print(data_pearson) -> 0.9831678357600647


# CORRELAÇÃO PEARSON COM TODAS INFORMAÇÕES
data_pearson_all = dataframe_infos.corr(method='pearson')
# print(data_pearson_all) -> salary  time-worked
# salary       1.000000     0.983168
# time-worked  0.983168     1.000000


# CORRELAÇÃO SPEARMAN
data_spearman = dataframe_infos['salary'].corr(
    dataframe_infos['time-worked'], method='spearman')
# print(data_spearman) -> 1.0


# CORRELAÇÃO SPEARMAN COM TODAS INFORMAÇÕES
data_spearman_all = dataframe_infos.corr(method='spearman')
# print(data_spearman_all) -> salary  time-worked
# salary          1.0          1.0
# time-worked     1.0          1.0
