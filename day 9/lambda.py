#lambdaFunction
#this program shows the triple(cube) of value 
def myFunc(n):
    return lambda a:a*n

Tripler =myFunc(3)
print(Tripler(3))

