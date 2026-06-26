num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


choice = input("Enter your choice")

if choice == "1":
    addition = num1 + num2
    print("Addition",addition)
    
elif choice == "2":
    subtraction = num1 - num2
    print("Subtraction",subtraction)

elif choice == "3":
    multiplication = num1 * num2
    print("Multiplication",multiplication)
    
elif choice == "4":
    division = num1 / num2
    print("Division",division)

else:
    print("Invalid operator")



                 
