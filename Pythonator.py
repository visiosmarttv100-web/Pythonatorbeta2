import time
print("Welcome to Pythonator! ");
option = int(input("Please type the number of the option : \n  1 = About the app \n  2 = My contact info \n  3 = Start \n  Your Option Number : " ));

def about():
    text = "Pythonator is a simple calculator written on Python, and it's my second project!"
    for char in text :
        print(char , end='', flush=True)
        time.sleep(.1)
      
def contact():
    text2="Hello! I'm sConfusionR , a beginner student and programmer who want to learn , Did you expect really giving my contact info ...." 
    for char in text2 :
        print(char , end='', flush=True)
        time.sleep(.1)
      
   
def calculator():
    setting = int(input("Type the number of the option : \n 1-Sum \n 2-Product \n 3-Division \n Your Option Number : ")) 
    if setting == 1 :
        num1= float(input("Type the first number"))
        num2= float(input("Type the second number"))
        print(f"The sum of {num1} and {num2} is {num1 + num2}")
    elif setting == 2 :
        num1= float(input("Type the first number"))
        num2= float(input("Type the second number"))
        print(f"The product of {num1} and {num2} is {num1 * num2}")
    elif setting == 3 :
        num1= float(input("Type the first number"))
        num2= float(input("Type the second number"))
        if num2 != 0 :
             print(f"The product of {num1} and {num2} is {num1 / num2}")
        else:
            print("Impossible to divise by 0")    
    else :
        print("Invalid Syntax!")
             

if option == 1 :
    about()
elif option == 2 :
    contact()
elif option == 3:
    calculator()
else:
    print("Invalid Option!")    

 