"""9) Escreva um programa que pergunte a quantidade de km percorridos por um 
carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro 
foi alugado. Calcule o preço a pagar, 
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado."""

km = int(input("Km percorridos\n"))
d = int(input("Dias totais do aluguel\n"))

preco = 0


for i in range(km):
	preco += 00.15
for i in range(d):
	preco += 60.00

print("O preço a pagar é de", preco)