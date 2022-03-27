import argparse
import find_number_of_people


parser = argparse.ArgumentParser(
    description="This program shows you data about results of exams"
)
parser.add_argument("--name", type=str, help="Put your name")
args = parser.parse_args()


def welcome(name):
    """Returns welcome text

    Args:
        name (str): Put your name

    Returns:
        [str]: welcome text
    """
    return f"Welcome in my program {name}. Choose the option."


if __name__ == "__main__":
    print(welcome(args.name))
    print(find_number_of_people.proceed_all_years.__doc__)
