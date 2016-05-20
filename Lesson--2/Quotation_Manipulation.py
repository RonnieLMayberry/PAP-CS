'''
Created on September 24, 2014

@author: mayberryr
'''
# Ronnie Mayberry
# Tuesday, September 23, 2014
# Quotation Manipulation
# Demonstrates string methods.

# quote from IBM Chairman, Thomas Watson, in 1943.
quote = "I think there is a world market for maybe five computers."

print("Original quote:")
print(quote)

print("\nIn uppercase:")
print(quote.upper())

print("\nIn lowercase:")
print(quote.lower())

print("\nAs a title:")
print(quote.title())

print("\nThe case of each letter switched:")
print(quote.swapcase())

print("\nThe first letter is capitalized:")
print(quote.capitalize())

print("\nWhere all white spaces at beginning/end are removed:")
print(quote.strip())

print("\nOccurences of old string are replaced with new:")
print(quote.replace(think, know ,[1]))

print("\nWith a minor replacement:")
print(quote.replace("five", "millions of"))

print("\nOriginal quote is still:")
print(quote)

input("\n\nPress the enter key to exit.")

