# scopes.py
# Local vs Global scope

# Define a function that prints m
def local():
	# define m within the local scope
	m = 7
	print(m)
	
# define m within the global scope
m = 5

# call the function: Expected to print 7
local()

# call the value of m: its in the global scope, so not affected by the function
print(m)
