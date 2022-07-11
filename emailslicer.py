
def emailSlicer(email):
    name = ''
    domain = ''
    flag = True
    for letter in email:
        
        if letter !="@" and flag:
            name = name + letter
            
        elif (letter == "@"):
                flag = False
        else:
            domain = domain + letter

    return (f"your user is {name},and you have account in {domain}")

email = input("please enter your email: ")
print(emailSlicer(email))
            
            
            
            
    
