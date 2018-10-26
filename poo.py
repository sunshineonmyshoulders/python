## Orientação a objetos

# Tudo em python é um objeto

# Criando um objeto

class Exemplo(object)
  pass

x = Exemplo() # Instanciamos a classse exemplo 
#atribuindo o valor dela a uma variavel

# Por convenção o nome da classe sempre deve começar com letra Maiúscula

# Atributos

class Gato(object):
	def __init__(self,cor): # o método especial init serve para inicializar atributos de um objeto
			self.cor = cor 

pixel = Gato(cor='listrado')
vick = Gato(cor='cinza')