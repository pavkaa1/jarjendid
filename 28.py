arvude_arv = 0
summa = 0

with open("arvud.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        arv = int(rida)
        summa += arv
        arvude_arv += 1

print("Arvude arv:", arvude_arv)
print("Arvude summa:", summa)