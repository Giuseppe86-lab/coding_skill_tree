"""Week 001 — Esercizio 2: riepilogo run di modelli.

Difficolta': facile-media
Timebox: 20 minuti
Skill: dizionari, aggregazione, validazione di record

Implementa ``summarize_model_runs(runs)``.

Ogni elemento di ``runs`` e' un dizionario che puo' contenere:

- ``model``: nome del modello;
- ``tokens``: numero di token utilizzati;
- ``success``: esito booleano della run.

Restituisci un dizionario indicizzato per nome del modello. Per ogni modello
valido calcola:

- ``total_runs``: numero di record del modello;
- ``successful_runs``: numero di record in cui ``success is True``;
- ``total_tokens``: somma dei token.

Regole:

- ignora i record senza ``model`` o con ``model`` uguale a ``None``;
- se ``tokens`` manca o vale ``None``, consideralo zero;
- se ``success`` manca, vale ``None`` oppure vale ``False``, non incrementare
  ``successful_runs``;
- puoi assumere che ogni valore non nullo di ``tokens`` sia un intero non
  negativo;
- una lista vuota produce ``{}``;
- non modificare record o lista di input.

Esempio:

    summarize_model_runs([
        {"model": "alpha", "tokens": 120, "success": True},
        {"model": "beta", "tokens": 50, "success": False},
        {"model": "alpha", "tokens": None, "success": True},
    ])

Output atteso:

    {
        "alpha": {
            "total_runs": 2,
            "successful_runs": 2,
            "total_tokens": 120,
        },
        "beta": {
            "total_runs": 1,
            "successful_runs": 0,
            "total_tokens": 50,
        },
    }
"""


def summarize_model_runs(runs):
    """Aggrega run, successi e token per modello."""
    raise NotImplementedError("Completa summarize_model_runs")


# Test visibili: non modificarli.
runs_test = [
    {"model": "alpha", "tokens": 120, "success": True},
    {"model": "beta", "tokens": 50, "success": False},
    {"model": "alpha", "tokens": None, "success": True},
    {"model": "beta", "success": True},
    {"tokens": 999, "success": True},
    {"model": None, "tokens": 300, "success": True},
]
runs_snapshot = [record.copy() for record in runs_test]

assert summarize_model_runs(runs_test) == {
    "alpha": {
        "total_runs": 2,
        "successful_runs": 2,
        "total_tokens": 120,
    },
    "beta": {
        "total_runs": 2,
        "successful_runs": 1,
        "total_tokens": 50,
    },
}
assert summarize_model_runs([]) == {}
assert summarize_model_runs([{"model": "zero", "tokens": 0}]) == {
    "zero": {
        "total_runs": 1,
        "successful_runs": 0,
        "total_tokens": 0,
    }
}
assert runs_test == runs_snapshot

print("Esercizio 2: test visibili superati")

