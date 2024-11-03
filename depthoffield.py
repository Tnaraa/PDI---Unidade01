#PDI - Unidade 01 - Video
#https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

#Capitulo 14 - Filtragem no domínio espacial I - Convolução
# Efeito de Profundidade de Campo
import cv2
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para MP4
out = cv2.VideoWriter('imagens/output.mp4', fourcc, 20.0, (1280, 720))

#Filtro laplaciano
laplacian = np.array([[0,-1,0],
                            [-1,4,-1],
                            [0,-1,0]], dtype=np.float32)

#Mascara
mask = np.zeros((3,3), np.float32)
mask = laplacian

cap = cv2.VideoCapture("imagens/vasos720p.mp4")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f"largura = {width}")
print(f"altura = {height}")
max_y = int(width)
max_x = int(height)

Valores = np.ones((max_x, max_y))
#Matrix para guardar os máximos laplacianos.
MaxLaplaciano = np.zeros((max_x, max_y))
status, frame = cap.read()
if not status:
    print("Não foi possivel pegar o quadro do video")
frameOk = np.copy(frame)
n = 0
while cap.isOpened():
    #Captura frame da cena do video
    status, frame = cap.read()
    if not status:
        print("Não foi possivel pegar o quadro do video")
        break
    if n <= 1:
        frameant = np.copy(frame)
        n += 1
    #Converta o frame para tons de cinza.
    framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('quadro', framegray)

    cv2.imshow("original", framegray)
    frame32f = framegray.astype(np.float32)
    framefiltered = cv2.filter2D(frame32f, -1, mask, anchor=(1, 1))
    Valores = np.copy(framefiltered)

    for i in range(0, max_x):
        for j in range(0, max_y):
            if Valores[i,j] > MaxLaplaciano[i,j]:
                MaxLaplaciano[i,j] = Valores[i,j]
                frameOk[i,j] = frame[i,j]
                frameant = frameOk
            else:
                frameOk = frameant
    cv2.imshow("saida", frameOk)
    dado = cv2.flip(frameOk, 0)

    # write the flipped frame
    out.write(frameOk)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()