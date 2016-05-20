'''
Created on January 14, 2015

@author: mayberryr
'''
# Handle It
# Demonstrates handling exceptions.
# Ronnie Mayberry
# Wednesday, January 14, 2015

# try/except
try:
    num = float(input("Enter a number: "))
except:
    print("Something went wrong!")

# specifying exception type
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")

# handle multiple exception types
print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Something went wrong!")

print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))
    except TypeError:
              print("I can only convert a string or a number!")
    except ValueError:
              print("I can only convert a string or digits!")

# get an exception's argument
try:
              num = float(input("\nEnter a number: "))
except ValueError as e:
              print("That was not a number! Or as Python would say...")
              print(e)

# try/except/else
try:
              num = float(input("\nEnter a number: "))
except ValueError:
              print("That was a not a number!")
else:
              print("You entered the number", num)

input("\n\nPress the enter key to exit.")   
