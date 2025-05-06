#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média (atenção à ordem de precedencia).

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))

m = (n1+n2)/2

print(f'A primeira nota foi {n1}, a segunda foi {n2} e a média das duas é {m:.1f}.')