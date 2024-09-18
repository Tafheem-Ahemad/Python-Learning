# While loop

print("Question 6")
n = int(input("Enter your number "))

i =n 
ans=1

while (i>0):
	ans*=i
	i-=1

print(ans)

print("Question 7")

while 1 :
	x= int(input("Give your input "))
	if( 1 <= x <= 10) :
		print("The Ans is valid")
		break
	else :
		print("The Ans is not valid")



print("Question 8")
n = int(input("Give your number "))

ans = True
for i in range(2,n):
	if(n%i==0) : 
		ans=0
		break

if(ans) : print("Yes Prime")
else : print("No Prime")


print("Question 9")
items = ["apple", "banana", "orange", "apple", "mango"]

st =set()
ans=1
for it in items :
	if( it in st) :
		ans=0;break #in one line
	st.add(it)
	
if(ans) : print("Has not dulticate")
else : print("Has dulticate")
