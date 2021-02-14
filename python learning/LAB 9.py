'''
MENU:
1.DOGS DETAILS
2.FRIENDS LIST
3. N AZZERET
'''
from time import sleep
from random import randint

def menu():
    while(True):
        choice=input("Menu:\n----------\n1.Dogs details\n2.Friends list\n3.N AZZERET\n")
        if(choice=="1"):
            dogs()
        elif(choice=="2"):
            friends()
        elif(choice=="3"):
            Azzeret()
        else:
            print("please press 1-3 only!\n")
            continue
        exit=input("Do you wawnt to exit?\nyes/no?")
        if(exit=="yes"):
            break
        else:
            print("Welcome back!\n")
    print("Have a good day!")
def dogs():
    name=input("Enter the dog's name: ")
    age=int(input("Enter the dog's age: "))
    print("The dog's name: " + name + "\nThe dog's age: " + str(age*7) + "\n")

def friends():
    list_friends=[]
    for i in range(5):
        list_friends.append(input("Enter friends names please: "))
    name=input("Enter a new name : " )
    if(name in list_friends):
        print(name + " is inside the list!\n")
    else:
        print(name + " isn't inside the list\n")


def Azzeret():
   num=int(input("Enter a number: "))
   sum=1
   for i in range(1,num+1):
       sum=sum*i
   print(str(num) + " AZZERET is : " + str(sum) + "\n")

menu()