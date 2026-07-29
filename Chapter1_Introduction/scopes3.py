# scopes3.py
# Local, Enclosing and Global

def enclosing_function():
    # Define m within the enclosing function
	m = 13

	def local():
	
		"""
		m doesnt belong to the scope defined by the local function,
		so Python will keep looking into the next enclosing scope.
		This time m is found in the enclosing scope
		"""		
		print(m, "Printing from the local scope")
		
	# calling the  function local
	local()

# define m within the global scope
m = 5
print(m, "printing from the global scope")

# call the enclosing function
print("Calling the enclosing function")
enclosing_function()


