from datetime import datetime


# ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
# Numéro de la variable pour la case (i, j)
# ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
def var(i, j, n):
    return (i - 1) * n + j


# ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
# Génération des clauses
# ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
def generer_clauses(n):
    clauses = []
    # ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
    # 1. Sur chaque ligne : au moins une dame
    # ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
    for i in range(1, n + 1):
        clause = []
        for j in range(1, n + 1):
            clause.append(var(i, j, n))
        clauses.append(clause)

    # ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
    # 2. Sur chaque colonne : au moins une dame
    # ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
    for j in range(1, n + 1):
        clause = []
        for i in range(1, n + 1):
            clause.append(var(i, j, n))
        clauses.append(clause)

    # ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
    # 3. Sur chaque ligne : au plus une dame
    # ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(j + 1, n + 1):
                clauses.append([
                    -var(i, j, n),
                    -var(i, k, n)
                ])

    # ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
    # 4. Sur chaque colonne : au plus une dame
    # ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            for k in range(i + 1, n + 1):
                clauses.append([
                    -var(i, j, n),
                    -var(k, j, n)
                ])

    # ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
    # 5. Sur chaque diagonale : au plus une dame
    # ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for i2 in range(i + 1, n + 1):
                for j2 in range(1, n + 1):
                    if abs(i - i2) == abs(j - j2):
                        clauses.append([
                            -var(i, j, n),
                            -var(i2, j2, n)
                        ])
    return clauses


# ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
# Écriture du fichier DIMACS
# ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
def creer_fichier(n):
    clauses = generer_clauses(n)
    nom_fichier = "queens" + str(n) + ".cnf"
    with open(nom_fichier, "w") as f:
        # Commentaire
        f.write("c ROSIN Emy " +
                datetime.now().strftime("%d/%m/%Y %H:%M") +
                "\n")
        f.write("c fichier cnf pour le probleme des " +
                str(n) + " dames\n")
        # En-tête
        f.write("p cnf " + str(n * n) + " " +
                str(len(clauses)) + "\n")
        # Clauses
        for clause in clauses:
            f.write(" ".join(map(str, clause)) + " 0\n")
    print("Fichier créé :", nom_fichier)
    print("Nombre de variables :", n * n)
    print("Nombre de clauses :", len(clauses))


# ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
# Programme principal
# ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
n = int(input("Taille de l'échiquier : "))
if n <= 0:
    print("La taille doit être un entier positif.")
else :
    creer_fichier(n)