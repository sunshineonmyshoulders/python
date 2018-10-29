"""5) Solicite o preço de uma mercadoria e o percentual de desconto.
 Exiba o valor do desconto e o preço a pagar. """


preco = int(input("Digite o preço\n"))
desconto = int(input("Descondo em %\n"))

porcentagem = preco // 100 * desconto

print("O valor final é", preco - porcentagem)
print("Desconto de", porcentagem, "reais")