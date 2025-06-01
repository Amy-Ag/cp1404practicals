"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
MINIMUM_SCORE=0
MAXIMUM_SCORE=100

def main():
    score=float(input("Enter score: "))
    result= validate_score(score)
    print(f"Your result is {result}")
    random_score = random.uniform(MINIMUM_SCORE, MAXIMUM_SCORE)
    random_result = validate_score(random_score)
    print(f"Your random number, {random_score} result is {random_result}")

def validate_score(score):
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        message="Invalid score"
    elif score>=90:
        message="Excellent"
    elif score>=50:
        message="Passable"
    else:
        message="Bad"
    return message

main()