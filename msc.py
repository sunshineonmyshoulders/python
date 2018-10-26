def encrypt(value):
	listChar=[]
	for i in range(len(value)):
		crypL=chr(ord(value[i])+i)
		listChar.append(crypL)
	return "".join(listChar)

value=input()
print(encrypt(value))

#EtCppjoGg:J;9;

