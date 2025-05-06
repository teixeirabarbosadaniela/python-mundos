#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um número inteiro:'))
d = n*2
t = n*3
rq = n**(1/2)

print(f'Você digitou o número {n}. Seu dobro é {d}, o triplo é {t} e a raíz quadrada é {rq:.2f}.')

