import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Grafics:
    def plotTripDurationByPrice():
        dim_payment_type = pd.read_csv('esquema_estrela/dim_payment_type.csv')
        fact_yellow_taxi = pd.read_csv('esquema_estrela/fact_yellow_taxi.csv')
        df = pd.merge(dim_payment_type, fact_yellow_taxi, left_on="id", right_on="payment_type", how='inner')
        df = df.groupby("description").size().reset_index(name="number_trips")
        
        plt.bar(df["description"], df["number_trips"], color="blue")

        plt.title("Quantidade de viagens por tipo de pagamento")

        plt.xlabel("Tipo de pagamento")
        plt.ylabel("Quantidade de viagens")
        
        return plt.show()
    
    def plotDurationTripPriceFinal():
        fact_yellow_taxi = pd.read_csv('esquema_estrela/fact_yellow_taxi.csv')
        final_fare = np.where(fact_yellow_taxi["final_fare"] > 0, fact_yellow_taxi["final_fare"], 0)
        plt.scatter(fact_yellow_taxi["trip_duration"], final_fare, color="red", marker="o", linewidth=1)
        
        plt.title("Relação entre duração da viagem e preço final")

        plt.xlabel("Duração da viagem (Horas)")
        plt.ylabel("Preço final da viagem")

        return plt.show()
    
    def plotDistanceTripPriceFinal():
        fact_yellow_taxi = pd.read_csv('esquema_estrela/fact_yellow_taxi.csv')
        trip_distance = np.where(fact_yellow_taxi["trip_distance"] > 0, fact_yellow_taxi["trip_distance"], 0)
        final_fare = np.where(fact_yellow_taxi["final_fare"] > 0, fact_yellow_taxi["final_fare"], 0)
        plt.scatter(trip_distance, final_fare, color="red", marker="o", linewidth=1)
        
        plt.title("Relação entre distância percorrida e preço final")

        plt.xlabel("Distância percorrida (Milhas)")
        plt.ylabel("Preço final da viagem")

        return plt.show()