import socket, sys

t = sys.argv[1]
p = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((t,p))
r = s.recv(1024)
print(r)
s.close()