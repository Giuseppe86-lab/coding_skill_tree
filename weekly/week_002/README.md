# Week 002 — Stato incrementale

Periodo: 2026-08-10 — 2026-08-14

Questa quest riprende i due punti emersi nella review precedente: tradurre i
predicati in modo letterale e implementare autonomamente una sliding window
lineare. Frequency map e aggregazione vengono allenate con stato e regole di
parita' piu' articolate rispetto alla prima settimana.

Tutti gli esercizi, gli esempi e i test visibili sono raccolti in
`quest.ipynb`. Usa `notes.md` per registrare il processo mentre lavori.

## Regole

- Leggi tutti e quattro gli esercizi prima di scegliere l'ordine.
- Avvia un timer separato per ogni esercizio.
- Se superi il timebox, annota il blocco e passa oltre.
- Non usare AI, soluzioni online o autocomplete generativo.
- Modifica soltanto le celle delle funzioni, non i test.
- Esegui i test visibili; Codex preparera' edge case e test di performance
  aggiuntivi durante la review.
- Punta prima a una soluzione semplice e corretta, poi verifica che la sua
  complessita' sia compatibile con i vincoli.

## Quest

| # | Esercizio | Difficolta' | Timebox | Skill principali |
|---|---|---:|---:|---|
| 1 | Alert confermati per servizio | Facile | 15 min | Predicati esatti, dict |
| 2 | Firma dominante degli incidenti | Media | 20 min | Aggregazione, frequency map, tie-breaking |
| 3 | Batch piu' lungo entro il budget | Media | 30 min | Sliding window, complessita' |
| 4 | Registro dinamico dei modelli | Media | 30 min | Frequency map, query online, stato incrementale |

Tempo target complessivo: **95 minuti**, escluse le note.

## Obiettivi della settimana

- Tradurre esattamente una condizione della specifica.
- Evitare scansioni ripetute quando lo stato puo' essere aggiornato.
- Implementare sliding window in autonomia su uno scenario diverso dai
  timestamp.
- Registrare almeno il primo blocco e la decisione presa per ogni esercizio.

Nessun singolo risultato assegna mastery a un pattern.

