# Solve system of linear equations
# Cramer's rule
#
# Jirawat Yuktawatin
# start   : 23/8/2017
# update  : 25/8/2017
#
# Python version : 3.6

from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from numpy.linalg import det

total_eqn = int(input('Total equation: '))

# Get coefficients from equation.
eqn = []
for i in range(total_eqn):
    sub_eqn = []
    for j in range(total_eqn + 1):
        num = int(input('{}{}: '.format(ascii_lowercase[j], i + 1)))
        sub_eqn.append(num)
    eqn.append(sub_eqn)

# Calculate a determinant of initial metrix.
init_eqn = []
for i in range(total_eqn):
    init_eqn.append(eqn[i][:-1])
normal_eqn = det(init_eqn)

# Calculate a determinant of adaptive metrix.
for i in range(total_eqn):
    adapt_eqn = deepcopy(init_eqn)
    for j in range(total_eqn):
        adapt_eqn[j][i] = eqn[j][-1]

    print('{} = {:.2f}'.format(ascii_uppercase[i], det(adapt_eqn) / normal_eqn))
