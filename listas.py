#lista é como um array
#uma variável que pode armazenar vários valores
#e de vários tipos

#sintaxe

lista = [1,2,3]

# vários tipos de dados, ex

lista2 = [1, 'string', 2.4]

#uma lista tb é uam sequencia de indexação, então podemos
# chegar ao valor pelo índice (como um array)

#listas podem ser concatenadas com strings, ex:

lista + lista2

# somando um valor permanentea lista

lista = lista + ['valor permantente']

# métodos

lista.append('novo valor') #adicionando

lista.pop() # rétorna e retira o último índice por padrão

lista.pop(2) # retorna e retira o índice indicado

#reverse

lista.reverse() # inverte a ordem da lista permanentemente

lista.sort() #ordena a lista Alfabetica/numericamente

# listas dentro de listas

# as listasd permitem vários tipos de dados(inteiros, floats, strings), inclusive listas

#qual o resultado de lst[1:]?

lst=['a','b','c']

lst[1:] # retornará tudo após o primeiro indice (incluindo o indice 1)
