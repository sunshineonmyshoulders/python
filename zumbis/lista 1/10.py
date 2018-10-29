"""0) Escreva um programa para calcular a redução do tempo de vida de um fumante. 
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
 Considere que um fumante perde 10 minutos de vida a cada cigarro, 
 calcule quantos dias de vida um fumante perderá. Exiba o total de dias."""

cigarros = int(input("Cigarros fumados por dia\n"))
anos = int(input("Anos fumando\n"))
minutos = 0
d = 0

for i in range(anos):
	cigarros = cigarros * 365 # para cada ano os cigarros diários são multiplicados por 365 

for i in range(cigarros):
	minutos += 10 # para cada cigarro os minutos perdidos são aumentados em 10

d = minutos // 1440 # dividindo o total de minutos perdidos pela quantidade de minutos em um dia



print("Você fumou", cigarros, "cigarros")
print("Minutos perdidos", minutos)
print("Dias", d)

# hora 60
# dia 1440
# ano 525.600