"""
This is the pattern finder test script version 2
"""


def is_decreasing(buying, monam_val, monpm_val, tuesam_val, tuespm_val, wedam_val, wedpm_val, thursam_val, thurspm_val, friam_val, fripm_val):
    week = [monam_val, monpm_val, tuesam_val, tuespm_val, wedam_val, wedpm_val, thursam_val, thurspm_val, friam_val, fripm_val]
    decrease = True
    prev_val = buying
    for price in week:
        print("Previous: " + str(prev_val), "Current: " + str(price))
        # This is checking if there is a decrease or stagnant price, there usually isn't a stagnant price so I might
        # take that out later. If there ever is an increase then we throw a flag and break the loop and return the
        # decision
        if prev_val <= price:
            decrease = False
            # print("It stops here.")
            break
        prev_val = price

    return decrease


def is_random(buying, monam_val, monpm_val, tuesam_val, tuespm_val, wedam_val, wedpm_val, thursam_val, thurspm_val, friam_val, fripm_val):
    week = [monam_val, monpm_val, tuesam_val, tuespm_val, wedam_val, wedpm_val, thursam_val, thurspm_val, friam_val, fripm_val]
    random = True
    prev_val = buying
    increase_times = 0
    for price in week:
        print("Previous: " + str(prev_val), "Current: " + str(price))

        # This is to check if there has been an increase which is vital for a random pattern.
        if prev_val < price:
            increase_times += 1
            # print("Increased.")

        # This is to check if it is decreasing and is above 0, we don't want any negative numbers
        # when trying this or else it'll ruin things.
        elif prev_val > price and increase_times > 0:
            increase_times -= 1
            # print("Decreased")

        # Checking to see if it increased more than once. Random patterns have one increase and then
        # an immediate decrease
        if increase_times > 1:
            # print("Random can't go above 1 increase proving it is random")
            random = False
            break

        prev_val = price

    return random


def is_big_peak(buying, monam_val, monpm_val, tuesam_val, tuespm_val, wedam_val, wedpm_val, thursam_val, thurspm_val, friam_val, fripm_val):
    week = [monam_val, monpm_val, tuesam_val, tuespm_val, wedam_val, wedpm_val, thursam_val, thurspm_val, friam_val, fripm_val]
    big_peak = True
    prev_val = buying
    increase_times = 0
    for price in week:
        print("Previous: " + str(prev_val), "Current: " + str(price))

        # We check to see if there is an increase in price. If there is then we increment the counter. If the counter
        # gets to 3 and it is less than 250 then we know that it is small peak. If not then we have big peak.
        if prev_val < price:
            increase_times += 1
            # print("Increased.")
        elif prev_val > price and increase_times > 0:
            increase_times -= 1
            # print("Decreased")
        if increase_times is 3 and price < 250:
            big_peak = False
            break

    return big_peak
