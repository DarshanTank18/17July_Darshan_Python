# Q16. Write a Python program to check whether a list contains a sub list


d_list = [1,2,5,['Darshan','1'],8,]



for i in d_list:
    if type(i) == list:
        print("Yes, the list contains a sublist.")
        break
else :
    print("No, the list does not contain a sublist.")