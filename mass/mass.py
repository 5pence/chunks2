import argparse

""" Complete create_parser below so that our BMI program can be called like this:

$ python bmi.py -h
usage: bmi.py [-h] [-w WEIGHT] [-l LENGTH]

Calculate your BMI.

optional arguments:
  -h, --help            show this help message and exit
  -w WEIGHT, --weight WEIGHT
                        Your weight in kg
  -l LENGTH, --length LENGTH
                        Your length in cm

$ python bmi.py -w 80 -l 187
Your BMI is: 22.88

Please note that calc_bmi and handle_args are given, you only need to code create_parser!
"""

def calc_bmi(weight, length):
    """Provided/DONE:
       Calc BMI give a weight in kg and length in cm, return the BMI
       rounded on 2 decimals"""
    bmi = int(weight) / ((int(length) / 100) ** 2)
    return round(bmi, 2)


def create_parser():
    """TODO:
       Create an ArgumentParser adding the right arguments to pass the tests,
       returns a argparse.ArgumentParser object"""


def handle_args(args=None):
    """Provided/DONE:
       Call calc_bmi with provided args object.
       If args are not provided get them from create_parser"""
    if args is None:
        parser = create_parser()
        args = parser.parse_args()

    if args.weight and args.length:
        bmi = calc_bmi(args.weight, args.length)
        print(f'Your BMI is: {bmi}')
    else:
        raise SystemExit


if __name__ == '__main__':
    handle_args()