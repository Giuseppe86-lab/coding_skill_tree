# Week 003 — Review

Stato: completata e verificata il 2026-08-19.

## Risultato complessivo

- Esercizi completati: 4/4
- Esercizi pienamente corretti rispetto a specifica e vincoli: 2/4
- Esercizi corretti sugli output ma non conformi alla scala: 1/4
- Esercizi con errori nelle transizioni: 1/4
- Tempo totale dichiarato: 89 minuti su 105
- XP ottenuti: +40
- Valutazione sintetica: 7/10
- Pattern allenati: string manipulation, deduplicazione stabile, aggregazione
  annidata, predicati esatti, sliding window, query online
- Pattern eventualmente consolidati: sliding window in forte consolidamento;
  prima implementazione autonoma O(n), corretta ed entro il timebox

## Valutazione

| Esercizio | Correttezza | Complessita' | Leggibilita' | Edge case | Pattern recognition | Timebox |
|---|---|---|---|---|---|---|
| 1 | Output corretti | O(c + n*u) tempo nel caso generale, O(u) spazio | Semplice e comprensibile; `strip()` nel generatore e' ridondante | 1.000 casi casuali, whitespace e non mutazione superati | Normalizzazione riconosciuta; manca il set per deduplicare in scala | 9/15 min |
| 2 | Corretta | O(n+m) tempo, O(m) spazio | Costruzione annidata corretta; ricerca finale del leader e nomi intermedi sono piu' complessi del necessario | 1.000 confronti casuali conformi al contratto, tie-breaking e non mutazione superati | Lookup annidato, predicato esatto e tie-breaking riconosciuti | 45/25 min |
| 3 | Corretta | O(n) tempo, O(1) spazio | Chiara, con nomi coerenti e invariante leggibile | 2.000 confronti casuali, confini 500/599, input vuoto, limite zero, errore e non mutazione superati | Sliding window riconosciuta e implementata autonomamente | 16/30 min |
| 4 | Test visibili superati; transizioni generali errate | O(n+q) tempo medio, O(m+r) spazio | Flusso leggibile, ma quattro `if` separati rendono meno evidente l'esclusivita' dei comandi | Falliscono incrementi gia' oltre soglia e completamenti che restano sotto soglia | Stato aggregato mantenuto, ma le transizioni non sono ancora modellate esattamente | 19/35 min |

Nel punto relativo all'esercizio 1, `c` e' il numero totale di caratteri,
`n` il numero di nomi e `u` il numero di nomi canonici distinti gia' prodotti.
Nel caso peggiore il controllo nella lista rende il tempo quadratico in `n`.

## Cosa e' andato bene

- La sliding window e' il progresso principale della settimana: la finestra
  persiste, `right` aggiunge, `left` rimuove e il conteggio degli errori resta
  sincronizzato con il segmento corrente.
- L'esercizio 3 supera 2.000 confronti casuali con un oracolo esaustivo e
  gestisce 200.000 elementi in circa 0,02 secondi.
- Nell'esercizio 2 il predicato `passed is True` e' tradotto correttamente e
  il tie-breaking conserva la prima apparizione grazie all'ordine dei dict.
- L'esercizio 2 supera 1.000 confronti casuali e gestisce 100.000 record in
  circa 0,06 secondi.
- Tutte le submission preservano gli input.
- Tre esercizi sono stati chiusi entro il timebox; il tempo totale resta sotto
  il budget complessivo nonostante il forte sforamento dell'esercizio 2.

## Primo problema importante

Nell'esercizio 4 `overloaded_worker` viene modificato quando il conteggio e'
semplicemente oltre o sotto la soglia, non soltanto quando la attraversa.
Con limite 1, un passaggio da 2 a 3 job mantiene il worker sovraccarico e non
deve incrementare di nuovo l'aggregato; analogamente, un passaggio da 1 a 0
non rimuove un worker sovraccarico, perche' non lo era gia' prima.

Il test inizialmente aggiunto per `enqueue` su un worker assente non viene
considerato nella valutazione: il testo dice che l'operazione aggiunge un job,
ma non definisce esplicitamente la creazione di un worker nuovo. L'ambiguita'
della specifica e' responsabilita' dell'autore dell'esercizio, non della
submission.

