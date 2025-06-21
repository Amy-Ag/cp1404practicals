"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland",
                "NSW": "New South Wales",
                "NT": "Northern Territory",
                "WA": "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria", "TAS": "Tasmania",
                "SA": "South Australia"}
print(CODE_TO_NAME)
user_entries=[]
state_code = input("Enter short state: ").upper()
while state_code != "":
    #EAFP
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
        state_name= CODE_TO_NAME[state_code]
        user_entries.append((state_code,state_name))
    except KeyError:
        print("Invalid state input")
    state_code = input("Enter short state: ").upper()
for code, state_name in user_entries:
    print(f"{code:<3} is {state_name}")