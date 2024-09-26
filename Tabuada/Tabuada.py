from função import lc
from função import ls
from time import sleep
while True:
    x = int( input( 'Qual Tab deseja? '))
    lc(f'Tabuáda do {x}',corl=4)
    print('')
    for re in range(0,11):
        ct = f'{x:2}x{re:2}= {re*x:2}'
        for i in ct:
            print(i, end = '', flush = True)
            sleep(0.2)
        print('')
    ls(cor = 4)
    y = ' '
    while y not in 'sn':
        y = str( input('Quer outra tab?[S/N]: '))
    if y == 'n':
        print('')
        print('\033[32mObrigado por usar nosso serviço!!\033[m')
        ls(cor = 4)
        break
    else:
        print('Então.,.', end = ' ')
