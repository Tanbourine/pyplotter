'''testing out uncertainties module'''

from uncertainties import ufloat_fromstr
from uncertainties.umath import *


def multiply_uncertainty(input_value):
    '''multiplies two values to find uncertainty'''
    user_input_main = input('Input main value >>> ')
    user_input_uncertainty = input('Input uncertainty value >>> ')
    input_value = ufloat_fromstr(
        user_input_main + '+/-' + user_input_uncertainty)


def main():
    user_input_main = input('Input main value >>> ')
    user_input_uncertainty = input('Input uncertainty value >>> ')
    input_value = ufloat_fromstr(user_input_main + '+/-' +
                                 user_input_uncertainty)
    square = input_value**2
    print("this is uncertainty squared >>> ", square)

if __name__ == '__main__':
    main()
