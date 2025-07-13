from guitar import Guitar

FILENAME="guitars.csv"

def main():
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)

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
    for i, guitar in range(guitars,1):
        print(guitar)

if __name__ == '__main__':
    main()