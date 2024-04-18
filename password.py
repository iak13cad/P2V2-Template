"""
    You are required to write a Python script that prompts the user to input a password and checks if the password meets the following security requirements:

    The password must be at least 8 characters long.
    The password must contain at least one uppercase letter.
    The password must contain at least one digit.
    The password should not contain any spaces.

Use DIGITS and UPERCASE_LETTERS to check for one digit/upercase letter. Hint: in
The program should continuously prompt the user to enter a password until all the requirements are met. Once a valid password is provided, the program should print a confirmation message and terminate.

Example Interaction and Output

Input 1
User enters: password

Output:
Password must be at least 8 characters long.
Password must contain at least one uppercase letter.
Password must contain at least one digit.

Input 2
User enters: Password1

Output:
Password is valid.

Input 3
User enters: Pass 123

Output:
Password should not contain spaces.
Password must be at least 8 characters long.
"""

"""
@ASSESSME.USERID: userID
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Practical 2
@ASSESSME.ANALYZE: YES
"""

DIGITS = "0123456789"
UPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def validate_password():
    pass

def main():
    validate_password()

if __name__ == "__main__":
    main()