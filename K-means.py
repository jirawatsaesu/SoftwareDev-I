# K-means clustering
#
# Jirawat Yuktawathin
# start  : 15/9/2017
# update : 22/9/2017
#
# Python version : 3.6

import matplotlib.pyplot as plt
from random import randrange
from copy import deepcopy


def k_means(data, k=2, centroid=None, cluster=None):
    # 1st round, Random a centroid.
    # 2nd rounds or more, Change a centroid.
    if not bool(centroid):
        cluster = [[] for i in range(k)]
        min_x = min(x for [x, y] in data)
        max_x = max(x for [x, y] in data) + 1
        min_y = min(y for [x, y] in data)
        max_y = max(y for [x, y] in data) + 1
        centroid = []
        for i in range(k):
            centroid.append([randrange(min_x, max_x), randrange(min_y, max_y)])

        # Plot raw data.
        for i in range(len(data)):
            x = [x for [x, y] in data]
            y = [y for [x, y] in data]
            plt.plot(x, y, 'mo', markersize=4)
        plt.pause(3)
        for i in range(k):
            x = [x for [x, y] in centroid]
            y = [y for [x, y] in centroid]
            plt.plot(x, y, 'rx', markersize=7)
        plt.pause(0.1)
        plt.clf()

    else:
        old_centroid = deepcopy(centroid)
        for i in range(k):
            try:
                means_x = sum(x for [x, y] in cluster[i]) / len(cluster[i])
                means_y = sum(y for [x, y] in cluster[i]) / len(cluster[i])
                centroid[i] = [means_x, means_y]
            except ZeroDivisionError:
                pass

        # Check centroid
        if old_centroid == centroid:
            plt.show()
            return centroid, cluster
        else:
            for i in range(k):
                for j in range(len(cluster[i])):
                    data.append(cluster[i].pop())

    # Change group
    for i in range(len(data)):
        for j in range(k):
            delta_x = centroid[j][0] - data[i][0]
            delta_y = centroid[j][1] - data[i][1]
            distance = (delta_x ** 2 + delta_y ** 2) ** 0.5
            if j == 0:
                min_distance = distance
                group = j
            elif distance < min_distance:
                min_distance = distance
                group = j
        cluster[group].append(data[i])

    # Plot an update data.
    for i in range(k):
        x = [x for [x, y] in cluster[i]]
        y = [y for [x, y] in cluster[i]]
        plt.plot(x, y, 'o', markersize=4)
    for i in range(k):
        x = [x for [x, y] in centroid]
        y = [y for [x, y] in centroid]
        plt.plot(x, y, 'rx', markersize=7)
    plt.pause(0.01)
    plt.clf()

    return k_means([], k, centroid, cluster)

point = 1000
coord = [[randrange(point), randrange(point)] for i in range(point)]
print(k_means(coord, 6))
