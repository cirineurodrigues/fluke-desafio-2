def makeCircle(raio):
    # calcular diâmetro
    diameter = (raio * 2) - 1

    # pelo exemplo percebi que caso o raio for par, o numero de caracteres contidos no meio é igual a raio + 1, caso seja ímpar é igual ao próprio raio
    middle = raio
    if raio % 2 == 0:
        middle = raio + 1
    
    # calculo da quantidade de linhas nas extremidades, que seria o diâmetro menos os caracteres contidos no meio divido por dois, pois são duas extremidades
    extremeties = int((diameter - middle)/2)

    # calculo da quantidade de linhas da extremidade superior
    topStart = diameter - (extremeties * 2)

    # calculo da quantidade de espaços inicial de espaços para realizar o desenho
    space = extremeties * 2


    for i in range (0, diameter):
        if i < extremeties:
            print(f'{" " * space}{"x " * topStart}')
            space -= 2
            topStart += 2
        elif i < middle + extremeties:
            print(f'{"x " * diameter}')
        else:
            space += 2
            topStart -= 2
            print(f'{" " * space}{"x " * topStart}')


makeCircle(5)



