def sum_numbers(*args):
    return sum(args)

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def show_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} is {v}")

# Now your existing code will work
numbers = [1, 2, 3, 4]
print(sum_numbers(*numbers))
