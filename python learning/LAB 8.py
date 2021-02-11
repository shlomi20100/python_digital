'''
menu:
1.printing 100 numbers
2.checking fibo
3.randit numbers until we get 12 or we count 10 times
'''
from time import sleep
from random import randint

while(True):
    choice=input("Menu: \n------------------\n1 .printing 100 numbers\n2 .checking fibo\n3 .randit numbers until we get 12 or we count 10 times\n")
#1
    if(choice=="1"):
        for i in range(1,101):
            print(i)
#2
    elif(choice=="2"):
        #fibo=[1, 2, 3, 5, 8, 13, 21]
        fibo=[]
        for i in range(7):
            fibo.append(int(input("Enter a number: ")))
        boolean = "True"
        for i in range(2, len(fibo)):
            print(fibo[i])
            print(fibo[i - 1])
            print(fibo[i - 2])
            print("\n")
            if fibo[i] != (fibo[i - 1] + fibo[i - 2]):
                boolean = "False"
                break
            if boolean == "True":
                print("It's fibo series")
            else:
                print("It isn't fibo series")
#3
    elif(choice=="3"):
        counter = 1
        num=randint(1,12)
        while(num!=12 and counter<11):
            print("Counter" + str(counter) + " Number: " + str(num) + "\n")
            counter=counter+1
            num=randint(1,12)
        else:
            print("Enter 1-3 only please!\n")
            continue
        exit=input("Do you want to exit? yes/no\n")
        if(exit=="yes"):
            print("Thank you and have a good day!\n")
            break


