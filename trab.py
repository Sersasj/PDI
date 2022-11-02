# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv


def thresholding(img: np.ndarray, t: int, isAbove: bool, brightness: int) -> None:
  """Função que realiza a limiarização da imagem.

  Recebe de parâmetros:
  img: a imagem que será utilizada
  t: o valor de limiarização
  isAbove: variável que controla o fluxo de alteração de brilho em relação ao limiar 
  brightness: valor de brilho que será utilizado
  """

  if isAbove:     # delimita o fluxo de alteração de brilho
    x = img >= t  # se isAbove for True, para cada pixel com valor >= t será alterado o brilho
  else:
    x = img < t   # se isAbove for False, o inverso ocorre

  img = img.astype(int)

  if brightness < 0:  # tratamento de valor de brilho, devendo estar entre o intervalo 0 <= brightness <= 255
    img[x] = np.maximum(img[x] + brightness, 0)
  else:
    img[x] = np.minimum(img[x] + brightness, 255)
  img = img.astype(np.uint8)

  cv.imshow("teste", img)
  cv.waitKey(0)
  cv.destroyAllWindows()
  cv.waitKey(1)


def main():
  print("#--------------------------------------------------------------------------------------------#")
  print("# Este programa recebe uma imagem em tons de cinza e realiza nesta uma alteração localizada  #\n"+ 
    "# de brilho em função de uma operação de limiarização (thresholding)                         #")
  print("#--------------------------------------------------------------------------------------------#")

  #imagem = int(input("1 - Coelho\n2 - Cachorro\n3 - Gato\n"))
  #if imagem == 1:
  #    imagem = "coelho.jpg"
  #elif imagem == 2:
  #    imagem = "cachorro.jpg"    
  #elif imagem == 3:
  #    imagem = "gato.jpg"          
  #t = int(input("Digite um valor de limiar"))
  #brilho = int(input("Digite um valor de brilho "))
  #acima = bool(input("Digite False ou True "))
  print("#--------------------------------------------------------------------------------------------#")

  thresholding(cv.imread("gato.jpg", cv.IMREAD_GRAYSCALE), 100, True, 180)


if __name__ == "__main__":
  main()
