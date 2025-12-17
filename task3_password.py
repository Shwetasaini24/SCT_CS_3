import re

def check_password_strength(password):
    score = 0
    criteria = {
        "length_8_plus": False,
        "uppercase": False,
        "lowercase": False,
        "number": False,
        "special_char": False,
    }
    if len(password) >= 8:
        score += 1
        criteria["length_8_plus"] = True
    if len(password) >= 12:
        score += 1 
    if re.search(r'[A-Z]', password):
        score += 1
        criteria["uppercase"] = True
    if re.search(r'[a-z]', password):
        score += 1
        criteria["lowercase"] = True
    if re.search(r'[0-9]', password):
        score += 1
        criteria["number"] = True
    if re.search(r'[^a-zA-Z0-9\s]', password):
        score += 1
        criteria["special_char"] = True
    if score >= 6:
        rating = "Excellent (Highly Recommended)"
    elif score >= 5:
        rating = "Strong"
    elif score >= 3:
        rating = "Moderate"
    elif score >= 1:
        rating = "Weak"
    else:
        rating = "Very Weak"

    return {
        "score": score,
        "rating": rating,
        "criteria": criteria
    }

def display_results(password, results):
    """
    Prints the assessment results in a user-friendly format.
    """
    print("\n--- Password Strength Assessment ---")
    print(f"Password: **{password}**")
    print(f"Total Score: **{results['score']} / 6**")
    print(f"Overall Rating: **{results['rating']}**")
    print("\n--- Criteria Met ---")
    
    # Iterate through criteria to show status
    for key, met in results['criteria'].items():
        status = "✅ MET" if met else "❌ NOT MET"
        
        # Friendly description of the criteria
        description = key.replace('_', ' ').title()
        if key == "length_8_plus":
            description = "Minimum Length (8+ Characters)"
        elif key == "special_char":
            description = "Special Characters (!@#$...)"
            
        print(f"  [{status}] {description}")
    print("----------------------------------\n")

if __name__ == "__main__":
    while True:
        user_password = input("Enter a password to assess: ")
        if user_password.lower() == 'quit':
            break
        
        if not user_password:
            print("Please enter a password.")
            continue
            
        assessment = check_password_strength(user_password)
        display_results(user_password, assessment)