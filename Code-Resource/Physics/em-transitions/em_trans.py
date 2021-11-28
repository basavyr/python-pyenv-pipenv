#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

HBAR = 1.0

# set the imaginary unit to one
II = 1.0


def homega(omega_0):
    energy = HBAR * omega_0
    return energy


def Nucleus_Wave_Function(psi_r, E0, t_sup):
    """
    Evaluates the nuclear wave-function based on the initial energy of the state.
    The nuclear wave-function is computed within the time interval [0,t_sup]
    """

    # initialize the t-values
    t_values = np.arange(0, t_sup, 0.1)

    exp_t = lambda t: np.exp(-II * E0 * t / HBAR)

    # compute the wave-function

    psi_t = list(map(exp_t, t_values))

    return psi_t


print(Nucleus_Wave_Function(1, 1.25, 1))
