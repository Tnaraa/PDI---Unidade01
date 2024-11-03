#PDI - Unidade 01 - Filtros de 3x3, 21x21 e 11x11
#Thaynara
#Capitulo 14 - Filtragem no domínio espacial I - Convolução
import cv2
import numpy as np

#Filtros
media_3x3 = np.ones((3,3), dtype=np.float32)
media_3x3[:] = 1/9

media_11x11 = np.ones((3,3) , dtype=np.float32)
media_11x11[:] = 1/(11*11)

media_21x21 = np.ones((3,3), dtype=np.float32)
media_21x21[:] = 1/(21*21)

#Analise camera
camera = 0
cap = cv2.VideoCapture(camera)

if not cap.isOpened():
    print("cameras indisponiveis")
    exit(-1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

#mascara
mask3 = np.zeros((3,3),np.float32)
mask3 = media_3x3
mask11 = np.zeros((3,3),np.float32)
mask11 = media_11x11
mask21 = np.zeros((3,3),np.float32)
mask21 = media_21x21

absolut = 1 #calcula absoluto da imagem

while True:
    #Abre a camera
    status, frame = cap.read()

    if not status:
        print("Erro ao usar a camera")
        exit(-1)

    framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    framegray = cv2.flip(framegray, 1)
    cv2.imshow("original", framegray)
    frame32f = framegray.astype(np.float32)

    framefiltered3 = cv2.filter2D(frame32f,-1,mask3, anchor=(1,1))
    framefiltered11 = cv2.filter2D(frame32f, -1, mask11, anchor=(1, 1))
    framefiltered21 = cv2.filter2D(frame32f, -1, mask21, anchor=(1, 1))

    if absolut:
        framefiltered3 = abs(framefiltered3)
        framefiltered11 = abs(framefiltered11)
        framefiltered21 = abs(framefiltered21)

    result3 = framefiltered3.astype(np.uint8)
    result11 = framefiltered11.astype(np.uint8)
    result21 = framefiltered21.astype(np.uint8)

    cv2.imshow("filtro espacial 3x3", result3)
    cv2.imshow("filtro espacial 11x11", result11)
    cv2.imshow("filtro espacial 21x21", result21)

    #Encerramento camera
    key = cv2.waitKey(30)
    if key == 27:
        break
    elif(key == ord('a')):
        absolut = not absolut

cap.release()
cv2.destroyAllWindows()