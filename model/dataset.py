import random

import numpy as np
from PIL import Image

from constants import HORNS, NO_HORNS, IMG_WIDTH, IMG_HEIGHT


class Dataset(object):
    def __init__(self, manifest, image_dir, num_samples=1000, training_split=0.8, mirror=False):
        self.image_dir = image_dir
        self.training_split = training_split
        self.data = []

        horns = [x for x in manifest if int(manifest[x]) == HORNS]
        no_horns = [x for x in manifest if int(manifest[x]) == NO_HORNS]

        # If num_samples was set too high, ensure we maintain a 50/50 ratio in our training data
        if len(horns) < num_samples:
            num_samples = len(horns)
        if len(no_horns) < num_samples:
            num_samples = len(no_horns)
        self.num_samples = num_samples

        horns = horns[0:num_samples]
        no_horns = no_horns[0:num_samples]

        self._add_images(horns, HORNS, mirror)
        self._add_images(no_horns, NO_HORNS, mirror)

        # If we include mirroring we'll double the number of samples here to account for the duplication. Hacky way
        # to do this but it saves work in the load_data logic
        if mirror:
            self.num_samples *= 2

        random.shuffle(self.data)

    def _add_images(self, image_names, image_label, mirror):
        for i in image_names:
            self.data.append(ImageArray(
                "{0}/{1}".format(self.image_dir, i),
                image_label
            ))

            if mirror:
                pass

    def load_data(self):
        data_size = len(self.data)
        training_size = int(data_size * self.training_split)

        train_img = np.stack([d.data for d in self.data[0:training_size]])
        train_label = np.stack([d.label for d in self.data[0:training_size]])
        test_img = np.stack([d.data for d in self.data[training_size:data_size]])
        test_label = np.stack([d.label for d in self.data[training_size:data_size]])

        train_img = train_img.reshape(train_img.shape[0], IMG_HEIGHT, IMG_WIDTH, 1)
        test_img = test_img.reshape(test_img.shape[0], IMG_HEIGHT, IMG_WIDTH, 1)

        return train_img, train_label, test_img, test_label


class ImageArray(object):
    def __init__(self, image_path, label):
        img = Image.open(image_path)
        self.data = np.array(img, dtype="float32") / 255
        self.label = label
