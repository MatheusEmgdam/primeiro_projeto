import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while (True):
    aparelho=input("\n Digite o tipo de aparelho\n")
    clear()
    potência=int(input("Digite a potência do aparelho em Watts\n"))
    clear()
    tempo=int(input("Digite o tempo médio do uso diário em horas\n"))
    clear()
    consumoMensal=(potência*tempo*30)/1000
    print(f"Aparelho: {aparelho} \n Consumo estimado: {consumoMensal}kWh/mês" )