num=int(input("enter a number with 4 digits: "))
'''
Thousands=4
Hundreds=5
Dozens=6
ahadot=7
'''

#this is Thousands
print("Thousands=" + str(num//1000))

#this is Hundreds
print("Hundreds=" +str((num%1000)//100))

#this is Dozens
print("Dozens=" +str((num%100)//10))

#this is unity
print("unity=" +str(num%10))