def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    if num2==0:
         return "Cannot divide by zero"
    return num1/num2


#main
while True:
 print("OPTIONS")
 print("1. ADD(+)")
 print("2. UBTRACT(-)")
 print("3. MULTIPLY(*)")
 print("4. DIVIDE(/)")
 print("5. EXIT")
 inp= int(input(" :"))
 if inp==5:
     break
 elif inp>=1 and inp<=4 :
     num1 = float(input("Enter first number: "))
     num2 = float(input("Enter second number: "))

     if inp == 1:
            print("Result:", add(num1, num2))
     elif inp == 2:
            print("Result:", subtract(num1, num2))
     elif inp == 3:
            print("Result:", multiply(num1, num2))
     elif inp == 4:
            print("Result:", divide(num1, num2))
 else:
        print("Invalid input")
