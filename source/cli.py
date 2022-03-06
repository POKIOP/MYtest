import argparse

parser=argparse.ArgumentParser(description='This program shows you data about people, who proceeded and passed to school leaving exam, in years 2010 - 2019 in all regions of Poland')
parser.add_argument('--name', type=str, help='Put your name')
args=parser.parse_args()


def welcome(name):
    """Returns welcome text

    Args:
        name (str): Put your name

    Returns:
        [str]: welcome text
    """
    return 'Welcome in my program ' + name + '. Choose the option'

if __name__ == '__main__':
    print(welcome(args.name))