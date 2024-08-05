a = int(input("Enter mark :"))
b = int(input("Enter mark :"))
c = int(input("Enter mark :"))
d = int(input("Enter mark :"))

sum = a + b + c + d
print("sum = ",sum)

pr = sum / 4
print("pr = ",pr)

if a > 33 and b > 33 and c > 33 and d > 33 :
    if pr < 80 :
        print("A")

    elif pr < 70 :
        print("B")

    elif pr < 60 :
        print("C")
    
    elif pr < 50 :
        print("D")

    elif pr < 40 :
        print("E")

    else :
        print("fail")

else :
    print("Fail")