p1,p2,p3,p4,p5,p6,p7,p8,p9 = '','','','','','','','',''

def print_t():
	print(p1,'/',p2,'/',p3)
	print(p4,'/',p5,'/',p6)
	print(p7,'/',p8,'/',p9)


def jogada_0():
	global p1,p2,p3,p4,p5,p6,p7,p8,p9 
	j = input("Vez do jogador O, escolha uma posição ")
	if j == '1':
	    p1 = 0
	elif j == '2':
		p2 = 0
	elif j == '3':
		p3 = 0
	elif j == '4':
		p4 = 0
	elif j == '5':
		p5 = 0
	elif j == '6':
		p6 = 0
	elif j == '7':
		p7 = 0
	elif j == '8':
		p8 = 0
	elif j == '9':
		p9 = 0
	else:
		print("Digite uma posição entre 1 e 9")
		
def jogada_X():
	global p1,p2,p3,p4,p5,p6,p7,p8,p9 
	j = input("Vez do jogador X, escolha uma posição ")
	if j == '1':
		p1 = 'X'
	elif j == '2':
		p2 = 'X'
	elif j == '3':
		p3 = 'X'
	elif j == '4':
		p4 = 'X'
	elif j == '5':
		p5 = 'X'
	elif j == '6':
		p6 = 'X'
	elif j == '7':
		p7 = 'X'
	elif j == '8':
		p8 = 'X'
	elif j == '9':
		p9 = 'X'
	else:
		print("Digite uma posição entre 1 e 9")

def confere():
	if p1 and p2 and p3 == '0':
		print("O jogador 0 venceu")
		
print_t()
jogada_0()
print_t()
confere()
jogada_X()
print_t()
confere()
jogada_0()
print_t()
confere()
jogada_X()
print_t()
confere()
jogada_0()
print_t()
confere()
jogada_X()
print_t()
confere()
jogada_0()
print_t()
confere()
jogada_X()
print_t()
confere()
jogada_0()
print_t()

