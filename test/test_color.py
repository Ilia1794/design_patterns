from colour import Color


if __name__ == "__main__":
	base_color = Color("#ff0000")
	end_color = Color("#0000ff")
	print([_.get_hex() for _ in base_color.range_to(end_color, 10)])