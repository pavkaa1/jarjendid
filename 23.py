sonad = ["arvuti", "programmeerimine", "hiir", "klaviatuur", "monitor"]

pikim = sonad[0]
luhim = sonad[0]

for sona in sonad:
    if len(sona) > len(pikim):
        pikim = sona
    if len(sona) < len(luhim):
        luhim = sona

print("Kõige pikem sõna:", pikim, "- pikkus:", len(pikim))
print("Kõige lühem sõna:", luhim, "- pikkus:", len(luhim))