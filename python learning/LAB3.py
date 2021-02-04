'''create 2 variables : string of your full name, another string of your mail.
create variable of your age (integer)
print all of them to the screen/

then, print your name from the end to the beginning and print it only with your age*3.

then, check if your name is stored inside this full string:
"idan, ben , dudu , yuval, shimon , yael , gal , adam , shahar , yana"
'''

name="shlomi vainblat"
mail="shlomi@gmail.com"
age=24
print("My name is: " + (name) + "\nMy mail is: " + (mail) + "\nMy age is: " + str(age))
print("\n\nMy name is: " + (name[::-1]) + "\nMy age is: " + str(age*3))
print(".........")
print("shlomi" in "idan, ben , dudu , yuval, shimon , yael , gal , adam , shahar , yana")