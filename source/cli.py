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


def search(user_choice):
    if user_choice == "1":
        region_of_Poland = user_input("Put region: ")
        year_of_exam = user_input("Put year: ")
        print(
            "The result is: "
            + str(
                find_number_of_people.proceed_in_year(
                    matura,
                    passs="przystąpiło",
                    region=region_of_Poland,
                    year=year_of_exam,
                )
            )
        )
    elif user_choice == "2":
        region_of_Poland = user_input("Put region: ")
        print(
            "The result is: "
            + str(
                find_number_of_people.proceed_all_years(
                    matura,
                    passs="przystąpiło",
                    region=region_of_Poland,
                    year="all",
                    sex="both",
                )
            )
        )
    elif user_choice == "3":
        region_of_Poland = user_input("Put region: ")

        print(
            "The result is: "
            + str(
                find_number_of_people.number_of_people_who_passed(
                    matura,
                    passs="zdało",
                    region=region_of_Poland,
                    year="all",
                    sex="both",
                )
            )
        )
    elif user_choice == "4":
        region_of_Poland = user_input("Put region: ")

        print(
            "The result is: "
            + str(
                find_number_of_people.percent_of_passed(
                    matura,
                    region=region_of_Poland,
                    year="all",
                    sex="both",
                )
            )
        )
