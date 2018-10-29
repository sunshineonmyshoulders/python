"""  6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e 
o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos 
e o salário líquido, conforme a tabela abaixo: 
a. + Salário Bruto : 
R$ b. - IR (11%) :
 R$ c. - INSS (8%) :
  R$ d. - Sindicato ( 5%) : 
  R$ e. = Salário Liquido : R$"""

valor_hora = int(input("Valor por hora trabalhada\n"))
hora_mes = int(input("Total de horas trabalhadas no mês\n"))

salario = valor_hora * hora_mes # total bruto
ir = salario // 100 * 11 # 11 % de ir
inss = salario // 100 * 8 # 8 % de inss
sindicato = salario // 100 * 5 # 5 % do sindicato

print("Salário bruto: R$", salario)
print("DESCONTOS")
print("IR (11%)        R$", ir)
print("INSS (8%)       R$", inss)
print("Sindicato (%5)  R$", sindicato)
print("TOTAL DESCONTOS R$", ir + inss + sindicato)
print("Liquido:        R$", salario - ir - inss - sindicato)