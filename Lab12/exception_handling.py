user_input = input("Enter a number: ")
try:
	number = int(user_input)
	print(f"The number is {number}.")
except ValueError as ve:
	    print("Error: Input is not a valid number. Please enter an integer.")

