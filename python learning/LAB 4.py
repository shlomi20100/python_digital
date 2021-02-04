'''
create a list with 4 details about you; name,age,mail and phone number. print that to the screen.
than, create another list with 2 IPs, then add 3 more IPs, pop the 3rd IP and print how many IPs do we have
and print them.
'''

my_list=["shlomi vainblat , 24 , shlomi@mgmail.com , 0528888888"]
print(my_list)
print("...........")
my_list1=["192.168.1.1 , 192.168.1.2"]
print(my_list1)
print("...........")
my_list1.append("192.168.1.3")
my_list1.append("192.168.1.4")
my_list1.append("192.168.1.5")
print(my_list1)
print("...........")
my_list1.pop(2)
print(my_list1)
print("...........")
print("We got IPs : " + str(len(my_list1)))