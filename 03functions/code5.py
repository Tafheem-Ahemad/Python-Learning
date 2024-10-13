
def solve(a, b):
	return a+b , a*b


add , mul=(100,200)
print(add)
print(mul)

add,_ = solve(10,20)
print(add)

mul,_ = solve(10,20) # it Return a "tuple"
print(mul)