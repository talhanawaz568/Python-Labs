def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Alice", age=30, city="New York")

