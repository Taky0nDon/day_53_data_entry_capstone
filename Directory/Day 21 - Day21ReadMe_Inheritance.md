D A Y T W E N T Y O N E

class inheritance

class Fish(ClassFishInheritsFrom):
	def __init__(self):
		super().__init__()  # super() initializes everything the super class can do inside Fish, turning ClassFishInheritsFrom into a superclass
		
class Animal:
	def __init__(self):
		self.num_eyes = 2
		
	def breathe(self):
		print("Inhale, exhale.")
		
class Fish(Animal):
	def __init__(self):
		super().__init__()  # Fish inherits from Animal all the attributes and methods of Animal
		
	def breathe(self):  # Fish breathes differently from land animals. modifying inherited method
		super().breathe  # everything the superclass method does
		print("doing this underwater")  # only the Fish class implementation of breathe will do this

	def swim(self):
		print("moving in water")
		

nemo = Fish()
nemo.swim()
nemo.breathe()  # method inherited from Animal superclass
print(nemo.num_eyes)