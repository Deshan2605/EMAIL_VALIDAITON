email=input("Enter your email: ")
k=0
j=0
d=0

if len(email)>=6:
    if email[0].isalpha(): #  Your email should start with an alphabet
        if ("@" in email) and (email.count("@")==1): # only 1 @ should be present in email
            if (email[-4]==".") ^ (email[-3]=="."): # ^ (X-OR OPERATOR): it means that either of the conditions will be true at a time, both cannot be true at the same time. jdkjn2gmail.com = [-4] or dschbhd@gmail.in = [-3]
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper(): # upper() will convert lower case to upper case w-->W
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="@" or i==".":
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                    print("NOT A VALID EMAIL. Your email cannot have space/uppercase in between.") # 5th position
                else:
                    print("VALID EMAIL.")
            else:
                print("NOT A VALID EMAIL. You should have a period in your email. For example: jdkjn2gmail.com or dschbhd@gmail.in " ) # 4th position
        else:
            print("NOT A VALID EMAIL. Your email should have one '@' character in it.") # 3rd position

    else:
        print("NOT A VALID EMAIL. Your email should start with an alphabet.") # 2nd position
else:
    print("NOT A VALID EMAIL. Your email should have atleast 6 characters.") # 1st position