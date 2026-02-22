name=input("Enter your name :    ")
m1=int(input("Enter your Maths mark (for 100)     :  "))
m2=int(input("Enter your Physics mark (for 100)   :  "))
m3=int(input("Enter your Chemistry mark (for 100) :  "))
print("Total Marks obtained  :\t", m1+m2+m3)
c=float((m1+m1+m3)/3)
avg = round(c,2)
print("Average MArk  :    \n",avg)
if(avg>89 and avg<=100):
    print(name,"obtained GRADE A")
elif(avg>69 and avg<=89):
    print(name,"Obtained GRADE B")
elif(avg>49 and avg<=69):
    print(name,"Obtained GRADE B")
else:
    print(name,"Obtained FAILED Mark ")
    



