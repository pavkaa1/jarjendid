muugid = [125.50, 210.00, 98.75, 340.20, 185.40, 420.00, 275.90]

paevad = ["Esmaspäev", "Teisipäev", "Kolmapäev",
          "Neljapäev", "Reede", "Laupäev", "Pühapäev"]

# Iga päeva müügisumma
for i in range(len(muugid)):
    print(paevad[i] + ":", f"{muugid[i]:.2f}", "eurot")

# Nädala kogumüük ja keskmine päevamüük
kogumyyk = sum(muugid)
keskmine = kogumyyk / len(muugid)

print("\nNädala kogumüük:", f"{kogumyyk:.2f}", "eurot")
print("Keskmine päevamüük:", f"{keskmine:.2f}", "eurot")

# Suurima müügiga päev
suurim = max(muugid)
indeks = muugid.index(suurim)

print("Suurim müük:", f"{suurim:.2f}", "eurot")
print("Suurima müügiga päev:", paevad[indeks])

# Päevad, mil müük ületas 200 eurot
arv = 0

for myyk in muugid:
    if myyk > 200:
        arv += 1

print("Üle 200 euro müügiga päevi:", arv)