# PDI

LIMIARIZAÇÃO E ALTERAÇÃO LOCAL DE BRILHO

O objetivo deste trabalho é implementar e testar um programa que receba uma imagem em tons de cinza e realize nesta uma alteração localizada de brilho em função de uma operação de limiarização (thresholding).

O programa deve receber os seguintes parâmetros:
uma imagem de entrada a, em tons de cinza
um valor inteiro de limiar t;
um valor booleano acima;
um valor inteiro brilho. 

Se acima for True, você deve realizar a alteração de brilho dos pixels com tons de cinza maiores ou iguais a t. Caso contrário, altere o brilho dos pixels com tons de cinza menores que t.
Dependendo do parâmetro brilho, a alteração localizada poderá ser um aumento (se brilho for positivo) ou uma redução (se brilho for negativo) de brilho.
Lembre-se que os valores alterados não podem ser menores que zero (preto) e nem maiores que L - 1 (branco).
O programa gera, como saída, uma imagem em tons de cinza com os valores de brilho alterados localmente.

Feito em python
Imagens utilizadas:

An Ancient Dark Night Descended Upon My Soul II (Ana Maria Pacheco) Journeys (Ana Maria Pacheco)
