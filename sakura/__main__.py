# Import stuff

from machine import *
import strap

# Get command line arguments

args = strap.getArgs()

# Get raw code from file

code = strap.getCode(args[1])

# Covert code into tuples

tupleCode = strap.tuplize(code)

# Create an instance of the virtual machine with the tuple code

m = Machine(tupleCode)

m.a = 56
m.b = 12
m.execute()
print m.a
    
    
