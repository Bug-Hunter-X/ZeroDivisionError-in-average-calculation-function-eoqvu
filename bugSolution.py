def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage (will now return 0)
average = calculate_average([]) 
print(average) # Output: 0

#Example with numbers
 numbers = [10,20,30,40,50]
average = calculate_average(numbers)
print(average) # Output: 30.0