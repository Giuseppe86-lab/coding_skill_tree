"""Week 001 — Esercizio 4: finestra di traffico piu' intensa.

Difficolta': media
Timebox: 30 minuti
Skill: sliding window, time series, edge case

Implementa ``max_requests_in_window(timestamps, window_seconds)``.

``timestamps`` contiene timestamp interi ordinati in modo non decrescente.
Ogni timestamp rappresenta una richiesta ricevuta da un servizio.

Per ogni possibile istante iniziale ``start``, una finestra contiene tutte le
richieste con timestamp nell'intervallo semiaperto:

    start <= timestamp < start + window_seconds

Restituisci il massimo numero di richieste contenute in una singola finestra.

Regole:

- timestamp duplicati rappresentano richieste distinte;
- ``timestamps`` vuoto produce zero;
- se ``window_seconds <= 0``, solleva ``ValueError``;
- gli input non devono essere modificati;
- la funzione deve gestire fino a 200.000 timestamp entro il timebox di un
  coding assessment.

Esempio:

    max_requests_in_window([1, 2, 4, 7, 8], 4)
    # Output atteso: 3

La finestra ``[1, 5)`` contiene le richieste ai timestamp 1, 2 e 4.
"""


def max_requests_in_window(timestamps, window_seconds):
    """Restituisce il picco di richieste in una finestra temporale."""
    raise NotImplementedError("Completa max_requests_in_window")


# Test visibili: non modificarli.
assert max_requests_in_window([1, 2, 4, 7, 8], 4) == 3
assert max_requests_in_window([], 10) == 0
assert max_requests_in_window([5, 5, 5], 1) == 3
assert max_requests_in_window([1, 5, 9], 4) == 1
assert max_requests_in_window([0, 3, 4, 7, 8, 9], 5) == 3

try:
    max_requests_in_window([1, 2, 3], 0)
except ValueError:
    pass
else:
    raise AssertionError("window_seconds <= 0 deve sollevare ValueError")

print("Esercizio 4: test visibili superati")

