# Solve system of linear equations
# Gaussian's rule
#
# Jirawat Yuktawatin
# start   : 23/8/2017
# finish  : 1/9/2017
#
# Python version : 3.6.1

from string import ascii_lowercase, ascii_uppercase

total_eqn = int(input('Total equation: '))

# Get coefficients from equation.
eqn = []
for i in range(total_eqn):
    sub_eqn = []
    for j in range(total_eqn + 1):
        num = int(input('{}{}: '.format(ascii_lowercase[j], i + 1)))
        sub_eqn.append(num)
    eqn.append(sub_eqn)
#print(eqn)

for i in range(total_eqn):

    # Division.
    for row in range(i, total_eqn):
        num = eqn[row][i]
        for column in range(i, total_eqn + 1):
            eqn[row][column] /= num
    #print('division', eqn)

    # Minus.
    for row in range(total_eqn):
        for column in range(total_eqn + 1):
            if row <= i:
                pass
            else:
                num = eqn[i][column]
                eqn[row][column] -= num
    #print('minus', eqn)

# Minus.
for i in range(total_eqn - 1):
    for j in range(i, total_eqn - i):
        num = eqn[i][i + j]
        #print(num)
        for column in range(total_eqn + 1):
            if i + j == 0:
                continue
            eqn[i][column] -= eqn[i + j][column] * num
            #print(eqn)
    #print(eqn)

# Show out.
for i in range(total_eqn):
    print('{} = {}'.format(ascii_uppercase[i], eqn[i][-1]))