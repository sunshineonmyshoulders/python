""" 7. Faça um programa para uma loja de tintas. O programa deverá pedir o 
tamanho em metros quadrados da área a ser pintada. Considere que a cobertura 
da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em 
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de 
latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos 
um número inteiro de latas."""

metros_area = int(input("Área que será pintada\n"))

litros = metros_area * 3 # para cada metro, 3 litros
lata = litros // 18 # pegando a quantidade de latas baseada nos litros

if lata == 0: #and litros < 18: # se a quantidade de litros for maior que zero e diferente de 18, lata recebe + 1
	lata += 1 # isso evita que caso a quantidade de litros necessários sejam menores que 18, as latas fiquem zeradas


preco = lata * 80

print("Metros que serão pintados", metros_area)
print("Litros necessários", litros)
print("Latas necessárias", lata)
print("Preço", preco)
# 1 lada para cada 54 metros
# 1 litro para cada 3 metros
# lata = 18 litros 
# preço 80