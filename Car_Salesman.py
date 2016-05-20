'''
Created on September 26, 2014

@author: mayberryr
'''
# Car Salesman
# Calculates actual price of the car after all expenses are added.
# Ronnie Mayberry
# Friday, September 26, 2014

cost = (input("\nPrice of car: "))
cost = int(cost)

tax = cost * .15
print("Tax:", tax)

carlicense = cost * .10
print("Car license:", carlicense)

dealerprep = 250
print("Dealer pre:", dealerprep)

destcharge = 20
print("Destination fee:", destcharge)

total = tax + carlicense + dealerprep + destcharge + cost

print("Actual car price:", total)
