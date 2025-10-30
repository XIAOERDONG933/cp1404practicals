"""
Emails
Estimate: 20 minutes
Actual:   36 minutes
"""

def main():
    """Store users' emails and names in a dictionary."""
    email_to_name = get_email_name_map()
    display_email_name_map(email_to_name)

def get_email_name_map():
    """Get email name map."""
    email_to_name = {}
    email = input("Email: ").strip()
    while email:

        name = extract_name_from_email(email)
        correct_name = input(f"Is your name {name}? (Y/n): ").strip().lower()

        if correct_name not in ['n', 'no']:
            email_to_name[email] = name
        else:
            name = input("Name: ").strip()
            email_to_name[email] = name

        email = input("Email: ").strip()
    return email_to_name

def display_email_name_map(email_to_name):
    """Display the names of the emails."""
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name_from_email(email):
    """Extract name from email address."""
    local_part = email.split('@')[0]
    name_parts = local_part.split('.')
    name = ' '.join(name_parts).title()
    return name

main()