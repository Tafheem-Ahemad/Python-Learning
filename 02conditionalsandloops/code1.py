print("qsn 1")

num = int(input("Age "))

# Write in single line
if num < 13: print("Child")
elif 13 <= num <= 19 : print("Teenager")
elif 20 <= num < 60 : print("Adult")
else : print("Senior")

# Here tab means a {}

print("qsn 2")

age = int(input("Your age "))
day = str(input("The day "))
discount = 0

if day == "wed" : discount=2

#using the format in print
if age >= 18 : print(f"price to be pay {12-discount}")
else : print(f"price to be pay {8-discount}")


print("qsn 3")

mark = int(input("Write your mark "))

if mark <= 90:
	print("Excellent")
elif mark <= 80 :
	print("Good")
elif mark <= 70 :
	print("Average")
elif mark <= 60 :
	print("Decent")
else : print("Fail")

print("qsn 4")