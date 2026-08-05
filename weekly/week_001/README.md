# Week 001 — Baseline controllata

Periodo: 2026-08-03 — 2026-08-07

Questa prima quest misura quanto i pattern gia' incontrati sono disponibili in
autonomia e introduce una sliding window su un caso backend realistico.

Tutti gli esercizi, gli esempi e i test visibili sono raccolti in
`quest.ipynb`. Usa `notes.md` per registrare tempi e ragionamento senza
appesantire il flusso del notebook.

## Regole

- Prima di iniziare, leggi tutti e quattro gli esercizi.
- Scrivi in `notes.md` l'ordine scelto e il motivo.
- Avvia un timer separato per ogni esercizio.
- Se superi il timebox, annota il punto di blocco e passa oltre.
- Non usare AI, soluzioni online o autocomplete generativo.
- Non modificare gli assert per farli passare.
- Esegui i test visibili; gli edge case e i test di performance aggiuntivi
  saranno preparati da Codex durante la review.
- Punta prima a una soluzione semplice e corretta; valuta eventuali
  ottimizzazioni soltanto dopo.

## Quest

| # | Esercizio | Difficolta' | Timebox | Skill principali |
|---|---|---:|---:|---|
| 1 | Flagged digits nei ticket | Facile | 15 min | String manipulation, frequency count |
| 2 | Riepilogo run di modelli | Facile-media | 20 min | Dict, aggregazione, edge case |
| 3 | Coppie compatibili tra dataset | Media | 20 min | Hash map, frequency count |
| 4 | Finestra di traffico piu' intensa | Media | 30 min | Sliding window, time series |

Tempo target complessivo: **85 minuti**, esclusa la compilazione delle note.

## Criteri di review

La review del venerdi' valutera':

- correttezza sui test visibili e su edge case aggiuntivi;
- complessita' temporale e spaziale;
- leggibilita' e scelta dei nomi;
- assenza di mutazioni non richieste;
- pattern riconosciuto prima di scrivere codice;
- rispetto del timebox;
- comportamento sui test aggiuntivi preparati durante la review.

Un singolo esercizio corretto non assegna mastery a un pattern.
