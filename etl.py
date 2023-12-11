import pandas as pd
from database import Database
class Etl:
    def etl(self):
        meses = ['01', '02']

        # dataframe_01 = pd.read_parquet('databases/yellow_tripdata_2023-01.parquet')
        # dataframe_02 = pd.read_parquet('databases/yellow_tripdata_2023-02.parquet')
        # dataframe_03 = pd.read_parquet('databases/yellow_tripdata_2023-03.parquet')
        # dataframe_04 = pd.read_parquet('databases/yellow_tripdata_2023-04.parquet')
        # dataframe_05 = pd.read_parquet('databases/yellow_tripdata_2023-05.parquet')
        # dataframe_06 = pd.read_parquet('databases/yellow_tripdata_2023-06.parquet')
        # dataframe_07 = pd.read_parquet('databases/yellow_tripdata_2023-07.parquet')
        # dataframe_08 = pd.read_parquet('databases/yellow_tripdata_2023-08.parquet')
        # dataframe_09 = pd.read_parquet('databases/yellow_tripdata_2023-09.parquet')

        # dataframe = pd.concat([dataframe_01, dataframe_02, dataframe_03, dataframe_04, dataframe_05, dataframe_06, dataframe_07, dataframe_08, dataframe_09])

        df = pd.read_parquet('databases/yellow_tripdata_2023-01.parquet')

        df = df.dropna(subset=['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count'])

        # Corrigindo erros de digitação ou formatação nas colunas
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

        # Normalizando os valores das colunas para garantir que estejam no formato correto
        df['passenger_count'] = df['passenger_count'].astype('int')
        del df['VendorID']
        del df['store_and_fwd_flag']
        
        # ETL

        # Calculando a duração da viagem
        df['duracao_viagem'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 3600

        df['trip_distance'] = df['trip_distance'] * 1609.344

        # Calculando a tarifa final
        df['tarifa_final'] = df['total_amount'] + df['extra'] + df['mta_tax'] + df['improvement_surcharge'] + df['tip_amount'] + df['tolls_amount'] + df['congestion_surcharge'] + df['airport_fee']
        
        dim_taxi = pd.read_csv('databases/taxi+_zone_lookup.csv')
        
        
        
        

t = Etl()
t.etl()
