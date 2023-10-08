# def hello():
#     print("hello")
#     hello()

# hello()



def number(num=0):
    print(num)
    if num==10:
        return    #break
    number(num+1)

number()


#task
#range(start, end)

#Recursion Function using Range Function


# def number(num=0):
#     print(num)
#     num = range(1,6)
#     for num1 in num:
#         print(num1)
           
# number()


# def person(name,course):
#     print(name,course)
# person("suman", "python")

# * is said to be args for passing multiple parameter in function if astrix is not placed then  we can't bale to pass multiple arguments 
# def person(*name):
#     print(name[0],name[1],name[2])

# person("suman","ram","shyam")

 #kwargs (keywords arguments)

# def person(name,course):
#     print(f"{name} studies {course}")
# person('ram',"django")


#we put ** (double astrix to put keyword argument to pass multiple infinite parameter like  multiple infinite name, age, address..... etc  )
# def person(**kwargs):
#     print(f"{kwargs['name']} studies {kwargs['course']} in {kwargs['institute']}")
# person(name='ram',course="django", institute="mindriser")



#person function args 
# argument name vanne parameter define garnu paryo
#multiple naam rakhera 
#print(my nmae is parametr ma rakheko value)


#kwargs
#person()
#name(first, last)
#age     
#description about hobby
#course

# print(hello my name is <name> and my last name is <name>)
#my age is <age>
#<hobby>
#i am studying<course>

