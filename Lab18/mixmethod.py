def tail_recursive_factorial(n, accumulator=1):
    if n <= 1:
        return accumulator
    else:
        return tail_recursive_factorial(n - 1, n * accumulator)

# Example usage
tail_result = tail_recursive_factorial(5)
print("The factorial of 5 using tail recursion is:", tail_result)
