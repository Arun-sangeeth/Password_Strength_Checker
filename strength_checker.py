import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Check for character diversity
    if re.search(r'[a-z]', password): score += 1
    else: feedback.append("Add lowercase letters.")
    
    if re.search(r'[A-Z]', password): score += 1
    else: feedback.append("Add uppercase letters.")
    
    if re.search(r'[0-9]', password): score += 1
    else: feedback.append("Add numbers.")
    
    if re.search(r'[^A-Za-z0-9]', password): score += 1
    else: feedback.append("Add special characters.")

    # Check against common passwords
    with open("common_passwords.txt") as file:
        common = set(line.strip() for line in file)
    if password in common:
        feedback.append("Password is too common.")
        score = 0

    # Score interpretation
    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {"strength": strength, "score": score, "feedback": feedback}
