"""1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores 
podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: 
equilátero, isósceles ou escaleno. """

l1 = int(input("lado 1\n"))
l2 = int(input("lado 2\n"))
l3 = int(input("lado 3\n"))

t = l1 + l2 + l3
if t == 180:
	if l1 == l2 and l2 == l3:
		print("É um equilátero")
	if l1 == l2 and l2 != l3 or l1 != l2 and l2 == l3:
		print("É um isósceles")
	if l1 != l2 and l2 != l3:
		print("É um escaleno")
else:
	print("Não é um triângulo")

# Triângulo é o polígono com o menor número de lados (3 lados) e a soma dos seus ângulos internos é igual a 180o.
# Triângulo Equilátero: é todo triângulo que apresenta os três lados com a mesma medida. 
# Triângulo Isósceles: é todo triângulo que apresenta dois lados com a mesma medida, ou seja, dois lados de tamanhos iguais.
# Triângulo Escaleno: é todo triângulo que apresenta os três lados com medidas diferentes, ou seja, três lados de tamanhos diferentes.