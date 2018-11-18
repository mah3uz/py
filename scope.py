'''
LEGB
Local, Enclosing, Global, Built-in
'''

x = "Global X"

def outer():
	x = 'outer x'

	def inner():
		nonlocal x
		x = 'inner x'
		print(x)

	inner()
	print(x)

outer()
print(x)
