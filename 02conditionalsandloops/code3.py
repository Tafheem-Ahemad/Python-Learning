print("Question 1")

n = int(input())
li =list(range(n))

for i in li:
	li[i] = int(input())

positive_count=0

for i in li:
	if(i>0) : positive_count+=1

print(f"The number of positive number {positive_count}")


print("Question 2")

n = int(input())


even_sum=0

for i in range(1,n+1):
	if(i%2==0) : even_sum+=i

print(f"The even sum is {even_sum}")


print("Question 3")
n = int(input())

for i in range(1,11):
	if(i==5) : continue
	print(i*n)