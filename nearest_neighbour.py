# TSP : Travel salesman problem
# Berlin 52
# Nearest neighbour (NN) algorithm
#
# Jirawat Yuktawathin
# 17/8/2017

import matplotlib.pyplot as plt

file = open("Berlin52")
coord = []

for line in file:
    x = float(line.split()[1])
    y = float(line.split()[2])
    coord.append([x, y])
file.close()

x_coord = [coord[0][0]]
y_coord = [coord[0][1]]

def NN(coord):
    '''
    The nearest neighbour (NN) algorithm (a greedy algorithm) lets the salesman
    choose the nearest unvisited city as his next move.
    '''
    all_distance = []
    if len(coord) == 1:
        return

    # Find a distance of all coordinate.
    for i in range(1, len(coord)):
        delta_x = coord[0][0] - coord[i][0]
        delta_y = coord[0][1] - coord[i][1]
        distance = (delta_x ** 2 + delta_y ** 2) ** 0.5
        all_distance.append([distance, i])

    # Next move, Choose a shortest way.
    x, y = coord[min(all_distance)[1]]
    coord[0] = coord[min(all_distance)[1]]
    coord.pop(min(all_distance)[1])
    x_coord.append(x)
    y_coord.append(y)
    NN(coord)

NN(coord)

# Find all distance.
total = 0
for i in range(len(x_coord)):
    delta_x = x_coord[i] - x_coord[i - 1]
    delta_y = y_coord[i] - y_coord[i - 1]
    distance = (delta_x ** 2 + delta_y ** 2) ** 0.5
    total += distance

plt.plot(x_coord + [x_coord[0]], y_coord + [y_coord[0]], '.', color = 'brown')
plt.plot(x_coord + [x_coord[0]], y_coord + [y_coord[0]], '--', color = 'orange')
plt.title('Distance = {:.3f}'.format(total))
plt.show()