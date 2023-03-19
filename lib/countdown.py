# your code goes here!
import time


def countdown(integer):
    while integer >= 1:
        print(f"{integer} SECOND(S)!")
        integer -= 1
    if integer == 0:
        print("HAPPY NEW YEAR!")


# countdown(10)


def countdown_with_sleep(an_integer):
    while an_integer >= 1:
        print(f"{an_integer} SECOND(S)!")
        an_integer -= 1
        time.sleep(1)
    if an_integer == 0:
        print("HAPPY NEW YEAR!")


countdown_with_sleep(10)
