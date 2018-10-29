"""6) Calcule o tempo de uma viagem de carro. 
Pergunte a distância a percorrer e a velocidade média esperada para a viagem"""

distancia = int(input("Distancia em km\n"))
velocidade = int(input("Velocidade media\n"))

tempo = distancia // velocidade

print("O tempo de viagem será de aproximadamente",tempo,"horas")