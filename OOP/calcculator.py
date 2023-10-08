def add(a,b):
   return(a+b)

def sub(a,b):
   return(a-b)

def multiply(a,b):
   return(a*b)

def divide(a,b):
   return(a/b)
 


def calculator():
    while True:
        print('\n Selection the following Operation:')
        print(' 1 for ADDITION')
        print(' 2 for SUBTRACT')
        print(' 3 for MULTIPLY')
        print(' 4 for DIVISION')
        print(' 0 for EXIT')

        choice = input(' Enter your Choice : (0,1,2,3,4): ')

        if choice=='0':
            print(" The Program is Terminated !!")
            break
        
        if choice in ['1','2','3','4']:
            first_num = float(input('enter the first number: '))
            second_num = float(input('enter the second number: '))

            if choice == '1':
             result= add(first_num,second_num)
             print(f'The result of Addition is : {result}')
            elif choice == '2':
               result = sub(first_num,second_num)
               print(f'The result of Subtraction is : {result}')
            elif choice == '3':
               result = multiply(first_num,second_num)
               print(f'The result of Multiplication is : {result}')
            elif choice == '4':
               result = divide(first_num,second_num)
               print(f'The result of Division is : {result}')
        
            
        else:
           print(" 'Invalid Choices/ please select again' ")
           

calculator()
