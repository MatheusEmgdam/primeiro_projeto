#Import do comando clear para limpeza do terminal
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while (True):
    #ENTRADA
    aparelho=input("\n Digite o tipo de aparelho\n")
    clear()
    potência=int(input("Digite a potência do aparelho em Watts\n"))
    clear()
    tempo=int(input("Digite o tempo médio do uso diário em horas\n"))
    clear()
    #PROCESSAMENTO
    consumoMensal=(potência*tempo*30)/1000
    #SAÍDA
    print(f"Aparelho: {aparelho} \n Consumo estimado: {consumoMensal}kWh/mês" )