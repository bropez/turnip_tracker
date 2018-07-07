"""
This is the pattern finder test script
"""


def pattern_finder(mon_price, tues_price, wed_price, thurs_price, fri_price):
    week_vals = [mon_price, tues_price, wed_price, thurs_price, fri_price]
    is_decreasing = True
    increase_decrease_flag = False
    is_random = False
    big_peak = False
    small_peak = False
    increase_counter = 0
    prev_value = 10000
    for day in week_vals:
        print("Current: " + str(day), "Previous: " + str(prev_value))
        # Checks if we have decreasing pattern
        # Decreasing is the default, if anything is above previous then the switch occurs and we are no longer
        # in the decreasing pattern and opens up opportunities for other patterns to be seen
        if prev_value <= day:
            is_decreasing = False
            increase_counter += 1
        elif prev_value > day and increase_counter > -1:
            increase_counter -= 1
            if increase_counter is 0:
                increase_decrease_flag = True

        # This checks to see if there is an increase and then a decrease
        # Since the beginning number is arbitrarily set, it will always be a decrease first
        if is_decreasing is False and increase_decrease_flag:
            print("We've reached the random phase.")
            is_random = True

        # Check to see if we have the small peak or big peak
        # if increase_counter is 3 and day >= 250 for big peak
        if is_decreasing is False and increase_counter is 3 and day >= 250:
            big_peak = True

        # if increase_counter is 3 and day < 250 for small peak
        if is_decreasing is False and increase_counter is 3 and day < 250:
            small_peak = True
        prev_value = day

    text = "A pattern wasn't chosen."
    if is_decreasing:
        text = "This is a decreasing pattern."
    elif is_random:
        text = "This is the random pattern."
    elif big_peak:
        text = "This is the big peak, sell them now."
    elif small_peak:
        text = "This is the small peak, wait for one more and sell them."

    print(text)
    # print("The increase counter is " + str(increase_counter))
    print("\n\n")


print("This is a decreasing pattern.")
pattern_finder(100, 90, 80, 70, 60)

print("This is a random pattern.")
pattern_finder(100, 110, 90, 95, 50)

print("This is the big peak")
pattern_finder(100, 120, 270, 80, 10)

print("This is the small peak")
pattern_finder(100, 130, 140, 155, 80)
