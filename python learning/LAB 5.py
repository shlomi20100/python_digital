'''Create a dictionary with 5 name & money.
then, sum the money of the first & last names and print it to the screen.
after that, add a new name with the sum of thr money you calculated be4.
In the end, print thr number of the entries and check if "shlomi" inside'''

my_dict={"shlomi":20 , "irena":30 , "lora":40 , "beni":50 , "caspi":60}
print("The first dict is : " + (str(my_dict)))
print("The summary of shlomi and caspi's money is : " +  (str (my_dict["shlomi"]+my_dict["caspi"])))
my_dict["shir"]=80
print("The new dict is : " + (str(my_dict)))
print("The number of entries : " + (str(len(my_dict))))
print("shlomi" in my_dict)
