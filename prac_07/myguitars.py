from guitar import Guitar

FILENAME="guitars.csv"

def main():
    guitars = load_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)
    new_guitars=add_new_guitar()
    for guitar in new_guitars:
        guitars.append(guitar)
    save_guitars(guitars, FILENAME)

def load_guitars(filename):
    """Load guitar from the csv file into list of Guitar objects."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    """Display the guitar list."""
    print("These are my guitars: ")
    for i, guitar in enumerate(guitars,1):
        print(guitar)

def add_new_guitar():
    """Prompt user to add a new guitar."""
    guitars=[]
    print("Would you like to add a new guitar?")
    name= input("Name:")
    while name != "":
        year = int(input("Year:"))
        cost = float(input("Cost:"))
        guitars.append(Guitar(name, year, cost))
        name = input("Name:")
    return guitars


def save_guitars(guitars, filename):
    """Save the guitar list."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

if __name__ == '__main__':
    main()