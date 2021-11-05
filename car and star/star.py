def square(width,height):


	print(width * "*")
	for x in range(height-2):
		print("*"+(width - 2) * " " + "*")
	print(width * "*")

square(10,3)
square(5,4)