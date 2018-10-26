import socket, sys

#alvo = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r = b"GET / HTTP/1.1" #\nHost: www.cnn.com\n\n"

s.connect(("www.cnn.com", 80))
s.send(r)
result = s.recv(10000)
while (len(result) > 0):
    print(result)
    result = s.recv(10000)
s.close()


"""import socket
request = b"GET / HTTP/1.1\nHost: www.cnn.com\n\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("cnn.com", 80))
s.send(request)
result = s.recv(10000)
while (len(result) > 0):
    print(result)
    result = s.recv(10000)"""