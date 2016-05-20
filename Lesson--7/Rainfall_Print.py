'''
Created on Jan 29, 2015

@author: mayberryr
'''
rainfall = open("rainfall.txt", "r")
output = open("rainfallfmt.txt", "w")

for aline in rainfall:
    values = aline.split()
    
    country = values[0]
    rain_fall = values[1]
    
    try:
        country = float(values[0])
        break
    except ValueError as e:
        print(e)
        
    print(values[0], "had", values[1], "inches of rain.")
    output.write("The country of %+25s has %5.1f inches yearly." % (values[0], values[1]))
    
print("Data formatted into a new file.")
    
rainfall.close()
output.close()