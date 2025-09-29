#Peça ao usuário um valor em reais (R$) e a cotação do dólar. Calcule e exiba quantos dólares
#ele teria com esse valor.

reais = float(input("Digite o valor em reais R$ "))
dolar = float(input("Digite a cotação do dólar $ "))

valor_convertido = reais / dolar

print(f'Você tem em dólares $ {valor_convertido:.2f}')