# Bootstrapper 

import sys
import io
import re

# Gets command line arguments

def getArgs():
    
    return sys.argv
    
# Reads in data fom raw file   

def getCode(filepath):
    
    return io.open(filepath, 'rt').read()

# Converts raw file code into organized tuples

def tuplize(code):
	
	codeList = code.split('\n')
	dubsy = []

	for i, line in enumerate(codeList):
		if line.find(';') != -1:
			codeList[i] = line[:line.find(';')].strip()

	for line in codeList:
		dubsy.append((re.split(r'[,\s]+', line)))
	
	dubsy = dubsy[0:-1]

	# Convert number strings to integers and convert None strings to actual None's

	for i, thing in enumerate(dubsy):	
		for k, thingy in enumerate(thing):	
			if re.compile('[0-9]+').match(thingy) != None:
				dubsy[i][k] = int(thingy)
			if re.compile('None').match(thingy) != None:
				dubsy[i][k] = None

	return tuple(dubsy)
	