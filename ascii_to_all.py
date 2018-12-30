#!/usr/bin/python2.7
import sys


print "Character:Binary   Octal Decimal Hexadecimal"

character = sys.argv[1]
for i in range(len(character)):
	decimal = ord(character[i])
	binary = bin(decimal)
	octal = oct(decimal)
	hexadecimal = hex(decimal)

	print "%s\t:%s %s   %s\t %s"%(sys.argv[1][i],binary,octal,decimal,hexadecimal)