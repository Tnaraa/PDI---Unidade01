import numpy as np
import cv2
import math

SIDE = 256
PERIODOS = 8

#criar um string com o nome do arquivo de saída.
ss_yml = f"senoide-{SIDE}.yml"

# matriz de float de tamanho SIDE x SIDE e inicializa todos os
# elementos com o valor 0.
image = np.zeros((SIDE, SIDE), dtype=np.float32)
#cria um objeto da classe cv::FileStorage para armazenar dados em um arquivo.
fs = cv2.FileStorage(ss_yml, cv2.FileStorage_WRITE)


for i in range(SIDE):
    for j in range(SIDE):
        image[i, j] = 127 * math.sin(2 * math.pi * PERIODOS * j / SIDE) + 128

fs.write("mat", image)
#Fceha o fluxo para o arquivo de saida
fs.release()

cv2.normalize(image, image, 0, 255, cv2.NORM_MINMAX)
image = image.astype(np.uint8)
ss_img = f"senoide-{SIDE}.png"
cv2.imwrite(ss_img, image)

fs.open(ss_yml, cv2.FileStorage_READ)

cv2.normalize(image, image, 0, 255, cv2.NORM_MINMAX)
image = image.astype(np.uint8)

cv2.imshow("image", image)
cv2.waitKey()

