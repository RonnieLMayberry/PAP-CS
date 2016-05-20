'''
Created on October 8, 2014

@author: mayberryr
'''
# Exclusive Network
# Demonstrates logical operators and compound conditions.
# Ronnie Mayberry
# Wednesday, October 8, 2014

print("\tExclusive Computer Network")
print("\t\tMembers only!\n")

security = 0

username = ""
while not username:
    username = input("Username: ")

password = ""
while not password:
    password = input("Password: ")

if username == "Mrs. Walter" and password == "secret":
    print("Hi, Mrs. Walter.")
    security = 5
    print("Your security level is:", security)
    
elif username == "S. Meier" and password == "civilization":
    print("Hey, Sid.")
    security = 3
    print("Your security level is:", security)
    
elif username == "S. Miyamoto" and password == "mariobros":
    print("What's up, Shigeru?")
    security = 3
    print("Your security level is:", security)
    
elif username == "W. Wright" and password == "thesims":
    print("How goes it, Will?")
    security = 3
    print("Your security level is:", security)
    
elif username == "guest" or password == "guest":
    print("Welcome, guest.")
    security = 1
    print("Your security level is:", security)
    
else:
    print("Login failed. You're not so exclusive.\n")

input("\n\nPress the enter key to exit.")
