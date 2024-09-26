def cv(cor= 0):
  '''
   cores:
   1 = VERMELHO
   2 = VERDE
   3 = AMARELO
   4 = AZUL
   5 = ROXO
   6 = Ciano
   7 = CINZA
  '''
  if cor < 0 or cor > 7:
    tip = 'Erro nas cores'
  else:
    if cor == 0:
      tip = f'\033[m'
    else:
      tip = f'\033[3{cor}m'
  return tip
