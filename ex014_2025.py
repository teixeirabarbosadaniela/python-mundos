#Escreva um programa que converta uma temperatura em Celsius para Fahrenheit.

c = float(input('Informe a temperatura em °C:'))
f = ((9*c)/5)+32 #fórmula (não precisaria dos parentes, considerando regra de precedência)

print(f'A temperatura de {c:.1f}°C corresponde a {f:.1f}°F!')