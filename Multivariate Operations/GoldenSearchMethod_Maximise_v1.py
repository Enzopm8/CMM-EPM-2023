import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time

# Summary: Golden Section Search Algorithm
# This script defines a function to perform the golden section search 
# to find the maximum or minimum of a given function within a specified 
# range with a specified tolerance.

# Objective function
def func_fx(x):
    # The objective function to be optimized.
    fx = 2 * np.sin(x) - (x**2 / 10)
    return fx

# Check position helper function
def check_pos(x1, x2):
    # Checks the position of x2 relative to x1.
    if x2 < x1:
        label = 'right'
    else:
        label = ''
    return label

# Update interior points helper function
def update_interior(xl, xu):
    # Updates the interior points based on the golden section.
    d = ((np.sqrt(5) - 1) / 2) * (xu - xl)
    x1 = xl + d
    x2 = xu - d
    return x1, x2

# Find maximum helper function
def find_max(xl, xu, x1, x2, label):
    # Finds the maximum within the given range.
    fx1 = func_fx(x1)
    fx2 = func_fx(x2)
    if fx2 > fx1 and label == 'right':
        xl = xl
        xu = x1
        new_x = update_interior(xl, xu)
        x1 = new_x[0]
        x2 = new_x[1]
        xopt = x2
    else:
        xl = x2
        xu = xu
        new_x = update_interior(xl, xu)
        x1 = new_x[0]
        x2 = new_x[1]
        xopt = x1
    return xl, xu, xopt

# Plotting function
def plot_graph(xl, xu, x1, x2):
    clear_output(wait=True)

    # Plotting sine graph
    plt.plot(x, y)
    plt.plot([0, 3], [0, 0], 'k')

    # Plotting x1 point
    plt.plot(x1, func_fx(x1), 'ro', label='x1')
    plt.plot([x1, x1], [0, func_fx(x1)], 'k')

    # Plotting x2 point
    plt.plot(x2, func_fx(x2), 'bo', label='x2')
    plt.plot([x2, x2], [0, func_fx(x2)], 'k')

    # Plotting xl line
    plt.plot([xl, xl], [0, func_fx(xl)])
    plt.annotate('xl', xy=(xl - 0.01, -0.2))

    # Plotting xu line
    plt.plot([xu, xu], [0, func_fx(xu)])
    plt.annotate('xu', xy=(xu - 0.01, -0.2))

    # Plotting x1 line
    plt.plot([x1, x1], [0, func_fx(x1)], 'k')
    plt.annotate('x1', xy=(x1 - 0.01, -0.2))

    # Plotting x2 line
    plt.plot([x2, x2], [0, func_fx(x2)], 'k')
    plt.annotate('x2', xy=(x2 - 0.01, -0.2))

    # y-axis limit
    plt.ylim([0, 2.5])
    plt.show()

# Golden Section Search function
def golden_search(xl, xu, mode, et):
    it = 0
    e = 1
    while e >= et:
        new_x = update_interior(xl, xu)
        x1 = new_x[0]
        x2 = new_x[1]
        fx1 = func_fx(x1)
        fx2 = func_fx(x2)
        label = check_pos(x1, x2)
        clear_output(wait=True)
        plot_graph(xl, xu, x1, x2)  # PLOTTING
        plt.show()

        # SELECTING AND UPDATING BOUNDARY-INTERIOR POINTS
        if mode == 'max':
            new_boundary = find_max(xl, xu, x1, x2, label)
        else:
            print('Please define min or max mode')
            break  # exit if mode not min or max
        xl = new_boundary[0]
        xu = new_boundary[1]
        xopt = new_boundary[2]

        it += 1
        print('Iteration: ', it)
        r = (np.sqrt(5) - 1) / 2  # GOLDEN RATIO
        e = ((1 - r) * (abs((xu - xl) / xopt))) * 100  # Error
        print('Error:', e)
        time.sleep(1)

        print(xopt, func_fx(xopt))

# Generate points for sine graph
x = np.linspace(0, 3, 100)
y = func_fx(x)

# EXECUTING GOLDEN SEARCH FUNCTION
golden_search(0, 6, 'max', 0.05)
