email = input("Enter your email: ")

k, j, d = 0, 0, 0

if len(email) >= 6:  # 1
    if email[0].isalpha():  # 2
        if "@" in email and email.count("@") == 1:  # 3
            if email[-4] == "." or email[-3] == ".":  # 4
                for i in email:
                    if i.isspace():  # 5
                        k = 1
                    elif i.isalpha():
                        if i.isupper():  # 5
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in ['_', '.', '@']:
                        continue
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:  # 5
                    print("Wrong Email: contains whitespace, uppercase letters, or invalid characters")
                else:
                    print("Right Email")

            else:
                print("Wrong Email: incorrect format")
        else:
            print("Wrong Email: invalid '@' placement or count")

    else:
        print("Wrong Email: must start with a letter")
else:
    print("Wrong Email: too short")
