class Singleton:
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton,cls).__new__(cls)
		return cls.instance

class Borg:
   __shared_state = {"1": "2"}
   def __init__(self):
      self.x = 1
      self.__dict__ = self.__shared_state


class A:
	def __init__(self):
		self.a = 1 
		self.b = "234"
		self.c = False 
		self.d = []


if __name__=="__main__":
	s = Singleton()
	print(s)
	s1 = Singleton()
	print(s1)
	b = Borg()
	b1 = Borg()
	b.x = 4
	print("Borg Object 'b': ", b) ## b and b1 are distinct objects
	print("Borg Object 'b1': ", b1)
	print("Object State 'b':", b.__dict__)## b and b1 share same state
	print("Object State 'b1':", b1.__dict__)
	print(f"{b1.x=}")
	a = A()
	print(f"{a.__dict__}")