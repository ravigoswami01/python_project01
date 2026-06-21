# password strength checker

import re 

def check_password_strength(password):
    # Check for minimum length
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        return "Weak: Password must contain at least one uppercase letter."
    
    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        return "Weak: Password must contain at least one lowercase letter."
    
    # Check for digits
    if not re.search(r'\d', password):
        return "Weak: Password must contain at least one digit."
    
    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Password must contain at least one special character."
    
    return "Strong: Your password is strong."

# example usage
def password_strength_checker():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(strength)

# run the password checker tool 
if __name__ == "__main__":
    password_strength_checker()
    