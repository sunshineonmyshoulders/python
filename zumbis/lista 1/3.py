"""3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
Cacule o total em segundos"""

d = int(input("Dias\n")) # 86.400
h = int(input("horas\n")) # 3600
m = int(input("minutos\n")) # 60
s = int(input("segundos\n"))

segundos = 0

for dia in range(d):
	segundos += 86400
for hora in range(h):
	segundos += 3600
for minuto in range(m):
	segundos += 60
for seg in range(s):
	segundos += 1

#segundos = d + h + m + s

print("Convertendo tudo em segundos, o total é:", segundos)