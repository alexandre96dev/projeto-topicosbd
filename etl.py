import pandas as pd
from database import Database
class Etl:
    def etl(self):
        dataframe_01 = pd.read_parquet('databases/yellow_tripdata_2023-01.parquet')
        # dataframe_02 = pd.read_parquet('databases/yellow_tripdata_2023-02.parquet')
        # dataframe_03 = pd.read_parquet('databases/yellow_tripdata_2023-03.parquet')
        # dataframe_04 = pd.read_parquet('databases/yellow_tripdata_2023-04.parquet')
        # dataframe_05 = pd.read_parquet('databases/yellow_tripdata_2023-05.parquet')
        # dataframe_06 = pd.read_parquet('databases/yellow_tripdata_2023-06.parquet')
        # dataframe_07 = pd.read_parquet('databases/yellow_tripdata_2023-07.parquet')
        # dataframe_08 = pd.read_parquet('databases/yellow_tripdata_2023-08.parquet')
        # dataframe_09 = pd.read_parquet('databases/yellow_tripdata_2023-09.parquet')

        # fact_yellow_taxi = pd.concat([dataframe_01, dataframe_02, dataframe_03, dataframe_04, dataframe_05, dataframe_06, dataframe_07, dataframe_08, dataframe_09])
        
        fact_yellow_taxi = pd.concat([dataframe_01])

        # Corrigindo erros de digitação ou formatação nas colunas
        fact_yellow_taxi['tpep_pickup_datetime'] = pd.to_datetime(fact_yellow_taxi['tpep_pickup_datetime'])
        fact_yellow_taxi['tpep_dropoff_datetime'] = pd.to_datetime(fact_yellow_taxi['tpep_dropoff_datetime'])
        
        #tirando colunas desnecessárias
        del fact_yellow_taxi['VendorID']
        del fact_yellow_taxi['store_and_fwd_flag']

        # Calculando a duração da viagem
        fact_yellow_taxi['trip_duration'] = (fact_yellow_taxi['tpep_dropoff_datetime'] - fact_yellow_taxi['tpep_pickup_datetime']).dt.total_seconds() / 3600

        # Calculando a tarifa final
        fact_yellow_taxi['final_fare'] = fact_yellow_taxi['total_amount'] + fact_yellow_taxi['extra'] + fact_yellow_taxi['mta_tax'] + fact_yellow_taxi['improvement_surcharge'] + fact_yellow_taxi['tip_amount'] + fact_yellow_taxi['tolls_amount'] + fact_yellow_taxi['congestion_surcharge'] + fact_yellow_taxi['airport_fee']
        
        #carregando e limpando dados dos códigos de localização 
        dim_locations = pd.read_csv('databases/taxi+_zone_lookup.csv')
        dim_locations = dim_locations.dropna(subset=['Zone', 'service_zone'])
        
        dim_payment_type = pd.DataFrame({'id': [1,2,3,4,5,6], 'description': ['Credit card', "Cash", "No charge", "Dispute", "Unknown", "Voided trip"]})
        dim_rate_code = pd.DataFrame({'id': [1,2,3,4,5,6], 'description': ['Standard rate', "JFK", "Newark", "Nassau or Westchester", "Negotiated fare", "Group ride"]})
        column_exists = 'Airport_fee' in fact_yellow_taxi.columns
        
        if column_exists:
            del fact_yellow_taxi['Airport_fee']
        
        fact_yellow_taxi['airport_fee'] = fact_yellow_taxi['airport_fee'].fillna(0)
        
        db = Database()
        
        dim_locations.to_csv("esquema_estrela/dim_locations.csv")
        dim_payment_type.to_csv("esquema_estrela/dim_payment_type.csv")
        dim_rate_code.to_csv("esquema_estrela/dim_rate_code.csv")
        fact_yellow_taxi.to_csv("esquema_estrela/fact_yellow_taxi.csv")
        
        db.connection.close()