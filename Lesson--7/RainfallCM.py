'''
Created on Jan 27, 2015

@author: mayberryr
'''
rainfall = open("rainfall.txt", "r")
output = open("rainfallInCM.txt", "w")

for aline in rainfall:
    values = aline.split()
    
    inches = float(values[1])
    cm = 2.54 * inches
    
    output.write(values[0] + " " + str(cm) + "\n")

rainfall.close()
output.close()
