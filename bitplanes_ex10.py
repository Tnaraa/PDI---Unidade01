#PDI - UNIDADE01 - CAPITULO10: Exercicio

import cv2
import numpy as np

Arquivo = "imagens/desafio-esteganografia.png"
nbits = int(3)

#Abrir a imagem
imagemOriginal = cv2.imread(Arquivo, cv2.IMREAD_COLOR)
if imagemOriginal is None:
    print(f"nao abriu {Arquivo}")
    exit()

imagemEscondida = np.copy(imagemOriginal)
valEscondida = [0,0,0]

for i in range(0, imagemOriginal.shape[0]):
    for j in range(0, imagemOriginal.shape[1]):
        valOrig = imagemOriginal[i, j]
        #Desloca os bits menos significativos para oa esquerda
        valEscondida[0] = valOrig[0] << (8 - nbits)
        valEscondida[1] = valOrig[1] << (8 - nbits)
        valEscondida[2] = valOrig[2] << (8 - nbits)

        imagemEscondida[i,j] = valEscondida

cv2.imshow("Imagem Escondida", imagemEscondida)
cv2.imshow("Original", imagemOriginal)
cv2.waitKey()
