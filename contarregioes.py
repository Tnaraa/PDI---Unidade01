#Aprimore o algoritmo de contagem apresentado para identificar regiões com ou sem buracos internos
# que existam na cena. Assuma que objetos com mais de um buraco podem existir.
# #Inclua suporte no seu algoritmo para não contar bolhas que tocam as bordas da imagem.
# Não se pode presumir, a priori, que elas tenham buracos ou não.
#CAPITULO 11 - PDI - LABELING

import cv2
import numpy as np

Arquivo = "imagens/bolhas.png"

#Abrir a imagem
image = cv2.imread(Arquivo, cv2.IMREAD_COLOR)
nbolhas = int(0)
nobjects = 0
nbordas = 0
p = (0, 0)

if image is None:
    print("Imagem não carregou corretamente")
    exit()

width = image.shape[1]
height = image.shape[0]
print(f"{width} x {height}")

#Na versão python, precisa da mascara para o floodfill
mask = np.zeros((height+2,width+2),np.uint8)

for i in range(height):
    for j in range(width):
        if (image[i,j] == np.array([255, 255, 255])).all():
            if ((i == 0 or i == height -1) and j <= width) or ((j == 0 or j == width - 1) and i <= height):
                #achou um objeto
                nbordas += 1
                #para o floodfill as coordenadas x e y são trocadas.
                p = (j, i)
                #reenche o objeto com o contador
                cv2.floodFill(image, mask, p, [0,0,0])

img_sbordas =  np.copy(image)
cv2.imshow("Sem bolhas nas bordas", image)
cv2.waitKey()
n_bolhas = 0

#Filtrar a imagem
for i in range(height):
    for j in range(width):
        if (img_sbordas[i,j] == np.array([255, 255, 255])).all():
            #achou um objeto
            n_bolhas += 1
            #para o floodfill as coordenadas x e y são trocadas.
            p = (j, i)
            if n_bolhas > (255+255):
                cv2.floodFill(img_sbordas, mask, p, [(n_bolhas - 255), 1, 0])
            elif n_bolhas > 255:
                cv2.floodFill(img_sbordas, mask, p, [0,(n_bolhas-255),1])
            else:
                cv2.floodFill(img_sbordas, mask, p, [0, 1, n_bolhas])

cv2.imshow("imagem pos contagem de bolhas totais", img_sbordas)
cv2.waitKey()
cv2.floodFill(img_sbordas,None, (0,0), (0,240,240))

for i in range(height):
    for j in range(width):
        if (img_sbordas[i,j] == np.array([0,0,0])).all():
            #achou um objeto
            nobjects += 1
            #para o floodfill as coordenadas x e y são trocadas.
            p = (j, i)
            #reenche o objeto com o contador
            cv2.floodFill(img_sbordas, mask, p, [128,128,128])


print(f"A figura tem {nobjects} bolhas com buracos no meio\n")
print(f"A figura tem {n_bolhas} bolhas, excluindo as que se encontram nas bordas\n")
print(f"A figura tem {nbordas} bolhas encostando nas bordas\n")
cv2.imshow("imagem final ", img_sbordas)
cv2.imwrite("labeling.png", img_sbordas)
cv2.waitKey()