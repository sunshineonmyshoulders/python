"""Challenge
Using the Python language, have the function FirstReverse(str) take the str parameter 
being passed and return the string in reversed order. For example: if the input 
string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH. """

import sys

def FirstReverse(str):
	return str[::-1] # Em python, é possível tratar uma string como uma list usando os []

print(FirstReverse(sys.argv[1]))


 # the easiest way to reverse a string in python is actually the following way:
 # in python you can treat the string as an array by adding [] after it and 
 # the colons inside represent str[start:stop:step] where if step is a negative number
 # it'll loop through the string backwards