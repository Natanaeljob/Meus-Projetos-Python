from cores import cv
from linhas import *

def menu():
  #Interface
  print(' ', end = '')
  lc('MENU',cort = 5, corl = 4)
  print(f'''{cv(4)}{"|":<36}{"|"}{cv(0)}
{cv(4)}{"|":<10}{cv()}{"[1] - Jogar":<26}{cv(4)}{"|"}{cv(0)}
{cv(4)}{"|":<36}{"|"}{cv()}
{cv(4)}{"|":<10}{cv()}{"[2] - sair":<26}{cv(4)}{"|"}{cv(0)}
{cv(4)}{"|":<36}{"|"}{cv()}''')
  print(' ', end = '')
  ls(4)
  #Operaçao
  R = '0'
  while R not in '12':
    print('')
    R = str( input(f'{"[R]: ":>15}'))
    if R == '' or R not in '12':
        print('')
        R = f'{cv(1)}Op. Invalida{cv()}'
        print(R)
  print('')
  ls(3)
  if R == '1':
    R = 'ON'
  else:
    R = 'OFF'
  return R
