#01 - Desenvolva um programa em Python que solicite ao usuário o valor do raio de um círculo e, em seguida, 
#calcule e exiba a área do círculo. Utilize a fórmula da área do círculo. Considere o valor de π = 3.1416. A = pi * r².
valor_raio = float(input("Olá, por favor digite o valor do raio de um círculo: "))

valor_pi = 3.1416

area = valor_pi * (valor_raio ** 2)

print(f'O valor da área do círculo é: {area:.2f}')