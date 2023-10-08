#Recursion Function using Range Function
#=======================================

# def range(start=0, end=0):
#     print(start)
#     if start==end:
#         return
#     range(start +1,end)
           
# range( start =100, end=102)     #IMPORTANT

#======================================================================

#args function task
#puts multiple name
#print(my name is <value @ parameter>)
#=======================================


# def person(*name):
#     print(f"My Name is {name[0]} ,{name[1]} ,{name[2]} ,{name[3]} ,{name[4]} ,{name[5]}")

# person("suman","ram","shyam","hari","krishna","binod")


# def person(*name):
#     for name1 in name:
#         print(f"My name is {name1}")

# person("suman", "ram", "hari", "shyam","krishna","binod")


#=========================================================================================================

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
#===============================================================================================================

# def person(**kwargs):
#     print(f"""Hello My Name is {kwargs['first_name']} {kwargs['last_name']}
#           And My age is {kwargs['age']} 
#           And My hobby is {kwargs['hobby']}
#           And I am Studying {kwargs['course']} """)

# person(first_name='Suman',last_name ='Ranjit',age="30",hobby="watching netflix", course="Python django")
