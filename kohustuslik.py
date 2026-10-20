nimed = []
punktid = []

with open("kontrolltoo.csv", "r", encoding="utf-8") as fail:
    for rida in fail:
        nimi, punkt = rida.strip().split(";")
        nimed.append(nimi)
        punktid.append(int(punkt))


# 2. Hinde määramise funktsioon
def maar_hinne(punkt):
    if punkt >= 90:
        return 5
    elif punkt >= 75:
        return 4
    elif punkt >= 50:
        return 3
    elif punkt >= 20:
        return 2
    else:
        return 1


# 3. Kõikide tulemuste väljastamine
print("KONTROLLTÖÖ TULEMUSED\n")

for i in range(len(nimed)):
    print(f"{i + 1}. {nimed[i]} – {punktid[i]} punkti")


# 4. Statistika arvutamine
opilaste_arv = len(nimed)
keskmine = sum(punktid) / opilaste_arv

parim_punkt = max(punktid)
madalaim_punkt = min(punktid)

# Kõik parima tulemuse saanud õpilased
parimad = []
for i in range(opilaste_arv):
    if punktid[i] == parim_punkt:
        parimad.append(nimed[i])

# Kõik madalaima tulemuse saanud õpilased
madalaimad = []
for i in range(opilaste_arv):
    if punktid[i] == madalaim_punkt:
        madalaimad.append(nimed[i])

# Vähemalt 50 punkti saanud õpilased
sooritasid = sum(1 for punkt in punktid if punkt >= 50)

# Alla 50 punkti saanud õpilased
ei_sooritanud = sum(1 for punkt in punktid if punkt < 50)


# 5. Statistika väljastamine
print("\nKONTROLLTÖÖ STATISTIKA\n")

print(f"Õpilasi kokku: {opilaste_arv}")
print(f"Keskmine punktisumma: {keskmine:.1f}")

for nimi in parimad:
    print(f"Parim tulemus: {nimi} – {parim_punkt} punkti")

for nimi in madalaimad:
    print(f"Madalaim tulemus: {nimi} – {madalaim_punkt} punkti")

print(f"Kontrolltöö sooritas: {sooritasid} õpilast")
print(f"Kontrolltööd ei sooritanud: {ei_sooritanud} õpilast")


# 6. Kõikide õpilaste hinded
print("\nÕPILASTE HINDED\n")

for i in range(opilaste_arv):
    hinne = maar_hinne(punktid[i])
    print(f"{nimed[i]} – {punktid[i]} punkti – hinne {hinne}")


# 7. Õpilase otsimine
print("\nÕPILASE OTSIMINE")

otsitav = input("Sisesta õpilase nimi: ").strip().casefold()

leitud = False

for i in range(opilaste_arv):
    if nimed[i].casefold() == otsitav:
        print(f"Õpilane: {nimed[i]}")
        print(f"Punktid: {punktid[i]}")
        print(f"Hinne: {maar_hinne(punktid[i])}")
        leitud = True
        break

if not leitud:
    print("Sellist õpilast ei leitud.")