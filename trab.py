# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv


def limiarizacao(img: np.ndarray, t: int, acima: bool, brilho: int) -> None:
  if acima:
    x = img >= t
  else:
    x = img < t
  img = img.astype(int)
  if brilho < 0:
    img[x] = np.maximum(img[x] + brilho, 0)
  else:
    img[x] = np.minimum(img[x] + brilho, 255)
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

  limiarizacao(cv.imread("gato.jpg", cv.IMREAD_GRAYSCALE), 100, True, 180)


if __name__ == "__main__":
  main()
