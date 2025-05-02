lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
# Tuplas são imutáveis


for comida in lanche:
    print(f"Eu vou comer {comida}")


for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]}")


for pos, c in enumerate(lanche):
    print(f"Eu vou comer {c} na posição {pos}") 


print("Comi pra caramba!!!") 


print(sorted(lanche))