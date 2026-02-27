coordinates = (10, 20, 30)
print("Coordinates Tuple:", coordinates)


try:
	coordinates[0] = 100
except TypeError as e:
	print("Error:", e)
