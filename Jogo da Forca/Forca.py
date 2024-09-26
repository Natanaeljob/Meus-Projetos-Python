# Funçoes
def forca(win = False, lose = False):
    if win == False and lose == False:
        if erro >= 0:
            p1 = p2 = p3 = p4 = p5 = p6 = ' ' 
            if erro >= 1:
                p1 = 'O'
                if erro >= 2:
                    p2 = '|'
                    if erro >= 3:
                        p3 ='/'
                        if erro >= 4:
                            p4 = '\ '
                            if erro >= 5:
                                p5 = p3
                                if erro >= 6:
                                    p6 = p4

            print(f'''{cv(1)}______________
|             |
|             {al1}{p1}{cv(1)}
|            {al1}{p3}{p2}{p4}{cv(1)}
|             {al1}{p2}{cv(1)}
|            {al1}{p5} {p6}{cv(1)}
|
|
|
|{cv()}''', end = '  ')


    elif lose == True:     
        print(f'''{cv(1)}______________
|             |
|             O  Enforcado!
|            /|\ 
|             |   Tente novamente
|            / \ 
|
|
|
|{cv()}''', end = '  ')

    else:
                print(f'''{cv(1)}______________
|             |
|
|
|
|    {cv(2)}O   Obrigado por me Salvar!!{cv(1)}
|   {cv(2)}/|\{cv(1)}
|    {cv(2)}|   Jogue novamente!!{cv(1)}
|   {cv(2)}/ \{cv(1)}
|{cv()}''', end = '  ')
    

# Importaçoes
import string
from chaves import *
from cores import cv
from linhas import *
from menu import *
from random import randint
from time import sleep

# Variaveis
abc = list(string.ascii_uppercase)
abc.append('Ç')
escolha = segredo = ''
sombra = list()
letras = list()
erro = conta = acerto = 0
master = 'OFF'

# Logo
print('Iniciando', end = '')
for ti in range (0,3):
    if ti == 2:
        print('.')
    else:
        print('.', end = '', flush = True)
        sleep(1)

sleep(1)
print(' ', end = '')
ls(4,espace = False)
print(f'''{cv(4)}{"|":<36}{"|"}{cv(0)}
{cv(4)}{"|":<36}{"|"}{cv(0)}
{cv(4)}{"|":<36}{"|"}{cv(0)}
{cv(4)}{"|":<12}{cv(2)}{"JOGO DA FORCA":<24}{cv(4)}{"|"}{cv(0)}
{cv(4)}{"|":<36}{"|"}{cv(0)}
{cv(4)}{"|":<36}{"|"}{cv(0)}''')
ls(4)
print('')
sleep(1)
print(f'{"BY. N.R.":>34}')
sleep(1)
# Inicio
while True:

  if menu() == 'OFF':
    if conta == 0:
      print(f'{cv(1)}{"Você nem jogou ;-;"}')
      print(f'Que sem graça!!{cv()}')
      ls(3)
    else:
      print(f'{cv(2)}{"        Obrigado por jogar!!":}')
      print(f'{"   Espero que tenha se divertido!!"}{cv()}')
      ls(3)
    break
  print('')
  # Cores e alguns Reset
  al1 = cv(randint(3,6))
  al2 = cv(randint(2,6))
  vida = 6
  erro = 0
  
  # Operaçoes de escolhas/ preparo da palavra
  if master == 'OFF':
      lt = randint(0,len(jogos)-1)
      escolha = jogos[lt]
  else:
      escolha = jogos[lt]
  for i, r in escolha.items():
    segredo = i.strip().upper()
    dica = r.strip()

  for l in segredo:
      if l == ' ':
          sombra += ' '
      elif l == '-':
          sombra += '-'
      else:
          sombra += '_'


  while True:
    # Inicio da Forca selecionada
    
    print(f'{cv(5)}Dica: {cv()}{dica}')
    print('')
    print(f'vida: {vida}', end = ' '* 12)
    if acerto == 0:
      print(' ')
    elif acerto == 1:
      print(f'{cv(2)}Acertou {acerto} palavra.{cv()}')
    else:
      print(f'{cv(2)}Acertou {acerto} palavras!!!{cv()}')
    forca()
    print(f'{al2}{" ".join(sombra)} {cv()}')
    print('')
    # Palpite e comparaçao
    
    palpite = ''
    while palpite not in abc:
      palpite = str( input('Letra: ')).strip().upper()
    ls(6)

    if palpite not in letras:
      letras.append(palpite)
      
      if palpite in segredo:
        for i, c in enumerate(segredo):
          if c == palpite:
            sombra[i] = c
          
      else:
        erro += 1
        vida -= 1
    
    else:
      print(f'Letra "{palpite}" Repetida.')
    
    print(f'Letras: {letras}')
    
    # Conclusoes do jogo
    if ''.join(sombra) == segredo:
      acerto += 1
      forca(win = True)
      print(f'{cv(5)}{"Palavra:"} {cv(2)}{segredo}{cv()}')
      print('')
      ls(4)
      jogos.pop(lt)
      break
    
    if vida == 0:
      forca(lose = True)
      print(' ')
      break
  
  if jogos == [] and master == 'OFF':
    master = 'ON'
    ls(4,espace = False)
    print(f'''{cv(4)}{"|":<36}{"|"}{cv(0)}
{cv(4)}{"|":<36}{"|"}{cv(0)}
{cv(4)}{"|":<12}{cv(6)}{"ACHOU FÁCIL!?":<24}{cv(4)}{"|"}{cv(0)}
{cv(4)}{"|":<36}{"|"}{cv(0)}
{cv(4)}{"|":<9}{cv(2)}{"MODO MASTER ATIVADO":<27}{cv(4)}{"|"}{cv(0)}
{cv(4)}{"|":<36}{"|"}{cv(0)}
{cv(4)}{"|":<36}{"|"}{cv(0)}''')
    ls(4)
    for hb in boss:
        jogos.append(hb)
  elif jogos == [] and master == 'ON':
      print(f'''{cv(4)}{"|":<36}{"|"}{cv(0)}
{cv(4)}{"|":<36}{"|"}{cv(0)}
{cv(4)}{"|":<12}{cv(6)}{"JOGO ZERADO!!!":<24}{cv(4)}{"|"}{cv(0)}
{cv(4)}{"|":<36}{"|"}{cv(0)}
{cv(4)}{"|":<9}{cv(2)}{"PARABÉNS DESAFIANTE":<27}{cv(4)}{"|"}{cv(0)}
{cv(4)}{"|":<36}{"|"}{cv(0)}
{cv(4)}{"|":<36}{"|"}{cv(0)}''')
      ls(4)
      break
  sombra.clear()
  letras.clear()
  conta += 1
  sleep(1)

