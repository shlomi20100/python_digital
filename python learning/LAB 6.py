'''
Write a code that will show the menu:
menu:
1. insert number and ** it by 3
2. insert 4 IPs to a list and print it
3. insert 4 entries to dns_dictionary and print it
4. check if a string is polindrom
*if the user wont choose 1-4, you'll tell him to insert 1-4 only!
'''
from time import sleep

choice=input("Menu:\n1. insert number and ** it by 3\n2. insert 4 IPs to a list and print it\n3. insert 4 entries to dns_dictionary and print it\n4. check if a string is polindrom\n")
if(choice=="1"):
    print("Your new number is: " + str((int(input("Enter a Number: ")))**3))
elif(choice=="2"):
    list_ip=[]
    list_ip.append(input("Enter you Ip : "))
    list_ip.append(input("Enter you Ip : "))
    list_ip.append(input("Enter you Ip : "))
    list_ip.append(input("Enter you Ip : "))
    print("Your new list of IP's : " + str(list_ip))
elif(choice=="3"):
    dns_dict={}
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    print("Your DNS dict is: " + str(dns_dict))
elif(choice=="4"):
    word=input("enter a word: ")
    if (word == word[::-1]) :
        print("This is a Polindrom")
    else:
        print("This ain't Polidrom")
else:
    print("Put a number from 1 to 4 only!!")
