#PDI - UNIDADE01 - CAP02 - ATIVIDADE 02 - Troca de Regiões
#Thaynara
#https://docs.opencv.org/3.4/d5/d98/tutorial_mat_operations.html
#https://agostinhobritojr.github.io/tutorial/pdi/pixels.html

#trocar os quadrantes em diagonal na imagem.
import cv2
import numpy as np

Arquivo = "imagens/biel.png"

#Abrir a imagem
image = cv2.imread(Arquivo, cv2.IMREAD_GRAYSCALE)
if image is None:
    print(f"nao abriu {Arquivo}")

altura, largura = image.shape[:2]
x = int(altura/2)
y = int(largura/2)
#Considerando que a imagem de entrada é multiplo de 02.

img_copy = np.copy(image)
cv2.namedWindow("Original", cv2.WINDOW_AUTOSIZE)

#Regioes de interesse:
image[0:x, 0:y] = img_copy[x:largura, y:altura]
image[0:x, y:altura] = img_copy[x:largura, 0:y]
image[x:largura, 0:y] = img_copy[0:x, y:altura]
image[x:largura, y:altura] = img_copy[0:x, 0:y]

cv2.namedWindow("Resultado", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Resultado", image)
cv2.imshow("Original", img_copy)
cv2.waitKey()