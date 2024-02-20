a = "    .....PrzyKladowy .Text"
print(a)
print(a.strip(" ."))
# Need to specify combiantion of chars, not just "." if there is space at start type " ."
changed = a.replace(".", ",", 1)
print(changed)

email = input("Wpisz swój e-mail")
changedemail = email.strip().lower()
# Delete whitespaces and set to lower case
if(changedemail.count('@') <= 1):
    print(changedemail)
elif(changedemail.count('@') >=2):
    print("Wrong format address type only one @")
else:
    print("Wrong address")

