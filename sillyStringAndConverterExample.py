# This is a file to run the several examples in the Python book

# Silly Strings example:

print("\nStarting with a newline, \n" \
      + "Then using concatenate " + "and the line continuation character, " \
      + "\nWe can print much larger lines using a single function call!\n")
print("String repeat " * 5 + "\n")

print("Now let's work with the \"input\" function: \n")

number_str = input("enter a number: ")

print("\nThe number entered is stored as a string: " + number_str + "\n")

#Let's change the input into an int and float

number_float = float(number_str)
number_int = int(number_float) #int() needs a literal int from a string,
# or a float not a string representation of a float

print("Converted, the input is now a float: " + number_float + " and an integer: " \
      + number_int + "\n")
