"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score=float(input("Enter score: "))
    result= validate_score(score)
    print(f"Your result is {result}")

def validate_score(score):
    if score < 0 or score > 100:
        message="Invalid score"
    elif score>=90:
        message="Excellent"
    elif score>=50:
        message="Passable"
    else:
        message="Bad"
    return message

main()