#Solicite ao usuário uma temperatura em graus Celsius. Converta para Fahrenheit.

celsius = int(input('Digite a temperatura em graus Celsius: '))

fahrenheit = (celsius * 1.8) + 32

print(f'A temperatura em Fahrenheit é {fahrenheit:.1f}')