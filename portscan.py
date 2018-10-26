import socket, sys

ip = sys.argv[1]

for porta in range(1,65535):
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 print("Varrendo porta", porta)
 if s.connect_ex((ip,porta)) == 0:
 	print(porta, "OPEN")
 s.close()

