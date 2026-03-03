def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@log_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Call the function to see the decorator in action
say_hello("Alice")
