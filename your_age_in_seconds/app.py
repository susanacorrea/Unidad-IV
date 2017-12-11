__author__ = 'Alfredo y Susy'


def age_program():
    seconds_or_years = input("Will you give me seconds (s) or years (y)?")
    if seconds_or_years == "s":
        # Convert seconds to years
        user_value = input("Enter the number of seconds you've lived for: ")
        print("You've lived for {} years".format(int(user_value) / 60 / 60 / 24 / 3654))
    elif seconds_or_years == "y":
        # Convert years to seconds
        user_value = input("Enter the number of years you've lived for: ")
        print("You've lived for {} seconds".format(int(user_value) * 365 * 24 * 60 * 60))


age_program()
