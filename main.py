from etl import Etl
from grafics import Grafics

feedDatabase = Etl()

feedDatabase.etl()

menu = ["1", "2", "3"]

opcao = input("Escolha uma opção: 1 - Grafico com relação duração viagem x preço final, 2 - Grafico com relação tipo de pagamento x quantidade de viagens, 3 - Grafico com relação distância percorrida x preço final \n")

if opcao == menu[0]:
    print("Opção 1 selecionada")
    Grafics.plotDurationTripPriceFinal()
    
elif opcao == menu[1]:
    print("Opção 2 selecionada")
    Grafics.plotTripDurationByPrice()
elif opcao == menu[2]:
    print("Opção 3 selecionada")
    Grafics.plotDistanceTripPriceFinal()
else:
    print("Opção inválida")