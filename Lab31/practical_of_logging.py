import logging

def divide_numbers(a, b):
    try:
        result = a / b
        logging.info("Division successful.")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero error.")
        return None

result = divide_numbers(10, 0)
