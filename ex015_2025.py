#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Qual a quantidade de km percorridos?'))
dias = int(input('Por quantos dias você locou o carro?'))
aluguel = (60*dias) + (0.15*km)
print(f'Você precisará pagar R${aluguel:.2f} pelos {dias} dias de locação, considerando os {km:.0f}km rodados.')