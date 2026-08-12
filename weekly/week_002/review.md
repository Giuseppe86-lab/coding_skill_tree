# Week 002 — Review

Stato: completata e verificata il 2026-08-11.

## Risultato complessivo

- Esercizi completati: 4/4
- Esercizi corretti rispetto a specifica e vincoli: 2/4
- Esercizi corretti sugli output ma non conformi alla scala: 2/4
- Tempo totale dichiarato: 74 minuti su 95
- XP ottenuti: +25
- Pattern allenati: predicati esatti, aggregazione, frequency map, sliding
  window, query online
- Pattern eventualmente consolidati: nessuna nuova mastery; predicati esatti
  applicati correttamente una volta dopo l'errore della Week 001

## Valutazione

| Esercizio | Correttezza | Complessita' | Leggibilita' | Edge case | Pattern recognition | Timebox |
|---|---|---|---|---|---|---|
| 1 | Corretta | O(n) tempo, O(k) spazio | Chiara; confronto con `None` migliorabile con `is None` | Predicati truthy eterogenei, servizio vuoto e non mutazione superati | Lookup e predicato esatto riconosciuti | 14/15 min |
| 2 | Corretta | O(n+u) tempo, O(u) spazio | Buona separazione tra output e frequenze di supporto | Parita', ordine, campi mancanti, stringhe vuote e non mutazione superati | Aggregazione e frequency map riconosciute | 27/20 min |
| 3 | Output corretti, scala non rispettata | O(n^2) tempo, O(1) spazio | Comprensibile, ma variabili `left` e `j` non rappresentano una finestra persistente | 1.000 confronti casuali, zeri, vuoto e budget negativo superati | Sliding window riconosciuta ma non implementata | 16/30 min |
| 4 | Output corretti, scala non rispettata | O(qm) nel caso peggiore, O(m) spazio | Chiara gestione delle operazioni; `distinct` ricalcola tutto | 1.000 sequenze casuali, transizioni a zero e non mutazione superati | Frequency map riconosciuta; stato aggregato non mantenuto | 17/30 min |

## Cosa e' andato bene

- Tutti i test visibili sono stati eseguiti e superati.
- L'esercizio 1 corregge esattamente l'errore della settimana precedente:
  `is True` esclude `1`, stringhe e altri valori truthy.
- L'esercizio 2 e' corretto, lineare e gestisce il tie-breaking senza perdere
  l'ordine di prima apparizione. Il dizionario `support` e' una scelta adatta.
- Gli esercizi 3 e 4 sono funzionalmente corretti: non sono emersi errori in
  1.000 confronti casuali per funzione.
- Nessuna submission modifica gli input.
- L'ordine scelto ha protetto prima tre esercizi per cui era disponibile una
  strategia, lasciando per ultimo quello dichiarato piu' incerto.

## Primo problema importante

Nell'esercizio 3 il pattern e' stato nominato correttamente nelle note, ma il
codice riparte da ogni indice `i`, azzera `j`, ricostruisce `tot_budget` e
risomma il segmento. La finestra non sopravvive da un'iterazione esterna alla
successiva: e' ancora enumerazione esaustiva di tutti gli inizi, quindi O(n^2).

Il benchmark mostra la crescita quadratica: con soli zeri e budget zero,
2.000 elementi richiedono circa 0,15 s, 4.000 circa 0,61 s e 8.000 circa
2,50 s. Il limite di 200.000 elementi non e' raggiungibile.

## Domanda o hint minimo

Se mantieni una variabile `current_sum`, che cosa devi sottrarre quando la
somma supera il budget affinche' `left` possa avanzare senza ricominciare da
zero?

## Secondo problema: query `distinct`

Nell'esercizio 4 ogni query `distinct` visita tutte le chiavi del registro. Se
ci sono molti modelli e molte query, il costo e' O(qm). Nel benchmark con lo
stesso numero di modelli distinti e query `distinct`, 2.000 elementi richiedono
circa 0,19 s, 4.000 circa 0,77 s e 8.000 circa 3,16 s.

Ogni operazione modifica il conteggio di un solo modello. Il numero di modelli
attivi cambia soltanto nelle transizioni `0 -> 1` e `1 -> 0`; puo' quindi
essere mantenuto incrementalmente invece di essere ricalcolato.

## Test aggiuntivi di review

- Esercizio 1: valori `True`, `False`, `None`, `1`, stringhe e liste, servizio
  vuoto e non mutazione; tutti superati.
- Esercizio 2: parita' tra errori, ordine di prima apparizione, valori zero,
  campi mancanti, stringhe vuote e non mutazione; tutti superati.
- Esercizio 3: casi limite e 1.000 confronti casuali con un oracolo esaustivo;
  output tutti corretti. Il benchmark evidenzia O(n^2).
- Esercizio 4: transizioni a zero, registrazioni successive e 1.000 sequenze
  casuali confrontate con un oracolo; output tutti corretti. Il benchmark
  evidenzia O(qm) nel caso peggiore.

## Dati di processo

Sono presenti ordine, motivazione, rischio percepito, pattern e tempi. E'
documentato il blocco dell'esercizio 2, ma mancano le decisioni prese e il
debrief finale. I tempi restano autodichiarati.

## Regola pratica da salvare

Riconoscere il nome del pattern non basta: lo stato deve sopravvivere tra le
iterazioni. Se una query chiede ripetutamente un aggregato e ogni update tocca
un solo elemento, aggiornare l'aggregato soltanto quando quell'elemento
attraversa una soglia rilevante.

## Decisione sui pattern

Nessun nuovo pattern e' masterizzato. Predicati esatti passano da errore
rilevato a consolidamento iniziale. Sliding window resta da sbloccare: e' stata
riconosciuta in due formulazioni, ma non ancora implementata autonomamente con
stato persistente e complessita' O(n).

## XP

- +25 XP: esercizio 1 facile, corretto entro il timebox.
- Esercizio 2 corretto ma oltre il timebox: nessun XP di completamento.
- Esercizi 3 e 4 non conformi ai vincoli di scala: nessun XP.
- Totale Week 002: +25 XP.

## Priorita' per Week 003

- Riproporre sliding window con somma corrente su una formulazione diversa.
- Allenare una query online in cui l'aggregato cambia soltanto su transizioni
  di stato.
- Conservare un esercizio di aggregazione, ma richiedere una struttura di
  output piu' complessa senza ripetere il dominant error.
- Completare decisioni e debrief nelle note.

## Dispensa progressiva

La Week 002 richiede un capitolo aggiuntivo: gli esercizi 3 e 4 sono corretti
sugli output ma non conformi alla scala. Il capitolo conserva le submission e
formalizza due invarianti incrementali: somma della finestra e numero di
frequenze strettamente positive.
