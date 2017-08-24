# TSP : Travel salesman problem
# Permutations algorithm
#
# Jirawat Yuktawathin
# start  : 9/8/2017
# finish : 23/8/2017
#
# Python version : 2.7

import matplotlib.pyplot as plt
from itertools import permutations
from random import randrange
import time

# Random points.
point = 5
x = [[], []]
y = [[], []]
for i in range(point):
    x[0].append(i + 1)
    x[1].append(randrange(0, 100))
    y[0].append(i + 1)
    y[1].append(randrange(0, 100))
#print(x)
#print(y)

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
#print(d_metrix)

# All of ways.
all_way = list(permutations(x[0]))
print(all_way)

# Create a graph
plt.ion()

fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(1, 2, 1)
line1, = ax1.plot(x[1], y[1], 'r--')
ax1.plot(x[1], y[1], 'ro')

ax2 = fig.add_subplot(1, 2, 2)
line2, = ax2.plot(x[1], y[1], 'b--')
ax2.plot(x[1], y[1], 'bo')

# Find the shortest way and graph update.
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
    line1.set_xdata(x_coord)
    line1.set_ydata(y_coord)

    x_coord_short = [x[1][k - 1] for k in (all_way[short] + (all_way[short][0],))]
    y_coord_short = [y[1][k - 1] for k in all_way[short] + (all_way[short][0],)]
    line2.set_xdata(x_coord_short)
    line2.set_ydata(y_coord_short)

    ax1.set_title('n = {} Distance = {}'.format(i + 1, d_total))
    ax2.set_title('Shortest distance = {}'.format(d_min))

    fig.canvas.draw()
    time.sleep(0.0001)

time.sleep(5)
#print(d_min)
#print(all_way[short])
