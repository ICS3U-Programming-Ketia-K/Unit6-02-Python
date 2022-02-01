#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Jan. 28, 2022
# This program uses a for loop to generate
# random numbers in a list, then
# displays the largest value

import constants
import random


# This function calculates the max value in the list of elements
def find_max_value(random_numbers):

    max_value = random_numbers[0]

    # calculate the max value
    for loop_counter in range(len(random_numbers)):
        if max_value < random_numbers[loop_counter]:
            max_value = random_numbers[loop_counter]

    return max_value


def main():
    # initializing counter
    loop_counter = 0

    # declaring variable
    random_nums_user = []

    # display opening message to console
    print("This program generates a list of 10 random "
          "numbers between 0 and 100, then determines the largest number.")
    print("")

    # displays random numbers and determine largest value
    for loop_counter in range(constants.MAX_ARRAY_SIZE):
        random_nums_user.append(random.randint(constants.MIN_NUM,
                                               constants.MAX_NUM))
        print("{} added to the list at position {}"
              .format(random_nums_user[loop_counter], loop_counter))

    max_user = find_max_value(random_nums_user)
    print("")
    print("The maximum value is: {}" .format(max_user))


if __name__ == "__main__":
    main()
