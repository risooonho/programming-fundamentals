# function new_line: prints a new line
def new_line():
   print()

# function three_lines: prints 3 new lines
def three_lines():
   new_line()
   new_line()
   new_line()

# function nine_lines: prints 9 new lines
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

# function clear_screen: clears screen by printing 25 new lines
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

# calls nine_lines() to print 9 new lines
print("now printing 9 lines")
nine_lines()

# calls clear_screen to print 25 lines
print("now printing 25 lines")
clear_screen()