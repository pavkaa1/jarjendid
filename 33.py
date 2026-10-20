hinded = [4, 5, 3, 4, 2, 5, 5, 3, 4, 5, 2, 4]

print("Hinnete koguarv:", len(hinded))
print("Keskmine hinne:", round(sum(hinded) / len(hinded), 2))

# Hinnete esinemiste arv
for hinne in range(1, 6):
    arv = hinded.count(hinne)
    print("Hinne", hinne, "esines", arv, "korda")

# Kõige sagedamini esinev hinne
sagedaim = max(hinded, key=hinded.count)
print("Kõige sagedamini esinev hinne:", sagedaim)

# Positiivsed ja mitterahuldavad hinded
positiivsed = 0
mitterahuldavad = 0

for hinne in hinded:
    if hinne >= 3:
        positiivsed += 1
    else:
        mitterahuldavad += 1

print("Positiivseid hindeid:", positiivsed)
print("Mitterahuldavaid hindeid:", mitterahuldavad)

# Tekstiline diagramm
print("\nHinnete jaotus:")
for hinne in range(1, 6):
    print("Hinne", hinne, ":", "*" * hinded.count(hinne))