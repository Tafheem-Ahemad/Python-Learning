# Multiple Interitence

class a:
	def into(self):
		return "I This First Class"
	
class b:
	def into(self):
		return "I This Second Class"
	

class c(b,a):  # b is fisrt , so b is search first
	def intoduction(self):
		return "I This Third Class"
	
x= c()
print(x.intoduction())
print(x.into())
