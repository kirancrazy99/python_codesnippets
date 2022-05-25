secretpassword='kiran'
count_limit=3
count=0

while count<count_limit:
    print("Please enter the secretpassword")
    password=input()
    if password==secretpassword:
        print("password accepted")
        break
    else:
        print("please try again")
    count+=1

else:
    print("3 attempts failed")