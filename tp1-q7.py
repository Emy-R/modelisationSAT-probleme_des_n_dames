import datetime

with open ("queens3.cnf", "r") as f:
    text=f.read()
print(text)

n = int(input("taille de l'échiquier : "))

with open ("queensN.cnf", "w") as g:
    g.write("c ROSIN Emy "+ datetime.now()+"\n"+
            "c fichier cnf pour le problème des " + n + " dames" + "\n" +
            "p cnf "+n*n+" "+"."+"\n"+
            "c clauses 'sur chaque ligne il existe au moins une dame'"
            )

