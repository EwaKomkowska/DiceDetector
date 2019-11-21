from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import skimage.morphology as mp


def thresh(number, threshpoint):
    if number < threshpoint:
        return 0
    else:
        return 1


def gamma(img):
    g = np.mean(img)
    return (img**g)


def contrast(img):
    percmin = 0.3
    percmax = 2.0
    MIN = np.percentile(img, percmin)
    MAX = np.percentile(img, 100-percmax)
    norm = (img - MIN) / (MAX - MIN)
    norm[norm[:, :] > 1] = 1
    norm[norm[:, :] < 0] = 0
    return norm


def prepare_photo(photo):
    photo = gamma(photo)
    # photo = gamma(photo)
    #
    # photo = contrast(photo)

    return photo


image = io.imread("./data/kostka.jpg", as_gray=True)
io.imshow(prepare_photo(image))

plt.show()
