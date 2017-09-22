# TSP : Travel salesman problem
# Permutations algorithm
#
# Jirawat Yuktawathin
# start  : 9/8/2017
# finish : 22/9/2017
#
# Python version : 3.6

import matplotlib.pyplot as plt
from itertools import permutations
from random import randrange

point = 5
x = [[i + 1 for i in range(point)], [randrange(100) for i in range(point)]]
y = [[i + 1 for i in range(point)], [randrange(100) for i in range(point)]]

# Metrix of distances.
d_metrix = [None] * (point * (point - 1))
i = 0
j = 0
while i < point:
    j = i + 1
    while j < point:
        delta_x = x[1][i] - x[1][j]
        delta_y = y[1][i] - y[1][j]
        distance = (delta_x ** 2 + delta_y ** 2) ** 0.5
        d_metrix[((i + 1) * (j + 1)) - 1] = distance
        j += 1
    i += 1

# All of ways.
all_way = list(permutations(x[0]))

# Create a graph
plt.figure(figsize=(10, 6))
ax1 = plt.subplot(1, 2, 1)
ax2 = plt.subplot(1, 2, 2)

# Find the shortest way then update graph.
for i in range(len(all_way)):
    d_total = 0
    for j in range(len(all_way[i])):
        position = (all_way[i][j] * all_way[i][j - 1]) - 1
        d_total += d_metrix[position]
    if i == 0:
        d_min = d_total
        short = i
    elif d_total < d_min:
        d_min = d_total
        short = i

    x_coord = [x[1][k - 1] for k in (all_way[i] + (all_way[i][0],))]
    y_coord = [y[1][k - 1] for k in (all_way[i] + (all_way[i][0],))]
    ax1.plot(x[1], y[1], 'ro')
    ax1.plot(x_coord, y_coord, 'r--')
    ax1.set_title('n = {} Distance = {}'.format(i + 1, d_total))

    x_coord_short = [x[1][k - 1] for k in (all_way[short] + (all_way[short][0],))]
    y_coord_short = [y[1][k - 1] for k in all_way[short] + (all_way[short][0],)]
    ax2.plot(x[1], y[1], 'bo')
    ax2.plot(x_coord_short, y_coord_short, 'b--')
    ax2.set_title('Shortest distance = {}'.format(d_min))

    plt.pause(0.01)
    ax1.cla()
    ax2.cla()
plt.show()
