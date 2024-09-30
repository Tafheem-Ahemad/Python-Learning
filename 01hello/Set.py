# Set  --> All the elements are unique
# Set is mutable
# Impoertant --> Set is unordered


# Different type of set creation
# Empty set
st = set()
print(st)

# set with list
st = set([10,20,30,40,50])
print(st)

# set with tuple
st = set((10,20,30,40,50))
print(st)	

# set with string
st = set("Hello")
print(st)

st ={10 , 20 , 30 , 40 , 50}
print(st)	

st ={10 , 20 , 30 , 40 , 50,100,200,300,400,500,10,20,30,40,50}
print(st)	


# All Inbuild functions of set
# add , remove , discard , clear , union , update , intersection , intersection_update , isdisjoint , issubset , issuperset


# Add element in set
st ={10 , 20 , 30 , 40 , 50}
st.add(60)
print(st)

# Remove element from set
st ={10 , 20 , 30 , 40 , 50}
st.remove(30) #remove the element if present
# st.remove(300) # it gives error if element is not present
print(st)

# Remove element from set
st ={10 , 20 , 30 , 40 , 50}
st.discard(200) #remove the element if present
print(st)

# Clear all the elements from set
st ={10 , 20 , 30 , 40 , 50}
st.clear()
print(st)

# union of two sets
st1 = {10,20,30,40,50}
st2 = {60,70,80,90,100}
st3 = st1.union(st2)
print(st3)

st1.update(st2) # it will update the set1 with set2
print(st1)


# Intersection of two sets
st1 = {10,20,30,40,50}
st2 = {30,40,50,60,70}
st3 = st1.intersection(st2)

print(st3)

st2.intersection_update(st1)
print(st2)


# set member 
st={10,20 , 30,40,50, 100,200,300,400,500 ,152,126,145,}
print(10 in st)
print(30 in st)

# isdisjoint() --> Return True if two sets have a null intersection
st1 = {10,20,30,40,50}
st2 = {60,70,80,90,100}
print(st1.isdisjoint(st2))
print(st1.isdisjoint(st1))

#  is subset --> Return True if all elements of set1 are present in set2
st1 = {10,20,30,40,50}
st2 = {10,20,30,40,50,60,70,80,90,100}
print(st1.issubset(st2))
print(st2.issubset(st1))

#  is superset --> Return True if all elements of set2 are present in set1
st1 = {10,20,30,40,50}
st2 = {10,20,30,40,50,60,70,80,90,100}
print(st1.issuperset(st2))
print(st2.issuperset(st1))

# conting unique words in string
s = "Hello how are you"
st = set(s.split())
print(st)

