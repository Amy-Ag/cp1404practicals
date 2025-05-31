MINIMUM_LENGTH=5
def main():
    password=get_valid_password(MINIMUM_LENGTH)
    asterisks=generate_asterisks(password)
    print(asterisks)

def get_valid_password(minimum_length):
    """Ask user to enter a password until it meets minimum length required."""
    password=input("Enter password: ")
    while len(password) < minimum_length:
        print(f"Password must be {MINIMUM_LENGTH} long.")
        password = input("Enter password: ")
    return password

def generate_asterisks(password):
    """Print asterisks equal to the length of password"""
    return "*"*len(password)

main()