from time import sleep
from random import randint

print("Welcome to our CUBE game\nEach turn cost you 3 ILS\n----------------\n")
money=int(input("Please enter how much money do you have?\n"))
tunrs=money//3
print("You have : " +str(tunrs) + " turns\nYour change is : " + str(money%3) + " ILS\nEnjoy!\n--------")
prize=0
for i in range(tunrs):
    print("Round number " + str(i+1) + " :")
    sleep(3)
    cube1=randint(1,6)
    cube2=randint(1,6)
    print("Cube 1 : " + str(cube1) +"\n" + "Cube 2 : " + str(cube2))
    if(cube1 == cube2):
        if(cube1 == 6):
            prize=prize +1000
        else:
            prize=prize +100
    elif(cube1==1):
        prize=prize + 20
    elif(cube2==2):
        prize=prize + 40
print("-------------\n")
print("Calculating your prize")
sleep(3)
print("\nYour prize: " + str(prize) + " ILS\n")