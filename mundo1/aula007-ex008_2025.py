#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.

n = float(input('Quantos metros tem o que você precisa medir?'))

cm = n*100
mm = n*1000

print(f'Você digitou "{n}m". Portanto, convertido temos {cm:.0f}cm ou {mm:.0f}mm. ')
