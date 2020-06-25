"""
Some codes from https://github.com/Newmu/dcgan_code
"""
import os

import scipy.misc
import math
import pprint
import numpy as np
from PIL import Image

pp = pprint.PrettyPrinter()

get_stddev = lambda x, k_h, k_w: 1 / math.sqrt(k_w * k_h * x.get_shape()[-1])


def get_image(image_path, image_size=(), need_transform=False):
    if need_transform:
        return transform(imread(image_path), image_size)
    else:
        return imread(image_path)


def save_images_to_one(images, size, image_path):
    return imsave(inverse_transform(images), size, image_path)


def imread(path):
    # print(path)
    img = scipy.misc.imread(path)
    # print(img)
    # print(type(img))
    img = img.astype(np.float)
    # print(img)
    img_shape = list(img.shape)
    if len(img_shape) == 2:
        img_shape.append(1)
        img = img.reshape(img_shape)
    return img
    # print(np.asarray(Image.open(path)))
    # return np.asarray(Image.open(path))


def imsave(images, size, path):
    h, w = images.shape[1], images.shape[2]
    img = np.zeros((h * size[0], w * size[1], 3))

    for idx, image in enumerate(images):
        i = int(idx % size[1])
        j = int(idx / size[1])
        img[j*h:j*h+h, i*w:i*w+w, :] = image
    return scipy.misc.imsave(path, img)


def save_images(images, i, folder):
    for idx, image in enumerate(inverse_transform(images)):
        scipy.misc.imsave(os.path.join(folder, '%s.png' % (i * idx)), image)


def center_crop(x, crop_h, crop_w=None, resize_w=64):
    if crop_w is None:
        crop_w = crop_h
    h, w = x.shape[:2]
    j = int(round((h - crop_h) / 2.))
    i = int(round((w - crop_w) / 2.))
    return scipy.misc.imresize(x[j:j + crop_h, i:i + crop_w],
                               [resize_w, resize_w])


def transform(image, npx=64):
    # npx : # of pixels width/height of image
    cropped_image = center_crop(image, npx)
    return np.array(cropped_image) / 127.5 - 1.


def inverse_transform(images):
    return (images + 1.) / 2.
