# TP3 — Logique

> TP de modélisation en logique propositionnelle et utilisation de solveurs SAT.

---

## Au programme

- Modélisation en **logique propositionnelle**
- Formules sous forme **CNF**
- Problème des **n dames**
- Génération de fichiers **DIMACS**
- Utilisation de **MiniSat**
- Fonctions, injections, surjections et bijections

---

## Problème des n dames

Le problème consiste à placer `n` dames sur un échiquier `n × n` sans qu'elles puissent se menacer entre elles.

### Contraintes

- Une dame **au moins** sur chaque ligne
- Une dame **au plus** sur chaque ligne
- Une dame **au moins** sur chaque colonne
- Une dame **au plus** sur chaque colonne
- Au plus une dame sur chaque diagonale

L'objectif est ensuite de transformer cette modélisation en formule **CNF**, puis de générer automatiquement un fichier **DIMACS** utilisable par un solveur SAT.

---

## 📄 Format DIMACS

Quelques éléments importants :

| Élément | Signification |
|:---:|---|
| `1` | Proposition 1 |
| `-1` | Négation de la proposition 1 |
| `0` | Fin d'une clause |
| `p cnf` | Déclaration du problème |
| `c` | Commentaire |

### Exemple

```text
c Exemple
p cnf 3 2
1 -2 0
2 3 -1 0
```

### Notes
Quelques rappels personnels sur les notions vues pendant le TP.
- Les variables propositionnelles représentent la présence ou l'absence d'une dame sur une case.
- Une formule CNF est constituée de clauses reliées par des ET.
- Chaque clause contient des littéraux reliés par des OU.
- Le format DIMACS permet de transmettre une formule à un solveur SAT.

> L'énoncé du TP n'est pas présent dans ce dépôt car il s'agit d'un document fourni par l'université.
