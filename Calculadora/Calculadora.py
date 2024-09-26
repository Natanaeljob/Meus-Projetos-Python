def menu():
    global resp
    global op
    print( """
[1]Nova {tip}
[2]Continuar
[3]Encerrar
 """ )
    op = 0
    


print("Calculator")
cores = {
"vermelho" :  "\033[31m" ,
"verde"    :  "\033[32m" ,
"amarelo"  :  "\033[33m" ,
"azul"     :  "\033[34m" ,
"roxo"     :  "\033[35m" ,
"ciano"    :  "\033[36m" ,
"f"        :  "\033[m"
}

escolha = r = n = n1 = n2 = op = 0

caixa = []

while escolha != 7:

    escolha = resp = r = n = n1 = n2 = op = 0

    print("""
{}
                       |
[1] {}Somar{}              |
[2] {}Subtrair{}           |
[3] {}Multiplicar{}        |
[4] {}Dividir{}            |
[5] {}Raiz quadrada{}      |
[6] {}%{}                  |
[7] FECHAR CALCULADORA |
{}
""".format("_"*24,
    cores["azul"], cores["f"], cores["vermelho"], cores["f"], cores["verde"], cores["f"],
    cores["ciano"], cores["f"], cores["roxo"], cores["f"], cores["amarelo"], cores["f"],
    "_"*24) )

    escolha = int( input( " O que quer fazer? " ) )
    
    if escolha == 1:
        while True:
            tip = 'soma'
            print("{}{:_^36}{}".format(cores["azul"], "Somar", cores["f"] ) )
            print("=+"*18)
            qtdd = int(input(" Quantos números quer somar? " ) )
            for re in range(0,qtdd):
                print("=+"*18)
                resp += float( input( " {} número ".format(re+1) ) )
            print("=+"*18)
            if resp.is_integer() == True:
                resp = int(resp)
            else:
                resp = "{:.2f}".format(resp)
            print("")
            print(" {}Soma = {}{}".format( cores["azul"], resp, cores["f"] ) )
            
            menu()
            while 0 == op or op > 3:
                op = int(input())
            if op == 1:
                resp = 0
            if op == 3:
                break
            
    if escolha == 2:
        while op != 3:
            print("{}Subtrair{}:".format(cores["vermelho"], cores["f"] ) )
            if r != 0:
                print("=-"*18)
                n1 = float( input( "Número: " ) )
                print("=-"*18)
                r = r - n1
            else:
                print("=-"*18)
                n1 = float( input( "1° número: " ) )
                print("=-"*18)
                n2 = float( input( "2° número: " ) )
                print("=-"*18)
                r = n1 - n2
            if r.is_integer() == True:
                r = int(r)
            else:
                r = "{:.2f}".format(r)
            print("")
            print(" {}Sub. = {}{}".format(cores["vermelho"], r, cores["f"]))
            op = int( input( """
[1]Nova sub.
[2]Continuar
[3]Encerrar
 """ ))
            if op == 1:
                r = 0
            
           
    if escolha == 3:
        while op != 3:
            print("{}Multiplicar{}:".format(cores["verde"], cores["f"] ) )
            if r != 0:
                print("=x"*18)
                n1 = float( input( "Número: " ) )
                print("=x"*18)
                r = r * n1
            else:
                print("=x"*18)
                n1 = float( input( "1° número: " ) )
                print("=x"*18)
                n2 = float( input( "2° número: " ) )
                print("=x"*18)
                r = n1 * n2
            if r.is_integer() == True:
                r = int(r)
            else:
                r = "{:.2f}".format(r)
            print("")
            print(" {}Multi. = {}{}".format(cores["verde"], r, cores["f"]))
            op = int( input( """
[1]Nova multi.
[2]Continuar
[3]Encerrar
 """ ))
            if op == 1:
                r = 0


    if escolha == 4:
        while op != 3:
            print("{}Dividir{}:".format(cores["ciano"], cores["f"] ) )
            if r != 0:
                print("=/"*18)
                n1 = float( input( "Número: " ) )
                print("=/"*18)
                r = r / n1
            else:
                print("=/"*18)
                n1 = float( input( "1° número: " ) )
                print("=/"*18)
                n2 = float( input( "2° número: " ) )
                print("=/"*18)
                r = n1 / n2
            if r.is_integer() == True:
                r = int(r)
            else:
                r = "{:.2f}".format(r)
            print("")
            print(" {}Divisão = {}{}".format(cores["ciano"], r, cores["f"]))
            op = int( input( """
[1]Nova divisão
[2]Continuar
[3]Encerrar
 """ ))
            if op == 1:
                r = 0


    if escolha == 5:
        while op != 2:
            print("{}Raiz{}:".format(cores["roxo"], cores["f"] ) )

            n = int( input( """
[1] Raiz quadrada
[2] Raiz avançada
 
 """ ) )
            if n == 1:
                print("=~"*18)
                r = float( input( "Número: " ) )
                print("=~"*18)
                r = r ** (1/2)
            else:
                print("=~"*18)
                r = float( input( "Número: " ) )
                print("=~"*18)
                n1 = float( input( "Expoente: " ) )
                print("=~"*18)
                r = r ** (1/n1)
            if r.is_integer() == True:
                r = int(r)
            else:
                r = "{:.2f}".format(r)
            print("")
            print(" {}Raiz = {}{}".format(cores["roxo"], r, cores["f"]))
            op = int( input( """
[1]Nova Raiz
[2]Encerrar
 """ ))
            if op == 1:
                r = 0


    if escolha == 6:
        while op != 2:
            print("{}%{}:".format(cores["amarelo"], cores["f"] ) )
            print(" Digite 1 em número para ver %")
            print(" Direta de 100")
            print("")
            print("=✓"*18)
            n1 = float( input( " Número " ) )
            print("=✓"*18)
            n2 = float( input( " % " ) )
            print("=✓"*18)
            if n1 == 0:
               n1 = 1
            r = n1 * (n2/100)
            if r.is_integer() == True:
                r = int(r)
            else:
                r = "{:.2f}".format(r)
            print("")
            print(" {}% = {}{}".format(cores["amarelo"], r, cores["f"]))
            op = int( input( """
[1]Nova %
[2]Encerrar
 """ ))
            if op == 1:
                r = 0

print("!!!{}Obrigado por usar nosso serviço{}!!!".format(cores["verde"],cores["f"] ) )