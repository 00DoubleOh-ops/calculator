def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Please select your function \n" \
      "1. Addition \n" \
      "2. Subtraction \n" \
      "3. Multiplication \n" \
      "4. Division")

select = int(input("Select desired function: "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if select == 1:
    print(num1, "+", num2, "=", 
          add(num1, num2))
elif select == 2:
    print(num1, "-", num2, "=",
          subtract(num1, num2))
elif select == 3:
    print(num1, "*", num2, "=",
          multiply(num1, num2))
elif select == 4:
    print(num1, "/", num2, "=",
          divide(num1, num2))

else:
    print("Invalid input")
    
    