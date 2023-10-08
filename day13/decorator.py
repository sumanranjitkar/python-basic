# def star(func):
#     def wrapper():
#         print('*'*10)

#         func()
#         print('*'*10)
#     return wrapper
# @star
# def name():
#     print("hello")
# @star
# def age():
#     print("age")

# name()
# age()


#TASK
# #############
#*************
#name
# #############
#*************

def star(func):
    def wrapper():
        
        print('*'*10)
        func()
        print('*'*10)
        
    return wrapper
def hash(func1):
        def wrapper1():
            print('#'*10)
            func1()
            print('#'*10)
        return wrapper1
# @star
# @hash
def name():
    print("name")


# @star
def age():
    print("age")

# name()
# print()
# age()

star(hash(name))()
# star(hash(name()))