# Implement a Timer Decorator
# Objective: Write a decorator `timer` that measures the execution time of any function it decorates.
# Parameters:
# - None directly; it decorates functions.
# Returns:
# - Wrapper function that prints the execution time.
# Details:
# - Use the `time` module to calculate the execution time.
# - Print the time in seconds.

import time
def timer(func):
	def wrapper(*args, **kwargs):
		start_time = time.time()  # Record the start time
		result = func(*args, **kwargs)  # Call the function
		end_time = time.time()  # Record the end time
		execution_time = end_time - start_time  # Calculate the execution time
		print(f"Function `{func.__name__}` took {execution_time:.3f} seconds")
		return result

	return wrapper

# Desired Outcome:
@timer
def some_heavy_computation():
#     # Arbitrary computation that takes time, e.g., a loop or sleep
 time.sleep(2)
some_heavy_computation()  # Expected to print: Function `some_heavy_computation` took X.XXX seconds

