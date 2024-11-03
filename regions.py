#Primeiro exercicio do capitulo 2.2 - Unidade 01
#Thaynara Maria Cunha de Andrade

import cv2
import numpy as np
Arquivo = "imagens/biel.png"

#Abrir a imagem
image = cv2.imread(Arquivo, cv2.IMREAD_GRAYSCALE)
if image is None:
    print(f"nao abriu {Arquivo}")

altura, largura = image.shape[:2]

#solicitar ao usuario as coordenadas de dois pontos P1 e P2, localizados dentro dos limites do tamanho da imagem
p1 = input(f"O tamanho da imagem é ({altura}, {largura}):\nDigite as coordenadas (x,y) do ponto 01, no formato x,y :\n")
x_p1, y_p1 = p1.split(',')
x_p1 = int(x_p1)
y_p1 = int(y_p1)

while x_p1 > altura or x_p1 < 0 or y_p1 > largura or y_p1 < 0:
    p1 = input(f"A coordenada ({x_p1}, {y_p1}) é inválida.\n"
          "Digite uma coordenada válida (0 <= x <= {altura}, 0 <= y <= {largura}): ")
    x_p1, y_p1 = p1.split(',')
    x_p1 = int(x_p1)
    y_p1 = int(y_p1)

p2 = input(f"O tamanho da imagem é ({altura}, {largura}):\nDigite as coordenadas (x,y) do ponto 02, no formato x,y :\n")
x_p2, y_p2 = p2.split(',')
x_p2 = int(x_p2)
y_p2 = int(y_p2)

while x_p2 > altura or x_p2 < 0 or y_p2 > largura or y_p2 < 0:
    p2 = input(f"A coordenada ({x_p2}, {y_p2}) é inválida.\n"
          "Digite uma coordenada válida (0 <= x <= {altura}, 0 <= y <= {largura}): ")
    x_p2, y_p2 = p2.split(',')
    x_p2 = int(x_p2)
    y_p2 = int(y_p2)

cv2.namedWindow("janela", cv2.WINDOW_AUTOSIZE)

#x,y = largura, altura
for i in range(x_p1, x_p2):
    for j in range(y_p1, y_p2):
        if i == x_p1 or i == x_p2 - 1 or j == y_p1 or j == y_p2 - 1:
            image[i, j] = 0

cv2.imshow("janela", image)
cv2.waitKey()

image = cv2.imread(Arquivo, cv2.IMREAD_COLOR)
figura = np.copy(image)
#x,y = largura, altura
for i in range(x_p1, x_p2):
    for j in range(y_p1, y_p2):
        image[i, j] = 1 - image[i,j]

cv2.namedWindow("resultado", cv2.WINDOW_AUTOSIZE)
cv2.imshow("resultado", image)
cv2.waitKey()
