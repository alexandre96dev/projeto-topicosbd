import pandas as pd

schema = {
    'dim_ratecode': ['RatecodeID'],
    'dim_payment_type': ['payment_type'],
    'fact_vendas': ['id_venda', 'id_cliente', 'id_produto', 'quantidade', 'valor']
}

dataframe_ = pd.read_parquet('databases/yellow_tripdata_2023-03.parquet')


dim_ratecode = dataframe_[schema['dim_ratecode']]

dim_ratecode = dim_ratecode.loc[dim_ratecode['RatecodeID'].isin([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])]

dim_ratecode = dim_ratecode.drop_duplicates()



dim_payment_type = dataframe_[schema['dim_payment_type']]

dim_payment_type = dim_payment_type.loc[dim_payment_type['payment_type'].isin([1, 2, 3, 4, 5])]

dim_payment_type = dim_payment_type.drop_duplicates()


print(dim_payment_type)