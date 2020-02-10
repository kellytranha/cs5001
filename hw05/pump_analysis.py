STARTING_NUMBER = 0
COUNTING_MINUTE = 1
THRESHOLD = 500
COUNTING_GALLON = 2
NEVER_REACH = -1
MINUTES_PER_HR = 60
HOURS_PER_DAY = 24
COUNTING = 1
KWH = 1000
GALLON_TO_REACH_ONE = 5
GALLON_TO_REACH_TWO = 100
COUNTING_CONTINUOUS = 120
INDEX_OFFSET = 1


def reach_gallon(content, gallon_to_reach):
    minute = STARTING_NUMBER
    gallon = STARTING_NUMBER

    for number in content:
        if gallon >= gallon_to_reach:
            break
        minute += COUNTING
        if number >= THRESHOLD:
            gallon += COUNTING_GALLON
    else:
        minute = NEVER_REACH
    print("It took", minute, "minutes of data to reach",
          gallon_to_reach, "gallons.")


def main():
    name = input("Please enter the file name: ")

    try:
        data = open(name, "r")
    except Exception:
        print("Unable to open", name)
        return

    content = data.read().split("\n")

    for index, string in enumerate(content):
        content[index] = int(string)

    hours = len(content) / MINUTES_PER_HR
    days = hours / HOURS_PER_DAY

    print("Data covers a total of", hours, "hours")
    print("(That's", days, "days)\n")

    num_minute = STARTING_NUMBER
    for number in content:
        if number >= THRESHOLD:
            num_minute += COUNTING_MINUTE

    num_gallon = num_minute * COUNTING_GALLON
    gallon_per_day = num_gallon / days

    print("Pump was running for", num_minute, "minutes, producing",
          num_gallon, "gallons)")

    print("(That's", gallon_per_day, "gallons per day)\n")

    num_watt = STARTING_NUMBER
    for number in content:
        num_watt += number

    kilo_watt = num_watt / KWH / MINUTES_PER_HR

    print("Pump required a total of ", num_watt, "watt minutes of power)")
    print("That's", kilo_watt, "kWh\n")

    reach_gallon(content, GALLON_TO_REACH_ONE)
    reach_gallon(content, GALLON_TO_REACH_TWO)
    print()

    print("Information on water softener recharges: ")

    count = STARTING_NUMBER
    for index, number in enumerate(content):
        if number >= THRESHOLD:
            count += COUNTING
        else:
            if count >= COUNTING_CONTINUOUS:
                print(count, "minute run started at ", end="")
                print(index - count + INDEX_OFFSET)
            count = STARTING_NUMBER


main()
