# é um tipo de estrutura de dados
# é semelhante a lista em relação a tamanho
# permite armazenar dados de vários tipos
# a diferença pras listas é a forma como acessamos os valores#
# o dicionário acessa os dados com mapeamento

dic = {'chave1':'arroz', 'chave2': 2, 'chave3': 3.2} 
# não existe uma sequência definida, (deve ser acesso através de chaves)
# é definindo entre chaves

# é possível colocar uma lista dentro de uma chave
# e por outra lista dentro dessa lista
# é muito flexível

#dicionários são mutáveis

dic = ['chave1'] = 'feijao' #muda o valor da chave1

# é possível criar um dicionário vazio

# é possível adicionar valores como se o dicionário ja existisse:

ex = ['chave'] = 'valor' 

# aninhamento
# é possivel por dicionários dentro de dicionários

dic.keys()# retornar todos os elementos do dicionários
list(dic.keys{}) # transforma o dict em lista

#db n estruturado são basicamente dicionários

dic.values() # retorna todos os valores do dic

# metodo items

dic.items() # retorna todos os itens, parecido com keys, mas mais legível

