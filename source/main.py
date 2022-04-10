import find_number_of_people
import load_csv as load_csv
import cli


def main():
    # TODO wywolac funkcje welcome z cli.py, wywolac funkcje get user input,
    name = cli.user_input("Hello. Put your name: ")
    print(cli.welcome(name))
    user_choice = cli.user_input("User choice is: ")
    matura = load_csv.load_csv("matura.csv")

    if user_choice == "1":
        print(
            "The result is: "
            + find_number_of_people.percent_of_passed(
                matura,
                region="Lubuskie",
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
    question = cli.user_input("Next searching ? yes or no: ")
    question = cli.quest(question)


if __name__ == "__main__":
    main()
