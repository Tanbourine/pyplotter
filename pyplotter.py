"""pyplotter.py
used to plot pies
"""
import csv
import numpy as np
import matplotlib.pyplot as plt


def main():
    ''' main function '''
    datafile = 'data.csv'
    x_data = []
    y_data = []
    yerr = []

    with open(datafile) as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            x_data.append(float(row[0]))
            y_data.append(float(row[1]))
            yerr.append(float(row[2]))

    np.asarray(x_data)
    np.asarray(y_data)
    np.asarray(yerr)

# ======= Plotting ========
    plt.figure()
    plt.errorbar(x_data, y_data, yerr=yerr)
    plt.title("Simple Errorbars")
    plt.plot(x_data, y_data)
    plt.legend(['A simple error bar'])
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
