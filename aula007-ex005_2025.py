#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('Escreva um número inteiro:'))
# s = n+1
# a = n-1
# print(f'O número que você digitou foi {n}, seu sucessor é {s} e seu antecessor é {a}.')

##Também é possível fazer da seguinte maneira (apenas 1 variavel, o que economiza a memória):
print(f'O número que você digitou foi {n}, seu sucessor é {n+1} e seu antecessor é {n-1}.')