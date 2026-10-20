temperatuurid = []

with open("temperatuurid.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        temperatuurid.append(int(rida))

print("Mõõtmisi:", len(temperatuurid))
print("Keskmine temperatuur:", round(sum(temperatuurid) / len(temperatuurid), 1), "°C")
print("Kõrgeim temperatuur:", max(temperatuurid), "°C")
print("Madalaim temperatuur:", min(temperatuurid), "°C")

miinuskraadid = 0
vahemalt_viis = 0

for temperatuur in temperatuurid:
    if temperatuur < 0:
        miinuskraadid += 1
    if temperatuur >= 5:
        vahemalt_viis += 1

print("Miinuskraadidega päevi:", miinuskraadid)
print("Vähemalt 5-kraadiseid päevi:", vahemalt_viis)