#Hw1
#Source: https://www.wunderground.com/forecast/us/wa/seattle
# Highest temperature values predicted for the 10 day forecast
highest_temp = 54 #(1/23)

#Lowest temperature values predicted for the 10 day forecast
lowest_temp = 42 #(1/19)

difference = highest_temp - lowest_temp

print("The difference between the highest and the lowest temperature values predicted for the 10 day forecast:", difference, "degrees Fahrenheit")

#temperature at NOON predicted for the 10 day forecast (1/18-1/27)

temp18 = 44
temp19 = 47
temp20 = 48
temp21 = 48
temp22 = 45
temp23 = 53
temp24 = 52
temp25 = 50
temp26 = 49
temp27 = 48

average = (temp18 + temp19 + temp20 + temp21 + temp22 + temp23 + temp24 + temp25 +temp26 + temp27)/10

print("The average temperature at noon predicted for the 10 day forecas:", average, "degrees Fahrenheit")

BASE = 32
CONVERSION_FACTOR = 5.0/9.0
PRECISION = 2

celsius_temp = (float(highest_temp) - BASE) * CONVERSION_FACTOR

print("The highest temperature predicted for the 10 day forecast:", round(celsius_temp, PRECISION), "degrees Celsius")
