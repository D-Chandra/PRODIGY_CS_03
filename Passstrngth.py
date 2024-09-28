import re

#Function to evaluate password strength
def evaluate_password_strength(password):
    feedback = []

    #check for length of password
    if len(password) < 16:
        feedback.append("Password is short as per latest NIST and CISA standards. It should be as long as 16 character.")
        if len(password) < 8:
            feedback.append("Password length is also lower than the minimum requirements of 8 characters.")
        else:
            feedback.append("Password length is ok.")
    
    #check for uppercase characters
    if not re.search(r'[A-Z]', password):
        feedback.append("Should include at least one uppercase letter.(Multiple are recommended)")
    else:
        feedback.append("Contains Uppercase Letters.")
    
    #check for lowercase charachters
    if not re.search(r'[a-z]', password):
        feedback.append("Should include at least one lowercase letter.(Multiple are recommended)")
    else:
        feedback.append("Contains Lowercase Letters")
    
    #check for numbers
    if not re.search(r'[0-9]', password):
        feedback.append("Should include at least one number.(Multiple are recommended)")
    else:
        feedback.append("Contains numbers.")

    #check for special characters
    if not re.search(r'[\W_]', password):
        feedback.append("Should include at least one special character.(Multiple are recommended)")
    else:
        feedback.append("Contains Special characters")

    # Common sequence checks
    common_patterns = [
        r'123456', r'654321', r'12345', r'987654321', r'password', r'admin', r'qwerty',
        r'abcdef', r'iloveyou', r'letmein', r'111111', r'000000', r'football', r'sunshine',
        r'abc', r'asdf', r'zxcvbn', r'2023', r'2022', r'1990', r'princess', r'dragon', r'monkey'
    ]
    
    for pattern in common_patterns:
        if re.search(pattern, password.lower()):
            feedback.append(f"Password contains a common pattern: '{pattern}'")
            break  # If one pattern is found, we don't need to check others
    
    return feedback

# Function to assess strength of passwords in a file
def assess_passwords_in_file(filename):
    with open(filename, 'r') as file:
        passwords = file.readlines() # Read all lines (passwords) from the file
    
    for index, password in enumerate(passwords, start=1): # Loop through each password, with line numbers starting at 1
        password = password.strip() # Remove any leading/trailing whitespace (e.g., newlines)
        print(f"\nEvaluating password {index}: {password}")  # Print which password is being evaluated
        feedback = evaluate_password_strength(password)  # Call the function to assess the password strength
        for comment in feedback:  # Loop through feedback messages for this password
            print(comment)  # Print each feedback message

#Main Function
def main():
    choice  = input("Do you want to input a password or assess passwords from a file? (input/file): ").lower()

    if choice == 'input':
        password = input("Enter the password you want to evaluate: ")
        feedback = evaluate_password_strength(password)
        print("\nPassword Strength Feedback:")
        for comment in feedback:
            print(comment)
    elif choice == 'file':
        filename = input("Enter the file path containing passwords(File should be structured as - 1 password per line): ")
        try:
            assess_passwords_in_file(filename)
        except FileNotFoundError:
            print("Error: The Specified file was not found.")
    else:
        print("Invalid Choice. Please select 'input' or 'file'.")

main()
