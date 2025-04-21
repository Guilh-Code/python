# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"


cid = str(input('Em que cidade você nasceu: ')).strip()  
# Pede o nome da cidade e remove espaços no início e no fim com .strip()

print(cid[:5].upper() == 'SANTO')  
# Verifica se os 5 primeiros caracteres da cidade (convertidos para maiúsculas) são "SANTO"
# Isso serve para saber se a cidade começa com "Santo", como "Santo André", "Santos", etc.

