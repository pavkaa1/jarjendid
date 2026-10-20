ostukorv = []

for i in range(5):
    toode = input("Sisesta toote nimetus: ")
    ostukorv.append(toode)

print("Ostukorv:", ostukorv)
print("Toodete arv:", len(ostukorv))