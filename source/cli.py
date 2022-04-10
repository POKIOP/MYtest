# import argparse
import find_number_of_people


# def get_parser():
#     parser = argparse.ArgumentParser(description="This program shows you data about results of exams")
#     parser.add_argument("--name", type=str, help="Put your name")
#     args = parser.parse_args()
#     return args


def welcome(name):
    """Returns welcome text

    Args:
        name (str): Put your name

    Returns:
        str: welcome text
    """
    return f"""Welcome in my program {name}.
    Choose the option:
                1 (Percent of passed)
                2 ()
                3
                4
                5."""


def user_input(text_to_show="Provide text: "):
    value = input(text_to_show)
    return value


def quest(question):
    if question == ("no"):
        print("Thank you and goodbye.")
    # else:
    #     print("What is your name ?")


if __name__ == "__main__":
    args = get_parser()
    print(welcome(args.name))
    print(find_number_of_people.proceed_all_years.__doc__)
