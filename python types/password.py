import string
import secrets

def make_secure_password(length: int = 16, include_uppercase: bool = True, 
                         include_numbers: bool = True, include_symbols: bool = True) -> str:
    """
    Generates a secure, random password that meets specified criteria.

    Args:
        length (int): The desired length of the password. Defaults to 16.
        include_uppercase (bool): Whether to include uppercase letters. Defaults to True.
        include_numbers (bool): Whether to include numbers. Defaults to True.
        include_symbols (bool): Whether to include symbols. Defaults to True.

    Returns:
        str: A securely generated random password.
    """
    
    # 1. Build the character set based on the user's choices.
    # We always start with lowercase letters.
    characters = string.ascii_lowercase
    print(characters)
    if include_uppercase:
        characters += string.ascii_uppercase
        print(characters)
    if include_numbers:
        characters += string.digits
        print(characters)
    if include_symbols:
        characters += string.punctuation
        print(characters)

    # 2. Loop until a password that meets all criteria is generated.
    while True:
        # Generate a random password from the full character set.
        password = "".join(secrets.choice(characters) for _ in range(length))
        
        # 3. Validate the password to ensure it meets the criteria.
        # This prevents a rare case where the random choice might miss a character type.



        conditions_met = [
            any(c in string.ascii_lowercase for c in password),
            any(c in string.ascii_uppercase for c in password) if include_uppercase else True,
            any(c in string.digits for c in password) if include_numbers else True,
            any(c in string.punctuation for c in password) if include_symbols else True
        ]

        print(conditions_met)
        
        # 4. If all conditions are met, break the loop and return the password.
        if all(conditions_met):
            return password

# This block runs only when the script is executed directly.
if __name__ == "__main__":
    print("--- Password Examples ---")

   # Example 1: Default password (16 chars, all types included)
    default_password = make_secure_password()
    print(f"Default Password (16 chars): {default_password}")

    # Example 2: Shorter password with no numbers
    easy_password = make_secure_password(length=8, include_numbers=False)
    print(f"Easy Password (8 chars, no numbers): {easy_password}")

    # Example 3: Long password with only letters and symbols
    symbols_and_letters_password = make_secure_password(length=32, include_numbers=False)
    print(f"Symbols & Letters Password (32 chars): {symbols_and_letters_password}")
    
    # Example 4: A simple password with only lowercase letters
    simple_password = make_secure_password(length=12, include_uppercase=False, include_numbers=False, include_symbols=False)
    print(f"Simple Password (12 chars, lowercase only): {simple_password}")

