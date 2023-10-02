
email = input("Enter your email: ")

def is_valid_email(email):
    if len(email) >= 6:
        if email[0].isalpha():
            if email.count("@") == 1 and "@" in email:
                if email[-4] == "." or email[-3] == ".":
                    for i in email:
                        if i.isspace():
                            return "Wrong Email: contains whitespace"
                        elif i.isalpha():
                            if i.isupper():
                                return "Wrong Email: contains uppercase letters"
                        elif i.isdigit():
                            continue
                        elif i not in ['_', '.', '@']:
                            return "Wrong Email: contains invalid characters"
                    return "Right Email"
                else:
                    return "Wrong Email: incorrect format"
            else:
                return "Wrong Email: invalid '@' placement or count"
        else:
            return "Wrong Email: must start with a letter"
    else:
        return "Wrong Email: too short"

print(is_valid_email(email))


# 1.Changed variable name Email to email to follow Python's convention of using lowercase for variable names.
# 2.Renamed the variable in the input function to email for consistency.
# 3.Changed Email to email in the code for consistency.
# 4.Fixed the conditions for checking the email format.
# 5.Updated the logic inside the loop to return appropriate error messages.