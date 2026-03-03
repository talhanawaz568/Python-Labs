class Mycontext:
	def __enter__(self):
		print("Entering the context and allocating resources.")
		return self
	def __exit__(self, exc_type, exc_value, traceback):
		print("Existing the context and calculating up resources.")

with Mycontext() as context:
	print("Running within the context block.")
