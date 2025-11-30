# user_input_validator.py

class UserInputValidator:
    def validate_positive_integers(self, values):
        valid = []
        invalid = []

        for v in values:
            try:
                n = int(v)
                if n > 0:
                    valid.append(n)
                else:
                    invalid.append(v)
            except ValueError:
                invalid.append(v)

        return valid, invalid
