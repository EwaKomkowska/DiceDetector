import cv2
import numpy as np


def cubeCircles(image, dp=1, minDist=40, param1=400, param2=40, minRadius=9, maxRadius=0):
    cubes = cv2.imread(image)
    # filenames[i], 1, 40, 400, 40
    # dziala dla 30; 40;
    # na 46 wykrywa jedno, ale poprawnie;
    # 2 (wykrywa przednie); 7(wykrywa jedno);
    # 17 (wykrywa tylko 2);19 - jedno; 21 jedno;
    # 24 - dwa; 25 - wykrywa 10; 27 wykrywa 1;

    gray = cv2.cvtColor(cubes, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 9)

    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    #minDist - srednia odleglosc
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
    circles = np.uint16(np.around(circles))

    licznik = 0
    for i in circles[0, :]:
        #outer circle
        cv2.circle(cubes, (i[0], i[1]), i[2], (0, 255, 0), 2)
        licznik += 1
        #center of the circle
        cv2.circle(cubes, (i[0], i[1]), 2, (0, 0, 255), 5)          #czy ta 2 jest promieniem?

    # Write some Text

    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, 30)
    fontScale = 0.5
    fontColor = (255, 0, 0)
    lineType = 2

    cv2.putText(cubes, "Suma liczby wykrytych oczek: " + str(licznik), bottomLeftCornerOfText, font, fontScale, fontColor, lineType)

    tytul = "Circle detection - Suma liczby wykrytych oczek: " + str(licznik)
    cv2.imshow(tytul, cubes)
    #im = cv2.resize(cubes, (600, 600))
    #cv2.imshow(tytul, im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    filenames = ['./data/' + str(28) + '.jpg']
    '''for i in range(10, 50, 10):
        filenames.append('./data/' + str(i) + '.jpg')'''

    #filenames.append("kostka")

    for i in range(0, len(filenames)):
        cubeCircles(filenames[i], 1, 200, 200, 25)



#28         filenames[i], 1, 200, 200, 25       wykrywa dwa poprawnie i trzecie błędnie na całej kostce
#46         filenames[i], 1, 45, 550, 30
#31         filenames[i], 1, 45, 550, 35
#43         filenames[i], 1, 50, 600, 25
#48         filenames[i], 1, 100, 400, 55
