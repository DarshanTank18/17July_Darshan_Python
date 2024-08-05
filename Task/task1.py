name = input("Enter name : ")
if name.isalpha() :
    print("---> ok")
    age = input("Enter Age : ")
    if age.isdigit() :
        print("---> ok")
        number = input("Enter mobile number : ")
        if len(number) == 10 :
            if number.isdigit():
                print("---> ok")
                email = input("Enetr email : ")
                if email.casefold() :
                    print("---> ok")
                else :
                    print("Enter only small latters")
            else :
                print("Enter only number")
        else :
            print("Enter 10 digit number")
    else :
        print("Enter only number")
else :
    print("Enter only characters")