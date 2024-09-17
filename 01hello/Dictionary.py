
def f1(s ):
	print(s)

dic =dict()

dic.setdefault('name', 'Ahemad')
print(dic)
dic = {
	'name': 'Tom',
	'age': 20,
	'class': 'CS',
	'roll': 101
	}


print(dic)

f1(dic['name'])

f1(dic.get('age' , 'Not Found')) #get value of key if not found return 'Not Found'
f1(dic.get('ages' , 'Not Found')) #get value of key if not found return 'Not Found'

for key , val in dic.items():
	print(key , val)

if 'age' in dic:
	print(dic['age'])

dic.pop('age') #remove any key
f1(dic)

dic['marks'] = 100 #add new key
f1(dic)


dic2 = {a : a**2 for a in range(10)}
f1(dic2)

dic2.clear()
f1(dic2)

