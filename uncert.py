''' Basic math operations with uncertainties '''

from uncertainties import ufloat_fromstr


def format_output(output):
    ''' formats output string to be pleasing to the eye'''
    print('')
    print('==============')
    print(output)
    print('==============')
    print('')


def add_uncertainty():
    ''' add two values together and find uncertainty'''
    print("Adding two values with uncertainties")
    input_value = get_input(2)
    output = input_value[0] + input_value[1]
    format_output(output)
    return output


def subtract_uncertainty():
    '''subtract two values together and find uncertainty'''
    print("Subtracting two values with uncertainties")
    input_value = get_input(2)
    output = input_value[0] - input_value[1]
    format_output(output)
    return output


def multiply_uncertainty():
    '''multiplies two values and find uncertainty'''
    print("Multiplying two values with uncertainties")
    input_value = get_input(2)
    output = input_value[0] * input_value[1]
    format_output(output)
    return output


def divide_uncertainty():
    '''divide two values and find uncertainty'''
    print("Dividing two values with uncertainties")
    input_value = get_input(2)
    output = input_value[0] / input_value[1]
    format_output(output)
    return output


def square_uncertainty():
    '''squares value and find uncertainty'''
    print("Square a value with uncertainties")
    input_value = get_input(1)
    output = input_value[0]**2
    format_output(output)
    return output


def get_input(num):
    """ Asks user for value and uncertainty
    Input = # of values to collect
    Output = Array of values formatted for uncertainty library
    """

    input_value = []
    for i in range(1, num+1):
        user_input_value = input('Input value ' + str(i) + ' >>> ')
        user_input_uncertainty = input(
            'Input uncertainty value ' + str(i) + ' >>> ')
        input_value.append(ufloat_fromstr(
            user_input_value + '+/-' + user_input_uncertainty))
    return input_value


def main():
    ''' main function '''

    flag = 'true'
    while flag in ['true', 'yes', 'y', 'yup', 'yessir', 'yeah', '', ' ']:
        operation = input('Which operation would you like to perform? >>> ')
        operation = operation.lower()

        if operation in ['add', 'addition', 'plus', 'a']:
            add_uncertainty()

        elif operation in ['subtract', 'minus', 'less', 's']:
            subtract_uncertainty()

        elif operation in ['multiply', 'mult', 'times', 'm']:
            multiply_uncertainty()

        elif operation in ['divide', 'div', 'd']:
            divide_uncertainty()

        elif operation in ['square', 'exp', 'exponent']:
            square_uncertainty()

        elif operation in ['no', 'cancel', 'n']:
            print('Canceling')
            quit()

        else:
            print('Invalid input')

        flag = input('Continue? >>> ')
        flag = flag.lower()


if __name__ == '__main__':
    main()
