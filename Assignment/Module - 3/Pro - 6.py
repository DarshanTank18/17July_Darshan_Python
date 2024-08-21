# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
strings = ["abc", "xyz", "aba", "1221", "a", "xyx", "abba"]
count = 0

for i in strings:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1

print(f"Number of matching strings: {count}")
