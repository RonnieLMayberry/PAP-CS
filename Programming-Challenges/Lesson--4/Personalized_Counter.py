'''
Created on October 28, 2014

@author: mayberryr
'''
# Personalized Counter
# Allows the user to input the range data, and prints out the output of the range.
# Ronnie Mayberry
# Tuesday, October 28, 2014

start = int(input("\nWhat number do you want to start at?"))
end = int(input("\nWhat number do you want to end up at?"))
intr = int(input("\nWhat number do you want to count by?"))

for i in range(start, end, intr):
    print(i, end="")
