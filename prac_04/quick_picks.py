import random
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():
    number_of_picks = int(input("How many quick picks? "))
    for number in range(number_of_picks):
        quick_pick = get_quick_pick()
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


def get_quick_pick():
    """Generate a quick pick of non-repeated random numbers in same line."""
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    return quick_pick


main()
