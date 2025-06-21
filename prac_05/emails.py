"""
Emails
Estimate: 20 minutes
Actual: 21 minutes
"""


def main():
    """Get email and ask name"""
    email_to_name= {}
    email= input("Email: ").strip()
    while email != "":
        default_name= extract_name_from_email(email)
        name_confirmation = input(f"Is your name {default_name}? (Y/n) ").strip().lower()

        if name_confirmation == "" or name_confirmation == "y":
            name = default_name
        else:
            name= input("Name: ").strip()
        email_to_name[email]= name
        email= input("Email: ").strip()
    print()

