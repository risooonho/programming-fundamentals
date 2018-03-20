# function prompt_integer : reads a number and return it to a variable as an integer
def prompt_integer():
    integer = int(input())
    return integer

# function compare: compares two numbers
def compare(a,b):
    # first case: a>b -> return 0
    if a>b:
        return 0
    # second case: a=b -> return 1
    elif a==b:
        return 1
    # third case: a<b -> return -1
    elif a<b:
        return -1


# Tests
print(compare(5,2))
print(compare(2,5))
print(compare(3,3))

# User input
print("Please enter number A")
user_input_A = prompt_integer()
print("Please enter number B")
user_input_B = prompt_integer()

# Compare user inputs A and B
print(compare(user_input_A, user_input_B))

