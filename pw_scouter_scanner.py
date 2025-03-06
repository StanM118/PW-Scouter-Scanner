import re

def check_password_strength(password: str) -> str:
    """Evaluates the strength of the provided password and gives suggestions."""
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    if not re.search(r"[A-Z]", password):
        return "Weak: Include at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return "Weak: Include at least one lowercase letter."

    if not re.search(r"[0-9]", password):
        return "Weak: Include at least one digit."

    if not re.search(r"[!@#$%^&*()_+-=]", password):
        return "Weak: Include at least one special character."

    if re.search(r"\s", password):
        return "Weak: Password should not contain spaces."

    common_passwords = ['password', '123456', 'qwerty', 'abc123', 'letmein']
    if password.lower() in common_passwords:
        return "Weak: Avoid common passwords."

    return "Strong Password!"

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    print(check_password_strength(password))

