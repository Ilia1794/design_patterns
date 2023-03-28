def dekor(debug):
	def dekor_(func):
		def wrapper(*args, **kwargs):
			if debug:
				print("In Decorator")
			return func(*args, **kwargs)
		return wrapper
	return dekor_

@dekor(True)
def func(a):
	return f"Arg os {a}"


if __name__ == "__main__":
	# dekor(True)(func)(10)
	print(func(10))