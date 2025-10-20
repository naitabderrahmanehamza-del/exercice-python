fichier = open("Table_de_multiplication.txt", "w")

for i in range(1, 11):
    fichier.write("table de multiplication de " + str(i) + "\n")
    for j in range(1, 11):
        fichier.write(str(i) + " x " + str(j) + " = " + str(i * j) + "\n")
    fichier.write("\n")

fichier.close()
