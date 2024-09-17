
print("Ahemad")

s1 = "Tafheem"
s2 = "Ahemad"

def f1(s1):
	print(s1)

f1(10)

def f2(s2):
	print(s2)

f2(s2)

def f3(s1):
	print(s1)

f3(s1)

num= 10
f1(num)

num = "1000"
f1(num)


#input in python
num = input("Enter the number")
f1(num)

num = input()
f1(num)

# s1[0]='1'

# Number
# List
# String 
# Dictinonary
# Tuple
# Boolean
# None
# Set


# Muatble Immutable

# point to not same address
n1 = [1 , 2 ,3]
n2 = [1 , 2 ,3]

print (n1 == n2)
print (n1 is n2)

n1[0]=1111
f1(n1)
f1(n2)


# point to  same address , So if I change One second is change
n1 = [1 , 2 ,3]
n2 = n1

print (n1 == n2)
print (n1 is n2)


n1[0]=1111
f1(n1)
f1(n2)