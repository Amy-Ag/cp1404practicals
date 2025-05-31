MENU = "1.Get valid score\n2.Print results\n3.Show stars\n4. Quit"

def main ():
    print(MENU)
    choice=input(">>>")
    while choice!="4":
        if choice == "1":
           score= validate_score()
        elif choice == "2":
            result=get_result(score)
            print(result)
        elif choice == "3":
            stars=print_stars(score)
            print(stars)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>>")
    print("Farewell")

def validate_score():
    score=int(input('Enter your score: '))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input('Enter your score: '))
    return score

def get_result(score):
    if score >= 90:
        message = "Excellent"
    elif score >= 50:
        message = "Passable"
    else:
        message = "Bad"
    return message


def print_stars(score):
    return "*"*score

main()