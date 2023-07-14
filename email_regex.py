import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$" # ^ - means start; ? - means that whatever input you are giving should be used only once; \w - means to search something; {} - used for searching in the given indexes; $ - used when your are searching from behind
user_email=input('Enter your email: ')

if re.search(email_condition,user_email):
    print("VALID EMAIL")
else:
    print("NOT A VALID EMAIL")