'''testing out uncertainties module'''

from uncertainties import ufloat_fromstr


def multiply_uncertainty():
    '''multiplies two values and find uncertainty'''
    input_x = get_input()
    input_y = get_input()
    output = input_x * input_y
    print(output)
    return output


def square_uncertainty():
    '''squares value and find uncertainty'''
    input_x = get_input()
    output = input_x**2
    print(output)
    return output


def get_input():
    '''get user input and format to uncertainty'''
    user_input_main = input('Input main value >>> ')
    user_input_uncertainty = input('Input uncertainty value >>> ')
    input_value = ufloat_fromstr(
        user_input_main + '+/-' + user_input_uncertainty)
    return input_value


def main():
    ''' main function '''
    square_uncertainty()
    multiply_uncertainty()


if __name__ == '__main__':
    main()
