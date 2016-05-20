'''
Created on Jan 27, 2015

@author: mayberryr
'''
rainfall = open("rainfall.txt", "r")

for aline in rainfall:
    values = aline.split()
    print(values[0], "had", values[1], "inches of rain.")
    
rainfall.close()