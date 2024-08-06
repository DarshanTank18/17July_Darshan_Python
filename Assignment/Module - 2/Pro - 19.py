# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
input_string = input("Enter string: ")

not_index = input_string.find('not')
poor_index = input_string.find('poor')

if not_index != -1 and poor_index != -1 and not_index < poor_index:
    result_string = input_string[:not_index] + 'good' + input_string[poor_index + 4:]
else:
    result_string = input_string

print("Resulting string:", result_string)