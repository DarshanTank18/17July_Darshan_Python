f = open("ex.txt", "r")
content = f.read()
count = "Hellooooooooooo"
count = content.count(count)
print(f"The word '{count}' appears {count} times in the file.")
f.close()