"""Week 001 — Esercizio 1: flagged digits nei ticket.

Difficolta': facile
Timebox: 15 minuti
Skill: string manipulation, frequency count, edge case

Implementa ``count_flagged_digits(ticket_ids, flagged_digits)``.

``ticket_ids`` e' una lista di interi non negativi.
``flagged_digits`` e' una lista di cifre intere comprese tra 0 e 9, senza
duplicati.

Restituisci un dizionario che associa a ogni cifra richiesta il numero totale
di occorrenze nelle rappresentazioni decimali di tutti i ticket ID.

Regole:

- tutte le cifre di ``flagged_digits`` devono comparire nel risultato, anche
  quando il conteggio e' zero;
- l'ordine delle chiavi segue ``flagged_digits``;
- ticket ID ripetuti contano ogni volta;
- il ticket ID ``0`` contiene una singola cifra zero;
- una lista vuota di ticket produce conteggi tutti uguali a zero;
- gli input non devono essere modificati.

Esempio:

    count_flagged_digits([204, 17, 220, 0], [0, 2, 7])
    # Output atteso: {0: 3, 2: 3, 7: 1}
"""


def count_flagged_digits(ticket_ids, flagged_digits):
    """Conta le occorrenze delle cifre segnalate nei ticket ID."""
    raise NotImplementedError("Completa count_flagged_digits")


# Test visibili: non modificarli.
assert count_flagged_digits([204, 17, 220, 0], [0, 2, 7]) == {
    0: 3,
    2: 3,
    7: 1,
}
assert count_flagged_digits([], [1, 5]) == {1: 0, 5: 0}
assert count_flagged_digits([111, 10, 1], [1, 0, 9]) == {1: 5, 0: 1, 9: 0}
assert count_flagged_digits([0, 0], [0]) == {0: 2}

print("Esercizio 1: test visibili superati")

