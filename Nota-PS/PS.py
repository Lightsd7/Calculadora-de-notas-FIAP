media1 = float(input("Média 1ºSemestre: "))
nac = float(input("Nota NAC: "))*0.2
total = media1+nac
falta = 12 - total
precisa = (falta - 2.22)/0.5
nota = round(precisa, 2)

print("Você precisa tirar " + str(nota) + " na PS.")
if nota>=6.9:
    print("Comece a estudar agora!!")