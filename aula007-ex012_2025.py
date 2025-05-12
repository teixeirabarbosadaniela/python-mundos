#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# n = float(input('Quanto custa o produto?'))
# d = n-(5/100)
# print(f'O preço do produto é R${n} e, com desconto de 5%, passa a ser R${d}')

n = float(input('Quanto custa o produto?'))
d = n-(n*5/100)
print(f'O preço do produto é R${n} e, com desconto de 5%, passa a ser R${d:.2f}')

