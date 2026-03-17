#!/bin/bash

# Prompt for the first number
echo "Enter the first number:"
read num1

# Prompt for the second number
echo "Enter the second number:"
read num2

sum=$((num1 + num2))
echo "The sum is : $sum"

# Subtraction
difference=$((num1 - num2))
echo "The difference is: $difference"

# Multiplication
product=$((num1 * num2))
echo "The product is: $product"

# Division
if [ $num2 -ne 0 ]; then
    quotient=$((num1 / num2))
    echo "The quotient is: $quotient"
else
    echo "Division by zero is not allowed."
fi

