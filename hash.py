import sys, hashlib

m = sys.argv[1]
n = sys.argv[1]
o = sys.argv[1]
m = hashlib.md5().hexdigest()
n = hashlib.sha224().hexdigest()
o = hashlib.sha512().hexdigest()

print('md5:',m)
print('sha224:',n)
print('sha512:',o)