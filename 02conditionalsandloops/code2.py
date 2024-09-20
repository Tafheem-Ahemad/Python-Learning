
print("Qustion 4")
color = str(input("The color of your fruit "))

if color == "green":
	print("Unripe")
elif color == "Yellow":
	print("Ripe")
elif color == "Brown":
	print("Overripe")
else : print("Color not found")


print("Qustion 5")
password = str(input("Give Your PassWord "))
count=0
for i in password :
	if('a' <= i <= 'z' or 'A' <= i <= 'Z') :  count+=1

strengh ="weak"
if count > 10 : strengh = "strong"
elif count >=6 : strengh = "mediun"

print(f"Your Password is {strengh}")

print("Qustion 6")
year = int(input("Take your input Year "))

if year%400 == 0 :
	print("Leap Year")
else :
	if(year %4 ==0  and year%100) : print("Leap Year")
	else : print("Leap Year")