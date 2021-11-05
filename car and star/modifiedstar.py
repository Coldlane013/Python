def square(width,height):
	print("Enter text or number here:")
	user_input = input("")
	print(width * user_input)
	for x in range(height-2):
		print(user_input+(width - 2) * " " + user_input)
	print(width * user_input)

square(10,3)
square(5,4)