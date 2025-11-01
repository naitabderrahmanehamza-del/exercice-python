with open("table_de_multiplication.txt", "w") as f:
    for c in range(1, 11):
        f.write(f"Table de multiplication de {c} :\n")
        for i in range(0, 11):
            f.write(f"{c} * {i} = {c*i}\n")
        f.write("\n")
