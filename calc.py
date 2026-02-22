a=int(input("Enter a num1: "))
b=int(input("Enter num2: "))
print("Select OPERATION BELOW:\n")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice (1-4):  "))
if (choice == 1):
    res=a+b
    print ("ADDITION:\t", res)
elif (choice == 2):
    res=a-b
    print ("SUBTRACTION:\t", res)

elif (choice == 3):
    res=a*b
    print ("MULTIPLICATION:\t", res)

elif (choice == 4):
    if (b == 0):
        print("ERROR: Division by zero")
    else:
        res = a/b
        print("DIVISION:\t", res)
else :
    {
        print("INVALID CHOICE")
    }

