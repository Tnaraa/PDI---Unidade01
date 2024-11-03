import cv2
import numpy as np

Arquivo = "imagens/bolhas.png"

#Abrir a imagem
image = cv2.imread(Arquivo, cv2.IMREAD_GRAYSCALE)

p = (0, 0)

if image is None:
    print("Imagem não carregou corretamente")
    exit()

width = image.shape[1]
height = image.shape[0]
print(f"{width} x {height}")

#Na versão python, precisa da mascara para o floodfill
mask = np.zeros((height+2,width+2),np.uint8)
#Busca objetos presentes
nobjects = 0

for i in range(height):
    for j in range(width):
        if image[i,j] == 255:
            #achou um objeto
            nobjects += 1
            #para o floodfill as coordenadas
            #x e y são trocadas.
            p = (j, i)
            #reenche o objeto com o contador
            cv2.floodFill(image, mask, p, nobjects)

print(f"A figura tem {nobjects} bolhas\n")
cv2.imshow("imagem", image)
cv2.imwrite("labeling.png", image)
cv2.waitKey()