""" 7. Faça um programa para uma loja de tintas. O programa deverá pedir o 
tamanho em metros quadrados da área a ser pintada. Considere que a cobertura 
da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em 
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de 
latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos 
um número inteiro de latas."""

metros_area = float(input("Área que será pintada\n"))

litros = metros_area / 3 # para cada metro, 3 litros#

if litros % 18 == 0: # se a sobra da divisão de litros por 18 for igual a 0
	latas = litros / 18 # atribuimos a latas o valor de ltiro dividido por 18, que será nossa quantidade de latas
else:
	latas = int(litros/18) + 1 # se não, fazemos a mesma coisa somando 1, para os casos em que se use apenas uma lata, ou que
	#passe de 1 lata por pouco


preco = latas * 80

print("Metros que serão pintados", metros_area)
print("Litros necessários", litros)
print("Latas necessárias", latas)
print("Preço", preco)

