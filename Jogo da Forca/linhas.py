from cores import cv

def ls(cor = cv(), tip = '_', espace = True):

  tam = 36 // len(tip)
  print(f'{cv(cor)}{"_" * tam}{cv()}')
  if espace == True:
    print(' ')

def lc(texto, tip = '_', cort = 0, corl = 0):
  tam = 34 - len(texto)
  if tam % 2 != 0:
    tam + 1
  tam //= 2
  tam //= len(tip)
  op = tip * tam
  print(f'{cv(corl)}{op}{cv(cort)} {texto} {cv(corl)}{op}{cv()}')
