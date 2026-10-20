arvud = []

with open("arvud.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        arvud.append(int(rida))

print("Järjend:", arvud)
print("Suurim arv:", max(arvud))
print("Väikseim arv:", min(arvud))
print("Keskmine:", sum(arvud) / len(arvud))

arvud.sort()
print("Kasvav järjekord:", arvud)