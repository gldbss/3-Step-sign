# Try logging in

def Login():                                                            # Here we declared the "Login" function.
    user = input("Enter your account name:\n").lower()
    try:                                                                # Here we are trying to do the following things. If the program could not do it, it will go to except case.
        file = open("asserets/"+user+".txt",'r')
        password = input("Enter Your Password:\n")
        if password in file:
            print("Access Granted")
            file1 = open("asserets/accessstatus.txt",'w')               # Here we opened a existing file only to write similar to line 15.
            file1.write("access granted")
            file1.close()
        else:
            print("Sorry, Wrong password (OR) Wrong Username")
            file1 = open("asserets/accessstatus.txt",'w')
            file1.write("access denied")
            file1.close()
            Login()
    except SyntaxError as msg:                                          # Here we told the program to take any syntax errors and turn in to messages,
        print(msg)                                                      # And here we print them.

Login()
