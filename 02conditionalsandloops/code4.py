print("Question 4")

s = str(input("Enter your string "))

rev=""

for i in s :
	rev=i+rev

print(rev)

print("Question 5")

li = [1 , 10 , 10 ,40 ,50 , 1 , 50 , 50 , 10, 20 , 15 , 14]
map = {}
for i in li:
	map[i] = map.get(i,0)+1

for i in li :
	if map[i] == 1 : 
		print(i)
		break