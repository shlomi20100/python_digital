print("Now we will calculate your marketing list...\nPrices :\n.........\nCola=5 NIS\nTomatoes=3 NIS\nCucumber=2 NIS\nChicken=20 NIS")
print("........")
Tomatoes=int(input("how many Tomatoes do you want? "))

Cucumber=int(input("how many Cucumber do you want? "))

Chicken=int(input("how many Chicken do you want? "))

Cola=int(input("how many Cola do you want? "))

print("\nSummry of your order: \n.............\nTomatoes: " + str(Tomatoes) + "\nCucumber: " + str(Cucumber) + "\nChicken: " + str(Chicken) + "\nCola: " +str(Cola))
#The longest way to calculate the summary of the list:
#sum1=Tomatoes*3
#sum2=Cucumber*2
#sum3=Cola*5
#sum4=Chicken*20

#the fast way to callculate the summary
summary=(Tomatoes*3)+(Cucumber*2)+(Cola*5)+(Chicken*20)
print("\nyou have yo pay: " +str(summary) + " NIS without tax")
#print("\nyou have yo pay: " +str(summary*1.17) + " NIS with tax") - it'll show more than 2 digits after the int
print("\nyou have yo pay: " +str("%.2f" %(summary*1.17)) + " NIS with tax")
