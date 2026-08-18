# Week 003 — Riutilizzare lo stato

Periodo: 2026-08-17 — 2026-08-21

Questa quest verifica se gli invarianti discussi nella Week 002 sono
disponibili su formulazioni nuove. La difficolta' cresce dalla normalizzazione
di stringhe a un report annidato, poi passa a una finestra contigua con un
vincolo di conteggio e a query online su una soglia diversa da zero.

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
- Prima di chiudere un esercizio, confronta la complessita' con il limite
  massimo dichiarato.

## Quest

| # | Esercizio | Difficolta' | Timebox | Skill principali |
|---|---|---:|---:|---|
| 1 | Nomi canonici delle feature | Facile | 15 min | String manipulation, set, ordine stabile |
| 2 | Report delle valutazioni modello | Media | 25 min | Aggregazione annidata, predicati esatti, tie-breaking |
| 3 | Sequenza di richieste affidabile | Media | 30 min | Sliding window, conteggio sotto vincolo |
| 4 | Monitor delle code dei worker | Media-difficile | 35 min | Frequency map, query online, transizioni di soglia |

Tempo target complessivo: **105 minuti**, escluse le note.

## Obiettivi della settimana

- Rendere piu' naturale la manipolazione robusta delle stringhe.
- Costruire un output annidato in una sola scansione.
- Implementare autonomamente una sliding window lineare con un vincolo non
  basato sulla somma dei valori.
- Rispondere a query online rispettando il vincolo di complessita' lineare.
- Registrare per ogni esercizio sia il primo blocco sia la decisione presa.

Nessun singolo risultato assegna mastery a un pattern.
