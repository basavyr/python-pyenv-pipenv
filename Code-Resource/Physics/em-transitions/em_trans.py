#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

HBAR = 1.0

# set the imaginary unit to one
II = 1.0


def homega(omega_0):
    energy = HBAR * omega_0
    return energy


def Create_T(t_sup):
    step = 0.1
    return np.arange(0, t_sup, step)


def Nucleus_Wave_Function(psi_r, E0, t_sup):
    """
    Evaluates the nuclear wave-function based on the initial energy of the state.
    The nuclear wave-function is computed within the time interval [0,t_sup]
    """

    # initialize the t-values
    t_values = Create_T(t_sup)

    exp_t = lambda t: np.exp(-II * E0 * t / HBAR)

    # compute the wave-function

    psi_t = list(map(exp_t, t_values))

    PSI_RT = [psi_r * psi_t[i] for i in range(len(psi_t))]

    return PSI_RT


psi_r = 1.12
E0 = 2.5
t_sup = 2

T_VALUES = Create_T(t_sup)
PSI_RT = Nucleus_Wave_Function(psi_r, E0, t_sup)

plt.plot(T_VALUES, PSI_RT, '-ob', label='Nuclear Wave-Function')
plt.legend(loc='best')
plt.xlabel('t [s]')
plt.ylabel(r'$\Psi(r,t)$')
plt.savefig('Nuclear_Wave_Function.png', bbox_inches='tight')
plt.close()
