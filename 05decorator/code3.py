

def memoisation(func):
	dp={};
	def wrapper(*args):
		if(args in dp) : return dp[args]
		result=func(*args)
		dp[args]=result
		return result
	return wrapper

@memoisation
def fibonacci(n:int):
	if(n<=1): return n;
	return fibonacci(n-1)+fibonacci(n-1);

print(fibonacci(100))
print(fibonacci(10))