def iterative_factorial(n):
	result = 1
	for i in range(2, n + 1):
		result *= i
	return result
iter_result = iterative_factorial(5)
print("The factorial of 5 using iteration is:", iter_result)
