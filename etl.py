import pandas as pd
import sqlite3

class Etl:
    def __init__(self):
        self.dataframe = ''
    def etl(self):
        dataframe = pd.read_parquet('databases/yellow_tripdata_2023-03.parquet')
        print(dataframe)
