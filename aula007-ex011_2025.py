#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
l = float(input('Qual a largura da parede, em metros?'))
h = float(input('Qual a altura da parede?'))
a = (l*h)
ap = (a/2)

print(f'Considerando a largura da parede {l}m e a altura {h}m, temos que a área da parede é {a:.2f}m².\n'
       f'Se cada litro de tinta pinta 2m², a quantidade para pintá-la por completo é de {ap:.2f}l.')
