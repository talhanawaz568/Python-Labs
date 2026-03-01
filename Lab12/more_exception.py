user_input = input("Enter a number: ")
try:
	result = 10 /int(user_input)
	print(f"Result is: {result}")
except ValueError:
	print("Error: Please enter numeric values!")
except ZeroDivisionError:
        print("Error: Division by zero is undefined!")
