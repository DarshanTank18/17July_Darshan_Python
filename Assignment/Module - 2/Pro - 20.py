# Write a Python function that takes a list of words and returns the length of the longest one.
words_list = ["darshan", "pradip", "dipesh", "dharam"]

if len(words_list) > 0:
    for word in words_list:
        if len(word) > max_length:
            max_length = len(word)

print("The length of the longest word is:", max_length)
