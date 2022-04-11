from unicodedata import name
import find_number_of_people
import load_csv as load_csv

matura = load_csv.load_csv("matura.csv")


def welcome(name):
    return f"""Welcome in my program {name}.
    What do you want to know ? Choose the option:
                1. People who proceed in particular year.
                2. People who proceed in all years.
                3. Number of people who passed in particular year.
                4. Percent of people who passed"""


def user_input(text_to_show):
    value = input(text_to_show)
    return value


def quest(question):
    if question == ("no"):
        print("Thank you and goodbye.")
    else:
        welcome(name)


def search(user_choice):
    if user_choice == "1":
        region_of_Poland = user_input("Put region: ")
        year_of_exam = user_input("Put year: ")
        print(
            "The result is: "
            + str(
                find_number_of_people.proceed_in_year(
                    matura,
                    passs="zdało",
                    region=region_of_Poland,
                    year=year_of_exam,
                )
            )
        )
    elif user_choice == "2":
        print(
            "The result is: "
            + str(
                find_number_of_people.proceed_in_year(
                    matura,
                    passs="zdało",
                    region="Lubuskie",
                    year="2018",
                )
            )
        )
    elif user_choice == "3":
        print(
            find_number_of_people.proceed_all_years(
                matura,
                passs="zdało",
                region="Lubuskie",
                year="2018",
                sex="kobiety",
            )
        )
