import numpy as np
import cv2 as cv


def invertHue(h, m, x):
    # faz o cálculo dos limites superiores e inferiores
    # com base em 180 por aspectos da bibilioteca cv2
    upper = np.mod((m + x)/2, 180)
    lower = np.mod((m - x)/2, 180)

    # cria matrizes booleanas de acordo com as condições
    # de começo e fim do círculo HSV delimitado pelo
    # usuário 
    start = h <= upper
    end = h >= lower

    # realiza o casting para o tipo np.uint16
    h = h.astype(np.uint16)

    # delimita qual operação será usada dependendo da 
    # condição de que o limite inferior é menor do que 
    # o limite superior 
    operation = start & end if lower < upper else start | end

    # realiaza a operação (podendo ser união ou interseção)
    h[operation] = np.mod(h[operation] + 90, 180).astype(np.uint8)

    # retorna o valor de hue castado para o tipo np.uint8 de volta
    return h.astype(np.uint8)


def hueAlteration(img: np.ndarray, m: int, x: int) -> None:
    """Função que realiza a alteração de faixa de matizes em uma imagem no sistema HSV

    Recebe de parâmetros:
    img: uma imagem colorida 
    m: um valor de inteiro de matiz (0 <= m < 360)
    x: um valor inteiro x para modificar o intervalo [m - x, m + x] por suas matizes inversas
    """
    # abre a imagem original
    cv.imshow('Imagem original', img)

    # converte a imagem original para HSV
    image_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # separa as matizes h, s e v
    hue, saturation, value = cv.split(image_hsv)
    # chama a função inverHue para inverter o valor de hue
    hue = invertHue(hue, m, x)
    # após realizar as modificações, realiza o merge na imagem
    image_hsv = cv.merge([hue, saturation, value])
    # converte a imagem de volta para RGB
    rgb = cv.cvtColor(image_hsv, cv.COLOR_HSV2BGR)

    # mostra a imagem
    cv.imshow('Imagem Alterada', rgb)
    cv.imwrite("img_alt.png", rgb)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.waitKey(1)


def main():
    a = cv.imread("colorCircle.png")
    m = 120
    x =  60
    #m = int(input("Matiz: "))
    #x = int(input("X: "))
    hueAlteration(a, m, x)


if __name__ == '__main__':
    main()
