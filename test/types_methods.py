class ClassForSomeExample:
	some_class_variable = True

	def __init__(self, a):
		self.a = a 

	def __print(self):
		print(f"{self.a=}")

	def pprint(self):
		print(f"{self.a=}")
		self.cls_print(self)

	@classmethod
	def cls_print(cls, a_obj):
		if not isinstance(a_obj, ClassForSomeExample):
			raise ValueError(f"Expected ClassForSomeExample, but you give {type(a_obj)}")
		print(f"{cls.some_class_variable=}")
		# a_obj.pprint()

	@staticmethod
	def static_print():
		print(f"{ClassForSomeExample.some_class_variable=}")

if __name__ == "__main__":
	a = ClassForSomeExample(3)
	a.pprint()
	# ClassForSomeExample.cls_print(a)