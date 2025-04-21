''' Cores no Terminal

                      ANSI
                 escape sequence   
                      \033[m

                Ex:  \033[0:33:44m

     STYLE            TEXT            BACK         

    0 - None        30 - Black      40 - black
    1 - Bold        31 - Red        41 - red 
    4 - Underline   32 - Green      42 - green
    7 - Negative    33 - Yellow     43 - yellow
                    34 - Blue       44 - blue
                    35 - Purple     45 - purple
                    36 - Cyan       46 - cyan
                    37 - White      47 - white
'''
# Exemplos:
print("\033[1;37;42m Olá, Mundo! \033[m")
print("\033[1;31;47m Alerta vermelho! \033[m")

a = 3
b = 5
print(f"Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m ")

nome = 'Guilherme'
cores = {'limpa' : '\033[m', 
      'azul': '\033[34m', 
      'amarelo': '\033[33m', 
      'pretoebranco': '\033[7;30m'
    }

print(f'Olá, Muito prazer em te conhecer, \033[4;34m{nome}\033[m !!!')
