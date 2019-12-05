#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: December 2019
# this function uses an array
# with user input

import random
some_variable = random.randint(1, 100)
# a number between 1 and 100


def main():
    # this function uses an array

    random_numbers = []

    # process & output
    for loop_counter in range(0, 10):
        some_variable = random.randint(1, 100)
        random_numbers.append(some_variable)
        print("{0}".format(random_numbers[loop_counter]))

    average = sum(random_numbers) / 10
    print("Average of the list = {0}".format(average))


if __name__ == "__main__":
    main()
