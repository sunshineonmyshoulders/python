"""4) Faça um programa que calcule o aumento de um salário. 
Ele deve solicitar o valor do salário e a porcentagem do aumento.
 Exiba o valor do aumento e do novo salário. """

salario = int(input("Salario atual\n"))
aumento = int(input("Aumento em %\n"))

aumento = salario // 100 * aumento # convertendo o salário em % dividindo por 100, barras // para dispensar casa decimal
# e multiplicando o valor da % pelo aumento

print("O novo salário com aumento será de R$", salario + aumento)
