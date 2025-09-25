#02 - Desenvolva um programa em Python que solicite ao usuário os valores da base maior, base menor e altura de um trapézio e, 
#em seguida, calcule e exiba a sua área. Utilize a fórmula da área do trapézio. A = (B + b) * h.

print("Vamos calcular a área de um trapezio")

B = float(input("Olá, por favor digite o valor da base maior: "))
b = float(input("Olá, por favor digite o valor da base menor: "))
h = float(input("Olá, por favor digite o valor da altura: "))

area = (B + b) * h

print(f'O valor da área do trapezio é: {area:.2f}')