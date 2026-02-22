print("FINDING MULTIPLICATION TABLE OF A GIVEN NUMBER\n")
num = int(input("Enter a number to print its multiplication table:  "))
for i in range (1, 11):
    res=num*i
    print(i," x ",num , " = ", res)
else:
    print("\nEND OF MULTIPLICATION TABLE")