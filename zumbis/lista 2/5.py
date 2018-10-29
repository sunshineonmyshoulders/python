"""5. Faça um Programa que leia três números e mostre o maior e o menor deles. """

"""4. Faça um Programa que leia três números e mostre o maior deles"""

n1 = int(input("Numero 1\n"))
n2 = int(input("Numero 2\n"))
n3 = int(input("Numero 3\n"))

r = min(n1,n2,n3) # o método min recebe comp parametro algum valor, e itera sobre eles, trazendo o menor numero
print("O numero menor é", r)