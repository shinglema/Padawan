import random
# randint generates a random integar between the first parameter and the second
var_number_trys=1
lower_limit_number=1
upper_limit_number=10




cpu_number = random.randint(lower_limit_number, upper_limit_number)
print(cpu_number)

var_input = random.randint(lower_limit_number, upper_limit_number)

my_list_guesses = [var_input]
print(len(my_list_guesses))

print ("Thanks for entering: ", var_input)

var_diff = abs(cpu_number-var_input)
var_status='none'

while cpu_number!=var_input:

    print("You are on try number ", var_number_trys)

    if var_input==cpu_number:
        print ("You are right on the money")

    if var_diff>=0 and var_diff<=300:
        print ("You are getting hot: ", var_diff)


    if var_diff>=400 and var_diff<=600:
        print ("You are getting warm: ", var_diff)

    if var_diff>600:
        print ("You are cold: ", var_diff)

    var_input = random.randint(lower_limit_number, upper_limit_number)
 
    var_diff = abs(cpu_number-var_input)
    var_number_trys=var_number_trys+1