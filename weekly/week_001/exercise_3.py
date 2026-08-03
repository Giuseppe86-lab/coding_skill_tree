"""Week 001 — Esercizio 3: coppie compatibili tra dataset.

Difficolta': media
Timebox: 20 minuti
Skill: hash map, frequency count, complessita'

Implementa ``count_compatible_pairs(left_scores, right_scores, target)``.

La funzione riceve due liste di interi. Restituisci il numero di coppie di
indici ``(i, j)`` tali che:

    left_scores[i] + right_scores[j] == target

Regole:

- lo stesso valore puo' comparire piu' volte e ogni combinazione di indici
  valida deve essere contata;
- valori negativi e zero sono ammessi;
- se una delle liste e' vuota, restituisci zero;
- non modificare gli input;
- la soluzione deve rispettare liste che possono contenere fino a 100.000
  elementi ciascuna.

Esempio:

    count_compatible_pairs([1, 1, 3], [2, 4, 2], 5)
    # Output atteso: 4

Le quattro coppie sono generate dai due ``1`` con il ``4`` e dal ``3`` con
ciascuno dei due ``2``.
"""


def count_compatible_pairs(left_scores, right_scores, target):
    """Conta tutte le coppie di indici con somma uguale al target."""
    raise NotImplementedError("Completa count_compatible_pairs")


# Test visibili: non modificarli.
assert count_compatible_pairs([1, 1, 3], [2, 4, 2], 5) == 4
assert count_compatible_pairs([], [1, 2], 3) == 0
assert count_compatible_pairs([0, 0], [0, 0, 0], 0) == 6
assert count_compatible_pairs([-2, 5, 5], [7, 0, -3], 5) == 3
assert count_compatible_pairs([1, 2, 3], [10], 99) == 0

print("Esercizio 3: test visibili superati")

