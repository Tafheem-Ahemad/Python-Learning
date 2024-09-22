# Question 7

def sum_all(*args):
	return sum(args)

print(sum_all(10 , 20 ,40))
print(sum_all(40,50))

# Question 5

def area(**kwargs):
	if "lenth" in kwargs.keys() and "breath" in kwargs.keys() : return kwargs["lenth"] * kwargs["breath"]
	else : return -1


print(area(lenth = 10 , breath =20))
print(area(lenth = 10))
print(area())