#parte pratica da aula 07

# print(18 % 2)
# print(122 % 2)
# print(122 % 3)
# print(pow(4, 3))
# print(81 ** (1/2))
# print(25 ** (1/2))
# print(127 ** (1/3))

# nome = input('Qual é o seu nome?')
# print(f'Prazer em te conhecer, {nome}!')

# nome = input('Qual é o seu nome?')
# print(f'Prazer em te conhecer, {nome:20}!') #vinte espaços depois do input

# nome = input('Qual é o seu nome?')
# print(f'Prazer em te conhecer, {nome:>20}!') # > alinhamento à direita

# nome = input('Qual é o seu nome?')
# print(f'Prazer em te conhecer, {nome:<20}!') # < alinhamento à esquerda

# nome = input('Qual é o seu nome?')
# print(f'Prazer em te conhecer, {nome:^20}!') # ^ alinhamento centralizado

# pode ser mais explicito e incluir 'str' antes do input

# nome = input('Qual é o seu nome?')
# print(f'Prazer em te conhecer, {nome:=^20}!') # ^ alinhamento centralizado e a string anterior('=') preenche os vazios



# nome = input('Qual é o seu nome?')
# print(f'Prazer em te conhecer, {nome:x^20}!') # ^ alinhamento centralizado e a string anterior('x') preenche os vazios



# n1 = int(input('Digite um número inteiro qualquer:'))
# n2 = int(input('Digite mais um:'))
# # s = n1+n2 #é uma possibilidade, mas não precisa! se fizer essa opção, colocar substituir por "s" dentro das chaves
# print(f'A soma é {n1+n2}!')


# n1 = int(input('Digite um número inteiro qualquer:'))
# n2 = int(input('Digite mais um:'))
# s = n1+n2
# m = n1*n2
# d = n1/n2
# di = n1//n2 #divisão de inteiro
# e = n1**n2 #exponenciação

# print(f'A soma é {s}, o produto é {m}, a divisão {d} (sendo a inteira "{di}"), e potência é {e}!')



# n1 = int(input('Digite um número inteiro qualquer:'))
# n2 = int(input('Digite mais um:'))
# s = n1+n2
# m = n1*n2
# d = n1/n2
# di = n1//n2 #divisão de inteiro
# e = n1**n2 #exponenciação

# print(f'A soma é {s}, o produto é {m}, a divisão {d:.2f} (sendo a inteira "{di}"), e potência é {e}!') # para limitar o número de casas decimais (flutuantes) depois do ponto ":._f"




# n1 = int(input('Digite um número inteiro qualquer:'))
# n2 = int(input('Digite mais um:'))
# s = n1+n2
# m = n1*n2
# d = n1/n2
# di = n1//n2 #divisão de inteiro
# e = n1**n2 #exponenciação

# print(f'A soma é {s}, o produto é {m}.', end='') #no caso de uma sentença dividida, caso prefira juntar, antes de encerrar com parenteses, inclui ",end=''" e daí sim fecha. Se desejar incluir outro tipo de caractere na transição entre os trechos, basta colocar dentro ",end='XX'"
# print(f'a divisão {d:.2f} (sendo a inteira "{di}"), e potência é {e}!')



# n1 = int(input('Digite um número inteiro qualquer:'))
# n2 = int(input('Digite mais um:'))
# s = n1+n2
# m = n1*n2
# d = n1/n2
# di = n1//n2 #divisão de inteiro
# e = n1**n2 #exponenciação
#
# print(f'A soma é {s},\no produto é {m},\na divisão {d:.2f} (sendo a inteira "{di}"),\ne potência é {e}!') #na sentença inteira, caso prefira quebrar em trechos, inclui "\n" e não deixe espaço algum nem antes nem depois do '\n' caso queira os prints sem indentação ou paragrafo.



n1 = int(input('Digite um número inteiro qualquer:'))
n2 = int(input('Digite mais um:'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2 #divisão de inteiro
e = n1**n2 #exponenciação

print(f'A soma é {s},\no produto é {m},\na divisão {d:.2f} (sendo a inteira "{di}"),\ne potência é {e}!') #na sentença inteira, caso prefira quebrar em trechos, inclui "\n" e não deixe espaço algum nem antes nem depois do '\n' caso queira os prints sem indentação ou paragrafo.


