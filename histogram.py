#https://docs.opencv.org/3.4/d8/dbc/tutorial_histogram_calculation.html
import cv2
import numpy as np

rodando = True
width, height = 0, 0
nbits = 64
Range = (0,25)
uniform = True
acummulate = False
histrange = [Range]
camera = 0
#histSize = 256

cap = cv2.VideoCapture(camera)

if not cap.isOpened():
    print("cameras indisponiveis")
    exit(-1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f"largura = {width}")
print(f"altura = {height}")

histw = nbits
histh = int(nbits//2)

histImgR = np.zeros((histh, histw, 3), dtype=np.uint8)
histImgG = np.zeros((histh, histw, 3), dtype=np.uint8)
histImgB = np.zeros((histh, histw, 3), dtype=np.uint8)

while rodando:
    status, image = cap.read()
    if not status:
        rodando = False

    planes = cv2.split(image)
    print(cv2.split(image))
    histR = cv2.calcHist([image], [0], None, [nbits], Range)

    cv2.normalize(histR, histR, 0, histImgR.shape[0], cv2.NORM_MINMAX)
    histR = histR.astype(np.uint8)
    histImgR[:] = 0



    #image[0:histh, 0:nbits] = histImgR
    #image[histh:2 * histh, 0:nbits] = histImgG
    #image[2 * histh:3 * histh, 0:nbits] = histImgB
    cv2.imshow("image", image)
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

    #cv2.imshow("Camera", image)