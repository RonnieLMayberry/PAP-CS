'''
Created on October 8, 2014

@author: mayberryr
'''
# Finicky Counter
# Demonstrates the break and continue statements.
# Ronnie Mayberry
# Tuesday, October 7, 2014

count = 0
while True:
    count += 1
    # end loop if count greater than 10
    if count > 1000:
        break
    # skip 5
    if count == 5:
        continue
    print(count)

input("\n\nPress the enter key to exit.")
