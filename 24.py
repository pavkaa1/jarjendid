laused = [
    "Täna õpime Pythonit",
    "Järjendid on väga kasulikud",
    "Programmeerimine nõuab harjutamist",
    "Tartu on ilus linn"
]

kokku = 0

for lause in laused:
    markide_arv = len(lause)
    a_arv = lause.lower().count("a")
    kokku += a_arv

    print("Lause:", lause)
    print("Tähemärkide arv:", markide_arv)
    print("Tähe a esinemiste arv:", a_arv)
    print()

pikim_lause = max(laused, key=len)

print("Tähe a esinemisi kokku:", kokku)
print("Kõige pikem lause:", pikim_lause)
print("Pikima lause tähemärkide arv:", len(pikim_lause))