"""4. Faça um Programa que leia três números e mostre o maior deles"""

n1 = int(input("Numero 1\n"))
n2 = int(input("Numero 2\n"))
n3 = int(input("Numero 3\n"))

r = max(n1,n2,n3) # o método max recebe comp parametro algum valor, e itera sobre eles, trazendo o maior numero
print("O numero maior é", r)