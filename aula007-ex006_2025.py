#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um número inteiro:'))
# d = n*2
# t = n*3
# rq = n**(1/2)

# print(f'Você digitou o número {n}. Seu dobro é {d}, o triplo é {t} e a raíz quadrada é {rq:.2f}.')

##outras maneiras de fazer!

## Economizando variáveis:

# print(f'Você digitou o número {n}. Seu dobro é {n*2}, o triplo é {n*3} e a raíz quadrada é {n**(1/2):.2f}.')

#com função "pow":

print(f'Você digitou o número {n}. Seu dobro é {n*2}, o triplo é {n*3} e a raíz quadrada é {pow(n,(1/2)):.2f}.')
