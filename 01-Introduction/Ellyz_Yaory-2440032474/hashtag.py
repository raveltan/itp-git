while True:
	height = int(input("Height: "))
	if height >=1 or height <= 8:
		break

#left side
for i in range(height):
	for j in range(height):
		if j < height - 1 - i:
			print(" ", end = "")
		else:
			print("#", end = "")
	print(end = " ")

#right side
	for j in range(height):
		if height - i < j + 2:
			print("#", end = "")
			print(end = "")
	print()
