# Write a Python script to check if a given key already exists in a dictionary. 
a = {'name': 'Darshan', 'age': 22, 'city': 'Rajkot'}

b = 'age'

print(a)

if b in a:
    print(f"The key '{b}' exists in the dictionary.")
else:
    print(f"The key '{b}' does not exist in the dictionary.")
