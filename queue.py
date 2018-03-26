
print("PERFORM QUEUE OPERATIONS")
print("===========================")
print("1 : Add item to list")
print("2 :Delete item from list")
p=input("Enter your choice")
p=int(p)
if  p==1:
	class queue:
		def __init__(self):
			self.q=[ ]
		def isEmpty(self):
			return (len(self.q)==0)
		def enqueue(self,item):
			return self.q.append(item)
	fruit=queue()
	a=input("Enter the number of items to be added to the list")
	a=int(a)
	i=0
	while i<=a:
		b=input("Read the item :")
		fruit.enqueue(b)
		
		print(fruit.q)
		
elif p==2:
	class queue:
		def __init__(self):
			self.q=[ ]
		def isEmpty(self):
			return (len(self.q)==0)
		def dequeue(self):
			return self.q.pop(0)
		def enqueue(self,item):
			return self.q.append(item)
	fruit=queue()
	a=input("Enter the number of items to be added to the list")
	a=int(a)
	i=0
	while i<=a:
		b=input("Read the item :")
		fruit.enqueue(b)
		
		print(fruit.q)
	c=fruit.isEmpty()
	if c==0:
		fruit.dequeue()
		print(fruit.q)
	else:
		print("No item to be removed")
else:
	print("Invalid")

