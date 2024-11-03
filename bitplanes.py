
import cv2

ArqPortadora = "imagens/biel-color.png"
ArqEscondida = "imagens/sushi-color.png"
nbits = int(3)

#Abrir a imagem
imagemPortadora = cv2.imread(ArqPortadora, cv2.IMREAD_COLOR)
imagemEscondida = cv2.imread(ArqEscondida, cv2.IMREAD_COLOR)

if imagemPortadora is None or imagemEscondida is None:
    print("Imagem não carregou corretamente")
    exit()

if imagemPortadora.shape[0] != imagemEscondida.shape[0] or  imagemPortadora.shape[1] != imagemEscondida.shape[1]:
    print('imagens devem ter o mesmo tamanho')
    exit()

imagemFinal = imagemPortadora.copy()
valFinal = [0,0,0]
for i in range(0, imagemPortadora.shape[0]):
    for j in range(0, imagemPortadora.shape[1]):
        valPortadora = imagemPortadora[i, j]
        valEscondida = imagemEscondida[i, j]
        valPortadora[0] = valPortadora[0] >> nbits << nbits
        valPortadora[1] = valPortadora[1] >> nbits << nbits
        valPortadora[2] = valPortadora[2] >> nbits << nbits
        valEscondida[0] = valEscondida[0] >> (8 - nbits)
        valEscondida[1] = valEscondida[1] >> (8 - nbits)
        valEscondida[2] = valEscondida[2] >> (8 - nbits)
        valFinal[0] = valPortadora[0] | valEscondida[0]
        valFinal[1] = valPortadora[1] | valEscondida[1]
        valFinal[2] = valPortadora[2] | valEscondida[2]
        imagemFinal[i,j] = valFinal

cv2.imwrite("esteganografia.png", imagemFinal)