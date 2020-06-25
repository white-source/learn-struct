import sys
import os
import pickle
import numpy as np
import matplotlib.pyplot as plt
import random

# sys.path.insert(0, os.path.join(
#    os.path.dirname(os.path.abspath(__file__)), "git", "models", "tutorials"))
#import tensorflow as tf


def get_data(path, file):
    with open(os.path.join(path, file), 'rb') as fo:
        dict_obj = pickle.load(fo, encoding='bytes')
    X = np.asarray(dict_obj[b'data'].T).astype("uint8")
    Y = np.asarray(dict_obj[b'labels'])
    names = np.asarray(dict_obj[b'filenames'])
    return X, Y, names


def show_image(X, Y, names, id):
    rgb = X[:, id]
    img = rgb.reshape(3, 32, 32).transpose([1, 2, 0])
    plt.imshow(img)
    plt.title("%s with label %s" % (names[id], Y[id]))
    plt.show()


if __name__ == '__main__':
    import getopt

    data_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data-cifar10")

    X, Y, names = get_data(data_dir, 'data_batch_1')
    show_image(X, Y, names, random.randint(1, 10000))
