#Hw5

import math

def main():

    
    degree = float(input("Please enter an angle: "))
    x = math.radians(degree) #convert to radians
    cosine = math.cos(x)
    sine = math.sin(x)

    print("The cosine of", degree, "is", cosine)
    print("The sine of", degree, "is", sine)

main()