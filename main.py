from skimage import io
import matplotlib.pyplot as plt
import cv2
import numpy as np


def gamma(img):
    g = np.mean(img)
    return img ** g


def contrast(img):
    percmin = 0.3
    percmax = 2.0
    MIN = np.percentile(img, percmin)
    MAX = np.percentile(img, 100 - percmax)
    norm = (img - MIN) / (MAX - MIN)
    norm[norm[:, :] > 1] = 1
    norm[norm[:, :] < 0] = 0
    return norm * 255


# Tutaj będzie zabawy z parametrami
# i - agresywność rozmycia Gaussa
# percent - percentyle zdjęcia użyte do wykrywania krawędzi metodą Canny'ego
# można też spróbować dopasować contourArea w tym ifie,
# coby odfiltrowało najmniejsze zaznaczone (i najprawdopodobniej - niepotrzebne) krawędzie
# Jebla idzie dostać
# Trzymajcie się na tych KCK'ach

def prepare_photo(photo):
    i = 3
    kernel = np.ones((i, i), np.float32) / i ** 2

    work = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    work = np.uint8(contrast(work))
    work = cv2.filter2D(work, -1, kernel)

    percent = np.percentile(work, [5, 60])

    work = cv2.Canny(work, percent[0], percent[1])
    contour_array, _ = cv2.findContours(work, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    contours = []

    # Weź kontury o większym polu niż ileś tam pikseli
    for xD in contour_array:
        if cv2.contourArea(xD) > 0:
            # print(cv2.contourArea(xD))
            contours.append(xD)

    cv2.drawContours(photo, contours, -1, (0, 255, 0), 3)

    return photo

#   ] \      / [        /\        ][   ] \     ][
#   ][\\    //][       //\\       ][   ][\\    ][
#   ][ \\  // ][      //  \\      ][   ][ \\   ][
#   ][  \\//  ][     //    \\     ][   ][  \\  ][
#   ][        ][    //======\\    ][   ][   \\ ][
#   ][        ][   //        \\   ][   ][    \\][
#   ][        ][  //          \\  ][   ][     \ [


if __name__ == '__main__':
    filenames = []

    for i in range(1, 12):
        filenames.append(str(i))

    filenames.append("kostka")

    images = [cv2.imread('./data/' + i + '.jpg') for i in filenames]

    for i in range(0, len(filenames)):
        plt.clf()
        print(filenames[i] + ".txt")
        io.imshow(cv2.cvtColor(prepare_photo(images[i]), cv2.COLOR_BGR2RGB))
        plt.savefig('./Preprocessed/' + filenames[i] + '.png')
