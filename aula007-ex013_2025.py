#Faça um algoritmo quew leia bo salário de um funcionário e mostre seu novo saláqrio com 15% de aumento.
s = float(input('Qual o seu salário atual?'))
aumento = s + (s*15/100)
print(f'Seu salário atual é R${s:.2f} e, após aplicado aumento de 15%, passará a ser R${aumento:.2f}.')


