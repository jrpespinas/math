"""Riemann Sums: Intro to Numerical Analysis"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '2.0.0'
__author__: 'Jan Rodolf Espinas'

import numpy as np
import matplotlib.pyplot as plt 
import error_analysis as ea
import argparse

def get_delta_x(lower_bound, upper_bound, n):
    return (upper_bound-lower_bound) / n

def f(x):
    return x**2

def get_riemann_sum(x, delta_x):
    """
    Returns the riemann `sum` given a `function` and 
    the input `x` and `delta_x`

    Parameters
    ----------
    x : list
        List of numbers returned by `np.linspace` given a lower
        and upper bound, and the number of intervals
    delta_x : 
        The interval
        
    Returns
    -------
    float
       The integral sum
    """
    return sum(f(x)*delta_x)

def riemann_integral(lower_bound,upper_bound,subintervals):
    """
    Shows the plot of the riemann sum given a `function` and 
    the input `x` and `delta_x`

    Parameters
    ----------
    x : list
        List of numbers returned by `np.linspace` given a lower
        and upper bound, and the number of intervals
    n : 
        The interval
        
    Returns
    -------
    float
       The integral sum
    """

    fig=plt.figure()
    for i in range(len(subintervals)):
        x = np.linspace(lower_bound,upper_bound,subintervals[i],endpoint=False)
        delta_x = get_delta_x(lower_bound,upper_bound,subintervals[i])
        riemann_sum = get_riemann_sum(x,delta_x)
        y=f(x)
        dims = 221+i
        plt.subplot(dims)
        plt.plot(x, y, color='C0')
        plt.bar(
            x, y, color="C"+str(i), 
            width=(upper_bound-lower_bound)/subintervals[i], 
            alpha=0.2, align='edge', edgecolor="C"+str(i),
            label = f"{riemann_sum}")
        plt.title(f'N = {subintervals[i]}')
        plt.grid()
        plt.legend()

    fig.suptitle(r"Riemann Integral of $x^2$")
    plt.show()

    
if __name__ == '__main__':

    # Type in the command line:
    # python3 numerical_analysis/riemann_sum.py -lb 0 -ub 5 -sub 10 20 50 100 
    
    parser = argparse.ArgumentParser(description="Riemann Integrals")
    parser.add_argument(
        '-lb', 
        '--LOWER_BOUND', 
        type=int,
        help='Lower Bound'
    )
    parser.add_argument(
        '-ub', 
        '--UPPER_BOUND', 
        type=int,
        help='Upper Bound'
    )
    parser.add_argument(
        '-sub', 
        '--SUBINTERVALS',
        nargs='+', 
        type=int,
        help='Subintervals'
    )
    args = vars(parser.parse_args())

    LOWER_BOUND = args['LOWER_BOUND']
    UPPER_BOUND = args['UPPER_BOUND']
    SUBINTERVALS = args['SUBINTERVALS']

    if len(SUBINTERVALS) == 4:
        riemann_integral(LOWER_BOUND,UPPER_BOUND,SUBINTERVALS)
    else:
        print("input only four subintervals")
