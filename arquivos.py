# abrindo arquivos com python

# função open abre um arquivo

arq = open('arquivo.txt') # abre o arquivo

arq.read() #le o arquivo dentro da variavel arq

arq.readline() #le a primeira linha, depois a sdegunda, etc

arq.seek(0) # resete o local onde esta a linha a ser lida 

for line in arq:
	print(line) # ira printar todas as linhas