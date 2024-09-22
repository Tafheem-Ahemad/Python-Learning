
# Factorial numbers

def factorail( n : int):
	if(n<=1): return 1
	else: return n*factorail(n-1)


print(factorail(20))
print(factorail(4))



# fibonnacy numbers
def fibo(n : int):
	if(n<0):  return  -1
	if(n==0): return 0
	if(n==1): return 1

	return fibo(n-1)+ fibo(n-2)


print(fibo(12))
print(fibo(8))
print(fibo(2))