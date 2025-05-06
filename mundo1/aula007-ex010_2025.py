#Crie um programa que leia quanto dinheiro uma pesssoa tem na carteira e mostre quantos Dólares ela pode comprar .
#Considere US$1,00 = R$5,68

n = float(input('Quanto você deseja converter para o valor do dólar de hoje?'))
c = (n/5.68)
print(f'O valor digitado foi R${n} e, com o câmbio valendo R$5.68 a cada 1U$, você terá: U${c:.2f}.')