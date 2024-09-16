
def f1(s):
	print(s)

l1 = [1, 2, 3, 4, 5, 6]
f1(l1)

# Substring
l2 = l1[1:3]

f1(l2)

l2= l1[:] # craete new list
f1(l2)

l2[0]=1111
f1(l1)
f1(l2)

l2= l1 # point to same address
f1(l2)
f1(l1)

#insert delete , update in short cut
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l3[1:2] =[]

f1(l3) #delete the postion 1

l3[1:1] =[2]

f1(l3) #insert the postion 1

l4 = l3[2 : 5 : 2] #same as string in python
f1(l4)

#insert delete 
l5 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
l5.insert(1, 100,) #insert 100 at postion 1
l5.insert(5, 100) #insert 100 at postion 5

f1(l5)

l5.remove(100) #remove 1st occurance 100 from list
f1(l5)

l5.pop(4) #remove 4th element from list ,  by default it remove last element
f1(l5)

l5.append(200) #append 200 at end of list 
f1(l5)

l5.insert(1, 1999) #insert 1999 at postion 1 , by default it insert at end of list
f1(l5)

# Sort
l6 = [10 , 200 , 40 , 26 , 400 , 100 , 1 ,12 ]  
l6.sort()

f1(l6)

l6 = [10 , 200 , 40 , 26 , 400 , 100 , 1 ,12 ]  
l6.sort(reverse=True)
f1(l6)

ra = [x  for x in range(10)]
f1(ra)

l7 = [0]
l7.extend(ra) #extend the list

f1(l7.count(0)) #count the number of 0 in list

l7.reverse() #reverse the list
f1(l7)

l7.clear() #clear the list

f1(l7)
