# function prompt_intener : reads a number and return it to a variable as an integer
def prompt_integer():
    integer = int(input())
    return integer

# function prompt_number : reads an number and checks if it is valid
def prompt_number():
    number = prompt_integer()
    # While first number is equal to 0
    while number == 0:
        #    Display error
        print("Error! Number can't be 0")
        #    Prompt for number
        #    Read number and store in variable
        number = prompt_integer()
    return number
        

## FIRST NUMBER

# Prompt for first number 
print("Please enter first number")
# Read first number and store in variable
first_number = prompt_number()

## OPERATION

# Display operations (1-add, 2-subtract, 3-multiply, 4-divide) 
print("The operations available are: 1-add, 2-subtract, 3-multiply, 4-divide")
# Prompt for operation 
print("Please choose number according to operation")
# Read operation and store in variable
operation = prompt_number()
# While operation is less than 1 or operation is greater than 4
while operation < 1 or operation > 4:
#    Display error
    print("Error! Choose correct operation")
    #    Prompt for operation
    #    Read operation and store in variable
    operation = prompt_number()


## SECOND NUMBER

# Prompt for second number 
print("Please enter second number")
# Read first number and store in variable
second_number = prompt_number()


## DOES OPERATION

# If operation is equal to 1 (add) 
if operation == 1: #add
    #      Add first number to second number and store result in variable 
    result = first_number + second_number

# Otherwise if operation is equal to 2 (subtract) 
elif operation == 2:
    #      Subtract second number from first number and store result in a variable
    result = first_number - second_number

# Otherwise if operation is equal to 3 (multiply)
elif operation == 3:
    #      Multiply first number with second number and store result in a variable Other wise if operation is equal to 4 (divide) 
    result = first_number * second_number

#    Otherwise (divide)
else:
    #      Divide first number by the second number and store result in a variable 
    result = first_number/second_number


# Display the result stored in the variable 
print("The result is {}".format(result))