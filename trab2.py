import numpy as np
import cv2 as cv


def invertHue(h, m, x):
    upper = np.mod((m + x)/2, 180)
    lower = np.mod((m - x)/2, 180)

    start = h <= upper
    end = h >= lower

    h = h.astype(np.uint16)

    operation = start & end if lower < upper else start | end

    h[operation] = np.mod(h[operation] + 90, 180).astype(np.uint8)

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

    image_hsv = cv.merge([hue, saturation, value])
    rgb = cv.cvtColor(image_hsv, cv.COLOR_HSV2BGR)

    cv.imshow('Imagem Alterada', rgb)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.waitKey(1)


def main():
    a = cv.imread('unknown.png')
    m = int(input("Matiz: "))
    x = int(input("X: "))

    hueAlteration(a, m, x)


if __name__ == '__main__':
    main()
