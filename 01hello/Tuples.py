
def f1(s):
	print(s)

# Tuple is imuatable and ordered
tu = (10 , 100 ,40 , 20 , 10 , 100 , 40 , 20)

f1(tu)
f1(tu.count(10))

f1(tu.index(100))
f1(tu[2]) #access the element of tuple like list

f1(tu[1: 7 : 2]) #access the element of tuple like list

# tu[4] = 200 #error because tuple is immutable

tu2 = (10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 , 100)


t3 = tu+tu2 # add two tuple like list
f1(t3)