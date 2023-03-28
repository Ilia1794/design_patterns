"""[summary]

Адаптер — это один из структурных паттернов, из названия которого исходит его и назначения. 
По сути это типичный переходник для разных интерфейсов или данных.
1. Адаптер имеет интерфейс, который совместим с одним из объектов.
2. Поэтому этот объект может свободно вызывать методы адаптера.
3. Адаптер получает эти вызовы и перенаправляет их второму объекту, 
	но уже в том формате и последовательности, которые понятны второму объекту.

[description]
"""
from math import sqrt


class Holle:
	def __init__(self, r):
		self.r = r 
	
	def put(self, obj):
		try:
			if self.r>= obj.r:
				print(f"Ok")
			else:
				print(f"Radius {obj.__name__} is big")
		except AttributeError:
			print(f"{obj.__name__} has not attribute r")


class Square:
	def __init__(self, x, h):
		self.x = x
		self.h = h

	def __name__(self):
		return "Square"
	
	def __add__(self, val):
		return Square(self.x, self.h+val.h)

	def __lt__(self, val):
		return self.h*self.x**2< val.h*val.x**2

	def __le__(self, val):
		return self.h*self.x**2 <= val.h*val.x**2


class SquareHoleAdapter:
	def __init__(self, obj: Square):
		self.sq_obj = obj 

	@property
	def r(self) -> float:

		return sqrt(2*(self.sq_obj.x**2))/2

	def __name__(self):
		return self.sq_obj.__name__



class TestProperty:
	def __init__(self, a):
		self.a = a 
		self.__r = 0 


	@property
	def r(self):
		return float(self.__r)

	@r.setter
	def r(self, val):
		if isinstance(val, (int, float)):
			self.__r = val + self.a
		else:
			self.__r = 0

	


if __name__ == "__main__":
	# c = Holle(2)
	s = Square(3, 5)
	s1 = Square(3, 4)
	print(s==s1)
	# s_a = SquareHoleAdapter(s)
	# c.put(s_a)
	# 
	t = TestProperty(3)
	print(t.r)
	t.r = 15
	print(t.r)
	t.r = [1,5]
	print(t.r)