## Domanda o hint minimo

Prima di aggiornare il conteggio di un worker, confronta due stati booleani:
era sovraccarico prima dell'operazione ed e' sovraccarico dopo? L'aggregato
cambia soltanto se i due stati sono diversi.

## Altri problemi rilevanti

### Esercizio 1 — deduplicazione

`name_clean not in risultato` scorre una lista crescente. Il benchmark con
nomi tutti distinti misura circa 0,05 s su 3.000 elementi, 0,22 s su 6.000 e
0,84 s su 12.000: il tempo quadruplica quando l'input raddoppia. La lista serve
per l'ordine; una struttura separata deve rendere costante il controllo di
appartenenza.

## Test aggiuntivi di review

- Esercizio 1: 1.000 input casuali con spazi, tab, newline, duplicati, stringhe
  vuote e verifica di non mutazione; output tutti corretti. Benchmark di scala
  non conforme alla dimensione massima.
- Esercizio 2: 1.000 confronti casuali limitati al contratto esplicito, con
  `passed` presente nei record validi, valori truthy non booleani, campi
  esplicitamente opzionali, parita' e non mutazione; tutto superato. Benchmark
  su 100.000 record completato in circa 0,06 secondi.
- Esercizio 3: 2.000 confronti casuali con oracolo esaustivo, confini HTTP,
  input vuoto, limite negativo e benchmark su 200.000 elementi; tutto
  superato.
- Esercizio 4: transizioni mirate e sequenze casuali confrontate con un
  oracolo, escludendo il caso ambiguo di `enqueue` su worker assente. Restano
  due errori indipendenti: `[2, 2]` invece di `[1, 1]` quando un worker resta
  sopra soglia e `[-1]` invece di `[0]` quando un worker resta sotto soglia.

## Dati di processo

Ordine, motivazione, rischio percepito, pattern e tempi sono compilati. Le
sezioni su blocchi, decisioni e debrief sono ancora vuote. L'esercizio 2 ha
superato il timebox di 20 minuti: in una simulazione sarebbe stato preferibile
fermarlo a 25 minuti, proteggere gli altri esercizi e tornarci alla fine.

## Regola pratica da salvare

- Se serve sia ordine stabile sia membership veloce, usare due strutture con
  responsabilita' diverse: lista per l'output e set per gli elementi gia'
  visti.
- Un aggregato di stato cambia soltanto quando l'entita' attraversa la soglia,
  non a ogni aggiornamento eseguito oltre la soglia.

## Decisione sui pattern

- Sliding window: forte consolidamento, ma non ancora mastery. Serve almeno
  un'altra soluzione autonoma, corretta e lineare su una formulazione diversa.
- Predicati esatti: applicati correttamente una seconda volta, ma l'esercizio
  e' fuori timebox; restano da consolidare sotto pressione temporale.
- Query online incrementali: la complessita' obiettivo e' stata riconosciuta,
  ma la logica delle transizioni di soglia non e' ancora acquisita.

## XP

- +40 XP: esercizio 3 medio, corretto ed efficiente entro il timebox.
- Nessun XP per l'esercizio 1: output corretti ma scala non rispettata.
- Nessun XP per l'esercizio 2: corretto, ma timebox superato.
- Nessun XP per l'esercizio 4: errori di correttezza nelle transizioni.
- Totale Week 003: +40 XP.

## Priorita' per Week 004

- Riproporre una sliding window diversa per verificare il consolidamento senza
  ripetere il conteggio degli errori HTTP.
- Allenare transizioni rispetto a una soglia con casi che restano sopra o
  sotto la soglia per piu' aggiornamenti consecutivi.
- Consolidare output annidati con un esercizio piu' corto e un timebox rigido.
- Richiedere deduplicazione stabile su un input grande.
- Completare blocchi, decisioni e debrief nelle note.

## Dispensa progressiva

La Week 003 richiede un capitolo aggiuntivo: documentera' la prima sliding
window autonoma O(n), la deduplicazione stabile efficiente e la generalizzazione
delle transizioni di soglia. La stesura viene lasciata come ultimo passaggio
dopo il feedback puntuale, per non anticipare le implementazioni complete.
