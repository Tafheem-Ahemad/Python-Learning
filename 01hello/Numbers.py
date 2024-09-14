
from decimal import Decimal
from fractions import Fraction
import random
import math

def f1(s):
	print(s)

num1 = "10 "
num2 = num1*12

f1(num2)

num2 = int(12.55)
f1(num2)

num1 = 2 ** 1000
# f1(num1)

# ** --> power
# // --> devide not get the decimal value

f1(True)

# Operaters same as C++

num1 = 10
num1+=1

f1(num1)

comlex_number = 2 + 1j
f1(comlex_number)

number = 9463243863845638 * 555
f1(number)

number =  9463243863845638 * 2.5
f1(number)

# Conert to binary , octal , hexadecimal
n1 = oct(100)
f1(n1)

n1 = hex(100)
f1(n1)

n1 = bin(100)
f1(n1)

#  To a specific base
n1 = int(str(100),8)
f1(n1)

# n1 = int("Ahemad") // give error
# f1(n1)

f1(type (n1)) # type 

f1 (1 << 5) # bitwise 

# Set
st = { 1 , 2 , 3}
st.add(10)
st.add(1)

f1(st)

st.clear()

f1(st)


f1(random.choice([10 ,20 , 30 , 40 , 50]))
f1(random.random())

f1(random.randint(10 , 100))

f1(math.log(5,2))
f1(math.factorial(40))
f1(int(math.log2(10)))
f1(int(math.sqrt(101)))

f1(min(10,-1.2))
f1(max(10,-1.2))

