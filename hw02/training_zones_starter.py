def main():
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    print("=======================================")

    ZONE_1_LOWER_BOUND = 0.5
    ZONE_1_UPPER_BOUND = 0.6
    ZONE_2_UPPER_BOUND = 0.7
    ZONE_3_UPPER_BOUND = 0.8
    ZONE_4_UPPER_BOUND = 0.93
    ZONE_5_UPPER_BOUND = 1.00

    PRECISION = 2

    #Compute the maximum heart rate using the given equation.
    max_heart_rate = 208 - 0.7 * age 
    #Subtract the resting heart rate from the maximum heart rate
    reserve = max_heart_rate - restHR

    zone_1_lower = round(restHR + reserve * ZONE_1_LOWER_BOUND, PRECISION)
    zone_1_upper = round(restHR + reserve * ZONE_1_UPPER_BOUND, PRECISION)
    zone_2_lower = round(zone_1_upper + 0.01, PRECISION)
    zone_2_upper = round(restHR + reserve * ZONE_2_UPPER_BOUND, PRECISION)
    zone_3_lower = round(zone_2_upper + 0.01, PRECISION)
    zone_3_upper = round(restHR + reserve * ZONE_3_UPPER_BOUND, PRECISION)
    zone_4_lower = round(zone_3_upper + 0.01, PRECISION)
    zone_4_upper = round(restHR + reserve * ZONE_4_UPPER_BOUND, PRECISION)
    zone_5_lower = round(zone_4_upper + 0.01, PRECISION)
    zone_5_upper = round(restHR + reserve * ZONE_5_UPPER_BOUND, PRECISION)


    print("Your heart rate reserve is: ", reserve, "bpm")
    print("Here is a breakdown of your training zones:")
    print("Zone 1:", zone_1_lower, "to", zone_1_upper, "bpm")
    print("Zone 2:", zone_2_lower, "to", zone_2_upper, "bpm")
    print("Zone 3:", zone_3_lower, "to", zone_3_upper, "bpm")
    print("Zone 4:", zone_4_lower, "to", zone_4_upper, "bpm")
    print("Zone 5:", zone_5_lower, "to", zone_5_upper, "bpm")

    print("=======================================")

main()