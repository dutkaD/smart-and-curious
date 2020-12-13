def check_age(age):
    print("Checking age...")
    if age >= 17:
        print("You are allowed to watch this movie")
    else:
        if age > 12 and age < 17:
            print("We need a permission form your parents")
        else:
            print("You are not allowed to watch this movie")


def check_age_less_code(age):
    print("Checking age...")
    if age >= 17:
        print("You are allowed to watch this movie")
    elif 12 < age < 17:
        print("We need a permission form your parents")
    else:
        print("You are not allowed to watch this movie")


check_age(17)
check_age_less_code(17)

