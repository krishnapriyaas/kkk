class Queue:
	def __init__(self, elements):
		self.queue = elements
	def displayQueue(self):
		print('Elements in Queue :')
		for element in self.queue:
			print(element)
	def remove(self):
		if len(self.queue) != 0:
			print("Deleted elememt is ", self.queue[0])
			self.queue.pop(0)
		else:
			print("Queue is empty")
	def enter(self, element):
		self.queue.append(element)
elementList = input('Enter queue elements seperated by comas: ').split(',')
elements = []
for element in elementList:
	elements.append(int(element))
print(elements)
queue = Queue(elements)
while(True):
	print("Menu\n====\n1.Print Queue\n2.Serve Queue\n3.Enter Queue\n4.Exit")
	option = input('Enter your choice: ')
	if option == '1':
		queue.displayQueue()
	elif option == '2':
		queue.remove()
	elif option == '3':
		element = input('Enter an element.')
		queue.enter(element)
	else:
		break

