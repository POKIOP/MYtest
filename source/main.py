import cli


def main():
    name = cli.user_input("Hello. Put your name: ")
    print(cli.welcome(name))
    user_choice = cli.user_input("User choice is: ")
    cli.search(user_choice)
    question = cli.user_input("Next searching ? yes or no: ")
    question = cli.quest(question)


if __name__ == "__main__":
    main()
