# commit1_demo.py

from user_input_validator import UserInputValidator

def commit1_demo():
    validator = UserInputValidator()
    sample_data = ["10", "5", "-3", "abc", "0"]

    valid, invalid = validator.validate_positive_integers(sample_data)

    print("Commit 1 Output:")
    print("Valid positive integers:", valid)
    print("Invalid values:", invalid)
    print("-----------------------------------")

if __name__ == "__main__":
    commit1_demo()
