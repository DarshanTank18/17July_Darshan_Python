# Write a Python function to get the largest number, smallest num and sum of all from a list.
def abc(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    total = sum(numbers)
    return largest,smallest,total

numbers = [5, 10, 15, 20, 25]
largest, smallest, total = abc(numbers)

print(f"Largest number : {largest}")
print(f"Smallest number : {smallest}")
print(f"Total : {total}")