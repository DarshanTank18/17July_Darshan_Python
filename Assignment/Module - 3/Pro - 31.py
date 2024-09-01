# How will you create a dictionary using tuples in python? 

Tup_1 = (101,102,103,104,105)

Tup_2 = ("Darshan","Dharam","Dipesh","Meet","Tirth")

Dic = len(Tup_1)

B = {}
for i in range(Dic):
    B[Tup_1[i]] = Tup_2[i]
print(B)