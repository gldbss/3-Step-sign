# Generate the Username & Password

import random as rdm                                                        # We are going to link "random" module to this script as "rdm"

def Generator():                                                            # We are doing to declare "Generator" function
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    numbers = "1234567890"
    symbols = "!@#$%^&()_-+={[]};',."
    pass_len = 12
    user_len = 7
    password = "".join(rdm.sample(lower+upper+symbols+numbers,pass_len))    # We have took random samples from lower,upper,symbols,numbers and set the max lenth as per pass_len
    user = input("Enter Your Name:\n").lower()                              # Here,"Enter Your Name:" will be printed and input is taken from the next line
    username = "".join(rdm.sample(user+numbers,user_len))                   # Same as password but took just user and numbers
    print("Your Username:"+username+"\nYour Password:"+password)
    file = open("asserets/"+user+".txt","w+")                               # Here we create a file to store username and password
    file.write(username+"\n"+password)                                      # Here we stored the username and password in the file
    file.close()                                                            # Here we closed the file

Generator()                                                                 # We called the function "Generator"
