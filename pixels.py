import cv2

image = cv2.imread("imagens/bolhas.png", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("nao abriu bolhas.png")

cv2.namedWindow("janela", cv2.WINDOW_AUTOSIZE)

for i in range(200, 210):
    for j in range(10, 200):
        image[i, j] = 0

cv2.imshow("janela", image)
cv2.waitKey()

image = cv2.imread("imagens/bolhas.png", cv2.IMREAD_COLOR)

B = 0
G = 0
R = 255
val = [B, G, R]  # B, G, R

for i in range(200, 210):
    for j in range(10, 200):
        image[i, j] = val

cv2.imshow("janela", image)
cv2.waitKey()






