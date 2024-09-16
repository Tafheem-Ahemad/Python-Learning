
def f1(s):
	print(s)

s1 = "abcdefghij"
f1(s1)

# S[2]= 'z' // Give Error

# Slice [  x : y : z] 
#  from index x to y (y not inclusive) in  z steps

s2 = s1.strip() # remove space from back and front
f1(s2)

s3 = s1.replace("de" , "xx")
f1(s3)

s3 = s1.replace("df" , "xx")
f1(s3)

# Split the string according to same spliter 
s4 = "a b c d e f g h"
li = s4.split(" ")  # space id bydefault

f1(li)

# Give some input
s5 = "I am {} and age is {}"
f1(s5.format("Ahemad" , 26)) 


# Join some list
li = ["1" , "2" ,"3" , "4"]
s6 = ",".join(li)

f1(s6)

f1(len(li))


#  For raw format
s7 = r"c:user\pwd"
f1(s7)

print("Ahemad" in "Tafheem Ahemad")