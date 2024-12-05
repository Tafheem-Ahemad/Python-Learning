
# Iterator is an object that contains a countable number of values.
# It is an object that can be iterated upon, meaning that you can traverse through all the values.
# It lazy loading of the values and it is not stored in memory.

li=[10,20,30,40]

iterator=iter(li)
for i in iterator:
	print(i)

# After iterator at the end of the block

iterator=iter(li)

try:
	while(True):
		print(next(iterator))
except StopIteration:
	print("The list is end")
		

import itertools
# It has good inbluid iterater