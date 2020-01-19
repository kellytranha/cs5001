#Hw2,3

def main():

    PRECISION = 2 

    num1 = float(input("Enter a first value: "))
    num2 = float(input("Enter a second value: "))
    total = num1 + num2

    print("The sum of", num1, "+", num2, "is", round(total, PRECISION))

main() 
