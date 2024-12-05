

# Generators are a simpler way to create iterators.
# They use the yield keyword to produce a series of values lazily, 
# which means they generate values on the fly and do not store them in memory.

def squre(n):
	for i in range(1,n+1):
		yield i**2

numbers=squre(5)
for i in numbers:
	print(i)


def large_file_read(file_path):
	with open(file_path,'r') as file:
		for line in file:
			yield line


files=r"08iterators&generators\text.txt"
file_lines=large_file_read(files)

for line in file_lines:
	print(line.strip())