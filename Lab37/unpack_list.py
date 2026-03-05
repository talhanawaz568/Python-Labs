numbers = [1, 2, 3, 4]
print(sum_numbers(*numbers))


data = {'name': 'John', 'age': 25}
print_kwargs(**data)

info = {'occupation': 'Engineer', 'country': 'USA'}
show_info(**info)
