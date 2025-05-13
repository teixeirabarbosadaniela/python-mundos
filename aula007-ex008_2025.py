#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.

n = float(input('Quantos metros tem o que você precisa medir?'))

# cm = n*100
# mm = n*1000

# print(f'Você digitou "{n}m". Portanto, convertido temos {cm:.0f}cm ou {mm:.0f}mm. ')

##durante a correção, o guanabara pede pra que o exercício seja complementado com as demais medidas:

print(f'Você digitou "{n:.0f}m".\nPortanto, a tabela com a escala torna-se:\n{n*0.001:.1f}km;\n{n*0.01:.0f}hm;\n{n*0.1:.0f}dam;\n{n:.0f}m;\n{n*10:.0f}dm;\n{n*100:.0f}cm e;\n{n*1000:.0f}mm.')
