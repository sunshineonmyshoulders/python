"""2. Determine se um ano é bissexto. Verifique no Google como fazer isso."""

ano = int(input("Digite o ano\n"))

if ano % 4 == 0 and ano % 100 != 0: # se o o resultado da divisão por 4 for = 0
# e o resultado da divisão por 100 for diferente de 0, então e bissexto
	print("É bissexto")
else:
	print("Não é bissexto")

# Para ser bissexto, o ano deve ser:
#Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
#Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;