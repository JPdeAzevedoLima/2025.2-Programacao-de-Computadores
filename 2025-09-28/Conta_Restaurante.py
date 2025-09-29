#Peça ao usuário o valor da conta e a porcentagem de gorjeta que deseja dar.
#Calcule o valor total a pagar e exiba com uma mensagem.

conta = float(input('Digite o valor da conta: '))

porcentagem = int(input('Digite o valor da porcentagem a ser acrescentada: '))

total = ((porcentagem / 100) + 1) * conta

print(f'O valor total da conta com a gorgeta é R$ {total:.2f}')