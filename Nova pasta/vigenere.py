import sys
from string import ascii_lowercase as lc 

file = open(sys.argv[1],'r').read().lower()
key = sys.argv[2].lower()
mode = sys.argv[3]

result = ''
keyidx = 0
idx = 0

for lt in file:
	if lt in lc:
		if mode == 'enc':
			idx += lc.find(key[keyidx%len(key)])
		elif mode == 'dec':
			idx -= lc.find(key[keyidx%len(key)])
		result += lc[idx%26]
	else:
		result += lt

print(result)