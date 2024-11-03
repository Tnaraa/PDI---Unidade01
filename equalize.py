#PDI - Unidade 01 - Excercicio equalização histograma
#Thaynara Maria Cunha de Andrade
#Fontes: https://docs.opencv.org/3.4/d4/d1b/tutorial_histogram_equalization.html
    #https://docs.opencv.org/3.4/d8/dbc/tutorial_histogram_calculation.html
    #https://agostinhobritojr.github.io/tutorial/pdi/histograma.html

import cv2
import numpy as np

rodando = True
width, height = 0, 0
nbits = 256
Range = (0,256)
uniform = True
camera = 0

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
histh = int(round(nbits//2))

while True:
    status, image = cap.read()
    if not status:
        print("Erro")
        exit(-1)

    #Histograma da imagem cinza
    plano = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    histGray = cv2.calcHist(plano, [0], None, [nbits], Range, )

    #Equalização da imagem cinza e o sue histograma
    ImgEqualizado = cv2.equalizeHist(plano)
    histEq = cv2.calcHist([ImgEqualizado], [0], None, [nbits], Range,  accumulate = False)

    #Normalização da imagem cinza e equalizada
    cv2.normalize(histGray, histGray, 0, histh, cv2.NORM_MINMAX)
    #histGray = histGray.astype(np.uint8)
    cv2.normalize(histEq, histEq, 0, histh, cv2.NORM_MINMAX)
    #histEq = histEq.astype(np.uint8)
    histImgGray = np.zeros((histh, histw, 3), dtype=np.uint8)
    histImgEq = np.zeros((histh, histw, 3), dtype=np.uint8)

    for i in range(1,nbits):
        cv2.line(histImgGray, (i, histh), (i, histh - int(histGray[i])), (0, 255, 255))
        cv2.line(histImgEq, (i, histh), (i, histh - int(histEq[i])), (0,0,255))

    histogramas = np.hstack((histImgGray, histImgEq))
    videos = np.hstack((plano, ImgEqualizado))
    cv2.imshow("Histogramas(normal,equalizado)", histogramas)
    cv2.imshow("Video(normal,equalizado)", videos)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
