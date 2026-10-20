temperatuurid = [12, 18, 25, 9, 31, 22, 16, 28, 7]

soojad = []
jahedad = []

for t in temperatuurid:
    if t >= 20:
        soojad.append(t)
    else:
        jahedad.append(t)

print(soojad)
print(jahedad)