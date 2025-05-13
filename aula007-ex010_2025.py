#Crie um programa que leia quanto dinheiro uma pesssoa tem na carteira e mostre quantos Dólares ela pode comprar .
#Considere US$1,00 = R$5,68

n = float(input('Quanto você deseja converter para o valor do dólar de hoje? R$'))
c = (n/5.63) #alterar para cotação do dia
print(f'O valor digitado foi R${n:.2f} e, com o câmbio valendo R$5.68 a cada 1U$, você terá: U${c:.2f}.Caso se interesse por outras cotações, segue:\nEUR${n/6.62:.2f}(euros);\nCAD${n/4.02:.2f}(dólar-canadense);\nGBP${n/7.44:.2f}(libra-esterlina);\nCNY${n/0.78:.2f}(yuan-chinês).')