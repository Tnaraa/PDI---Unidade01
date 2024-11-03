#PDI - Unidade 01 - Capítulo 15. Filtragem no domínio espacial II - TiltShift
#Thaynara Maria

#https://stackoverflow.com/questions/57547796/creating-multiple-trackbars-in-opencv-python
import cv2
import numpy as np

imageTop = None
image1 = None
image2 = None
blended = None

alfa_slider = 0
alfa_slider_max = 100

gauss_max = 100
gauss = 0

top_slider = 0
top_slider_max = 100

inferior_slider = 0
inferior_slider_max = 100

TrackbarName = ['']*50

def on_trackbar_blend(val):
    global alfa_slider
    alfa_slider = val
    on_trackbar_functions(image2)

def on_trackbar_foco_topo(val):
    global top_slider
    top_slider = val
    on_trackbar_functions(image2)

def on_trackbar_foco_abaixo(val):
    global inferior_slider
    global top_slider
    if val > top_slider + 3:
        inferior_slider = val
    else:
        inferior_slider = inferior_slider
    on_trackbar_functions(image2)

def on_trackbar_gaussiano(val):
    global gauss
    gauss = val
    on_trackbar_functions(image2)

def on_trackbar_functions(image):

    imageTop = np.copy(image1)
    limit = int(top_slider*image.shape[0]/100)
    limit2 = int(inferior_slider*image.shape[0]/100)
    image2 = cv2.GaussianBlur(image, (gauss*2 + 1, gauss*2 + 1), 0)

    if limit > 0:
        tmp = image2[limit:limit2, 0:image.shape[1]]
        imageTop[limit:limit2, 0:image.shape[1]] = tmp

    alfa = alfa_slider / alfa_slider_max
    blended = cv2.addWeighted(image1, 1- alfa, imageTop, alfa, 0.0)
    cv2.imshow("addweighted", blended)
    cv2.imwrite("ResultadoTiltshit.png", blended)

#Código:
Arquivo = "imagens/biel-color.png"

#Abrir a imagem
image1 = cv2.imread(Arquivo, cv2.IMREAD_COLOR)
if image1 is None:
    print(f"nao abriu {Arquivo}")
image2 = cv2.imread("imagens/biel-color.png", cv2.IMREAD_COLOR)

imageTop = np.copy(image2)

cv2.namedWindow("addweighted", 1)
TrackbarName = 'Alfa x %d' % alfa_slider_max

cv2.createTrackbar(TrackbarName, "addweighted",
                   alfa_slider,
                   alfa_slider_max,
                   on_trackbar_blend)

TrackbarName = 'Scanline x %d' % top_slider_max
cv2.createTrackbar("x_s x {}".format(top_slider_max),
                  "addweighted",
                   top_slider,
                   top_slider_max,
                   on_trackbar_foco_topo)

TrackbarName = 'x_i x %d' % top_slider_max
cv2.createTrackbar(TrackbarName,
                  "addweighted",
                   inferior_slider,
                   inferior_slider_max,
                   on_trackbar_foco_abaixo)

TrackbarName = 'Gauss x %d' % gauss_max
cv2.createTrackbar(TrackbarName,
                  "addweighted",
                   gauss,
                   gauss_max,
                   on_trackbar_gaussiano)

on_trackbar_functions(image2)

cv2.waitKey(0)
