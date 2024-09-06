# Write a Python function to check whether a number is in a given range

def is_in_range(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False

start_range = input("Enter start range : ")
end_range = input("Enter end range : ")
number = input("Enter check no : ")

if is_in_range(number, start_range, end_range):
    print(f"{number} is in the range between {start_range} and {end_range}.")
else:
    print(f"{number} is not in the range between {start_range} and {end_range}.")