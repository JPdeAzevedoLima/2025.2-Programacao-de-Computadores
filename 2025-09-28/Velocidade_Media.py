#Peça ao usuário a distância percorrida (em km) e o tempo gasto (em horas). Calcule a velocidade
#média e exiba o resultado.

distancia = float(input('Digite a  distância percorrida (em km): '))
tempo = float(input('Digie o tempo gasto (em horas): '))

velocidade_media = distancia / tempo

print(f'Sua velocidade média foi {velocidade_media:.2f} km/h')