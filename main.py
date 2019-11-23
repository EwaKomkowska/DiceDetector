from skimage import io, measure, img_as_float
import matplotlib.pyplot as plt
import cv2
import numpy as np
from scipy import ndimage


def thresh(number, threshpoint):
    if number < threshpoint:
        return 0
    else:
        return 1


def gamma(img):
    g = np.mean(img)
    return img**g


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
    work = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    _, work = cv2.threshold(work, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    contour_array, _ = cv2.findContours(work, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    contours = []

    #Weź kontury dłuższe niż ileś tam pikseli
    for xD in contour_array:
        if cv2.contourArea(xD) > 60:
            contours.append(xD)

    cv2.drawContours(photo, contours, -1, (0, 255, 0), 3)

    return photo


#  ][\\    //][       //\\       ][   ][\\    ][
#  ][ \\  // ][      //  \\      ][   ][ \\   ][
#  ][  \\//  ][     //====\\     ][   ][  \\  ][
#  ][        ][    //      \\    ][   ][   \\ ][
#  ][        ][   //        \\   ][   ][    \\][

if __name__ == '__main__':
    filenames = []

    for i in range(1, 12):
        filenames.append(str(i))

    filenames.append("kostka")

    images = [cv2.imread('./data/' + i + '.jpg') for i in filenames]

    for i in range(0, len(filenames)):
        plt.clf()
        io.imshow(prepare_photo(images[i]))
        plt.savefig('./Preprocessed/' + filenames[i] + '.png')
