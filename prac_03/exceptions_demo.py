"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
-->It occurs when user enters something that cannot be converted
to an integer.
2. When will a ZeroDivisionError occur?
-->It occurs when denominator is a zero and program divides it which
is logically an invalid answer.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
-->Yes.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Cannot divide by zero!")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

