# should_continue = True
# if should_continue:
#     print("Hello")
#
# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")
#
# if person in known_people:
#     print("You know {}!".format(person))
# else:
#     print("You don't know {}!".format(person))


## Exercise

def who_do_you_know():
    # Ask the user for a list of people they know
    people = input("Enter the names of people you know, separated by commas: ")

    # Split the string into a list
    people_list = people.split(',')

    people_without_spaces = []
    for person in people_list:
        people_without_spaces.append(person.strip())

    # Return that list
    return people_without_spaces

def ask_user():
    # Ask user for a name
    person = input("Enter a name of someone you know: ")

    # See if their name is in the list of people they know
    if person in who_do_you_know():
        print("You know {}".format(person))
    else:
        print("You don't know {}".format(person))

ask_user()

