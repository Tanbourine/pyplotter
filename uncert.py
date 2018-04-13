''' Basic math operations with uncertainties '''

from uncertainties import ufloat_fromstr


def add_uncertainty():
    ''' add two values together and find uncertainty'''
    input_value = get_input(2)
    output = input_value[0] + input_value[1]
    print(output)
    return output


def subtract_uncertainty():
    '''subtract two values together and find uncertainty'''
    input_value = get_input(2)
    output = input_value[0] - input_value[1]
    print(output)
    return output


def multiply_uncertainty():
    '''multiplies two values and find uncertainty'''
    input_value = get_input(2)
    output = input_value[0] * input_value[1]
    print(output)
    return output


def divide_uncertainty():
    '''divide two values and find uncertainty'''
    input_value = get_input(2)
    output = input_value[0] / input_value[1]
    print(output)
    return output


def square_uncertainty():
    '''squares value and find uncertainty'''
    input_value = get_input(1)
    output = input_value[0]**2
    print(output)
    return output


def get_input(num):
    ''' 
    Asks user for value and uncertainty
    Input = # of values to collect
    Output = Array of values formatted for uncertainty library
    '''

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
    add_uncertainty()
    # square_uncertainty()
    # multiply_uncertainty()


if __name__ == '__main__':
    main()
