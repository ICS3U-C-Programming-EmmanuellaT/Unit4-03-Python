#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on 14th november, 2026
# This program asks the user for a whole number
# and calculates the power of two for that number in a for loop
# and catches errors that are not integers and displays it back to the user.


def main():
    user_number = input("Enter a whole number ")
    try:
        user_number = int(user_number)
        if user_number >= 0:
            for counter in range(user_number + 1):
                power_of_two = counter**2
                print(
                    "2 to the power of {counter} is {power_of_two}".format(
                        counter=counter, power_of_two=power_of_two
                    )
                )
        else:
            print(
                "{user_number} is not a positive number, please enter a positive number".format(
                    user_number=user_number
                )
            )
    except Exception:
        print(
            "{user_number} is not a valid number, enter a valid integer".format(
                user_number=user_number
            )
        )

    finally:
        print("Program ended.")


if __name__ == "__main__":
    main()
