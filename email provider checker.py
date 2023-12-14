#Getting the email address from the user
while True:
    email=input("enter your email address")
    if"@gmail.com"in email:
        print("you are using google ")
    elif"@yahoo.com"in email:
        print("you are using yahoo")
    elif"@outlook.com"in email:
        print("you are using outlook")
    elif"@proton.com"in email:
        print("you are using proton")
    elif"@zoho.com"in email:
        print("you are using zoho")
    elif"@fast.com"in email:
        print("you are using fast")
    elif"@mail.com"in email:
        print("you are using apple mail")
    else:
        print("invalid email format")