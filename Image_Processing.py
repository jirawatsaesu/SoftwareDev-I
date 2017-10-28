# Image Processing by K-means clustering
#
# Jirawat Yuktawathin
# start  : 19/9/2017
# update : 20/9/2017
#
# Python version : 3.6

from PIL import Image
from copy import deepcopy


def k_means(data, k=2, centroid=None, cluster=None):
    # 1st round, Random a centroid.
    # 2nd rounds or more, Change a centroid.
    if not bool(centroid):
        cluster = [[] for i in range(k)]
        min_x = min(x for [x, y, z, *arg] in data)
        max_x = max(x for [x, y, z, *arg] in data) + 1
        min_y = min(y for [x, y, z, *arg] in data)
        max_y = max(y for [x, y, z, *arg] in data) + 1
        min_z = min(z for [x, y, z, *arg] in data)
        max_z = max(z for [x, y, z, *arg] in data) + 1
        centroid = []
        for i in range(k):
            centroid.append([(min_x + max_x) / 2, (min_y + max_y) / 2,\
                             (min_z + max_z) / 2])
    else:
        old_centroid = deepcopy(centroid)
        for i in range(k):
            try:
                means_x = sum(x for [x, y, z, *arg] in cluster[i]) / len(cluster[i])
                means_y = sum(y for [x, y, z, *arg] in cluster[i]) / len(cluster[i])
                means_z = sum(z for [x, y, z, *arg] in cluster[i]) / len(cluster[i])
                centroid[i] = [means_x, means_y, means_z]
            except ZeroDivisionError:
                pass

        # Check centroid
        if old_centroid == centroid:
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
            delta_z = centroid[j][2] - data[i][2]
            distance = (delta_x ** 2 + delta_y ** 2 + delta_z ** 2) ** 0.5
            if j == 0:
                min_distance = distance
                group = j
            elif distance < min_distance:
                min_distance = distance
                group = j
        cluster[group].append(data[i])

    return k_means([], k, centroid, cluster)


def mod_img(pic, color, mod_pic):
    # Image read.
    print('Image read...')
    img = Image.open(pic)
    px = img.load()
    rgb = []
    x_max, y_max = img.size
    for px_x in range(x_max):
        for px_y in range(y_max):
            rgb.append(px[px_x, px_y] + (px_x, px_y))

    # K-means clustering
    print('clustering...')
    centroid, cluster = k_means(rgb, color)

    # Change color.
    print('Save a new file...')
    for i in range(len(centroid)):
        for j in range(len(cluster[i])):
            px[cluster[i][j][-2], cluster[i][j][-1]] =\
                (int(centroid[i][0]), int(centroid[i][1]), int(centroid[i][2]))
    img.save(mod_pic)
    return 'Complete!'

mod_img('pic.jpg', 8, 'modified_8.jpg')
