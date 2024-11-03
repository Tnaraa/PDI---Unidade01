#PDI - Unidade 01 - Excercicio equalização histograma 2
#Detector de movimento
#Thaynara Maria Cunha de Andrade
#Fontes: https://docs.opencv.org/3.4/d4/d1b/tutorial_histogram_equalization.html
    #https://docs.opencv.org/3.4/d8/dc8/tutorial_histogram_comparison.html
#https://www.youtube.com/watch?v=vJOJtEj_-RM

import cv2
import numpy as np

rodando = True
width, height = 0, 0
nbits = 256
Range = (0,256)
uniform = True
camera = 0
movimento = 0
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

histImg = np.zeros((histh, histw, 3), dtype=np.uint8)
histOr = np.zeros((histh, histw, 3), dtype=np.uint8)
cv2.normalize(histOr, histOr, 0, histh, cv2.NORM_MINMAX)

status, image = cap.read()
if not status:
    print("Erro")
    exit(-1)
#Histograma da imagem cinza
planos = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

histOr = cv2.calcHist(planos, [0], None, [nbits], Range, accumulate = False)

while True:
    status, image = cap.read()
    if not status:
        print("Erro")
        exit(-1)
    plano = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #Histograma da imagem cinza
    hist = cv2.calcHist([plano], [0], None, [nbits], Range, accumulate = False)

    #Normalização da imagem cinza
    cv2.normalize(hist, hist, 0, histh, cv2.NORM_MINMAX)

    img_base = cv2.compareHist(histOr, hist, cv2.HISTCMP_CORREL)

    if img_base < 0.95:
        movimento += 1
        cv2.putText(image, "Houve movimento", (10, image.shape[1] - 200), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                    (64, 75, 255), 2)
        print(f"Houve movimento({movimento})")

    for i in range(1,64):
        cv2.line(histImg, (i, histh), (i, histh - int(hist[i])), (0, 255, 255))

    cv2.imshow("Video", image)
    histOr =  np.copy(hist)
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
