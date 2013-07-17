# Import stuff

from machine import *
import strap

# Get command line arguments

args = strap.getArgs()

# Get raw code from file

code = strap.getCode(args[1])

# Covert code into tuples

tupleCode = strap.tuplize(code)

# Create an instance of the virtual machine

m = Machine((
    # If b is zero, then we are done.
    ('test', 'zero', 'b'),      # if b == 0
    ('branch', None),           # We're done
    ('copy', 't', 'a'),         # t <- a

    # If a < b, then we swap out b and a.
    ('test', 'lt', 't', 'b'),   # t < b?
    ('branch', 7),

    # Subtract out b from a.              
    ('exec', 't', 'sub', 't', 'b'), # t <- t-b
    ('jump', 3),

    ('copy', 'a', 'b'),         # a <- b
    ('copy', 'b', 't'),         # b <- t
    ('jump', 0),
    ))
m.a = 56
m.b = 12
m.execute()
print m.a
    
    
