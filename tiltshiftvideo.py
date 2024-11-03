#PDI - Unidade 01 - Capítulo 15. Filtragem no domínio espacial II - TiltShiftVideo
#Thaynara Maria
#Video: https://www.youtube.com/watch?v=DUJY5Z0TfeI&t=337s

#https://stackoverflow.com/questions/57547796/creating-multiple-trackbars-in-opencv-python

#Youtube link: https://youtu.be/r5lTmHuPsks
import cv2
import numpy as np

image1 = None
imageTop = None
Image2 = None

alfa_slider_max = 100
alfa_slider = 0
nome = "addweighted"

cap = cv2.VideoCapture("imagens/rodovia.mp4")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f"largura = {width}")
print(f"altura = {height}")
max_y = int(width)
max_x = int(height)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para MP4
out = cv2.VideoWriter('imagens/motionrodovia.mp4', fourcc, 20.0, (max_y, max_x))

valor = 10

def on_trackbar_blend(val):
    global alfa_slider
    global image2
    alfa_slider = val

def on_trackbar_functions(image):
    image2 = cv2.GaussianBlur(image, (21, 21), 0)

    tmp = image2[0:max_x, 0:int(max_y/7)]
    imageTop[0:max_x, 0:int(max_y/7)] = tmp

    tmp2 = image2[0:int(max_x/5), 0:max_y]
    imageTop[0:int(max_x/5), 0:max_y] = tmp2

    tmp3 = image2[0:max_x, 6*int(max_y/7):max_y]
    imageTop[0:max_x, 6*int(max_y/7):max_y] = tmp3

    tmp4 = image2[4*int(max_x/5):max_x, 0:max_y]
    imageTop[4*int(max_x/5):max_x, 0:max_y] = tmp4

    alfa = alfa_slider / alfa_slider_max
    blended = cv2.addWeighted(image1, 1- alfa, imageTop, alfa, 0.0)
    cv2.imshow("addweighted", blended)
    return blended


cv2.namedWindow(nome, 1)

TrackbarName = 'Alfa x %d' % alfa_slider_max

cv2.createTrackbar(TrackbarName, "addweighted",
                   alfa_slider,
                   alfa_slider_max,
                   on_trackbar_blend)

while cap.isOpened():
    # Captura frame da cena do video
    status, frame = cap.read()
    if not status:
        print("Não foi possivel pegar o quadro do video")
        break
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Aumentar a saturação
    saturation_scale = 2.5  # Fator de aumento da saturação
    hsv_frame[:, :, 1] = np.clip(hsv_frame[:, :, 1] * saturation_scale, 0, 255)

    # Converter de volta para o espaço de cores BGR
    frame = cv2.cvtColor(hsv_frame, cv2.COLOR_HSV2BGR)

    image1 = np.copy(frame)

    imageTop = np.copy(image1)

    dado = on_trackbar_functions(image1)
    out.write(dado)

    for i in range(valor):
        sit, vo = cap.read()
        if not sit:
            break

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()