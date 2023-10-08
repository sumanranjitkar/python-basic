#python scope
#=======================


#local scope
# def number():
#     x=10 #variable initialize within function 
#     print(x)
# number()



#global scope
# x=10
# def number():
#     x=11
#     print(f"Local Scope  inside function {x}") #local scope

# number()
# print(f"Global Scope  outside function {x}") #global scope


# x=10
# def number():
#     global x #global scope lai override garera local scope print garna ko lagi by which results will be x=11
#     x=11
#     print(f"Local Scope  inside function {x}") #local scope

# number()
# print(f"Global Scope  outside function {x}") #global scope


#Task
#is_Login variable which is global variable
#function login with 2 parameter
#username and password
#is login variable true or false
#if both matches print true else false

is_Login=False
def login(user_name, password):
    global is_Login
    # user_name=="suman"
    # password=="1234"

    if user_name=="suman" and  password =="1234":
        is_Login=True
        print("username and password match")
    else:
        is_login = False
        print("invalid user_name and password")

login('suman','1234')



        











