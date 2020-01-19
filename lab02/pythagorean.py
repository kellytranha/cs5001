#Hw4

import math

def main():

    PRECISION = 2
    
    x1 = float(input("Please enter x1: "))
    y1 = float(input("Please enter y1: "))
    x2 = float(input("Please enter x2: "))
    y2 = float(input("Please enter y2: "))

    e_dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    print("Euclidean distance between the two points is:", round(e_dist, PRECISION))

main()
