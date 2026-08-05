# Week 001 — Review

Stato: completata e recensita il 2026-08-04.

## Risultato complessivo

- Esercizi completati: 4/4
- Esercizi corretti rispetto a specifica e vincoli: 3/4
- Esercizi parzialmente corretti: 1/4
- Tempo totale dichiarato: 37 minuti su 85
- XP ottenuti: +90
- Pattern allenati: string manipulation, aggregazione, frequency map,
sliding window
- Pattern consolidati: nessuna nuova mastery; hash map e frequency count sono
stati confermati come punti forti

## Valutazione


| Esercizio | Correttezza                                          | Complessita'                       | Leggibilita'                                                 | Edge case                                      | Pattern recognition                         | Timebox   |
| --------- | ---------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------ | ---------------------------------------------- | ------------------------------------------- | --------- |
| 1         | Corretta                                             | O(cifre totali) tempo, O(d) spazio | Chiara; conversione ripetuta migliorabile                    | Visibili e aggiuntivi superati                 | `str(n)` riconosciuto subito                | 14/15 min |
| 2         | Corretta per il contratto booleano dell'input        | O(n) tempo, O(k) spazio            | Buona; la copia del record non serve                         | Campi mancanti, `None`, `False` e zero gestiti | Aggregazione con lookup riconosciuta        | 13/20 min |
| 3         | Corretta                                             | O(n+m) tempo, O(u) spazio          | Chiara; `.get()` e' ridondante dopo il controllo di presenza | Molteplicita', negativi e liste vuote gestiti  | Frequency map riconosciuta                  | 5/20 min  |
| 4         | Output corretti, ma non rispetta il vincolo di scala | O(n^2) tempo, O(1) spazio          | Comprensibile; `input` oscura il built-in                    | Bordi e duplicati corretti; scala non gestita  | Sliding window nominata ma non implementata | 5/30 min  |




## Cosa e' andato bene

- Tutti i test visibili sono stati eseguiti e superati.
- L'esercizio 1 mostra che la regola `str(number)` e' stata applicata in
autonomia entro il timebox.
- L'esercizio 2 aggrega correttamente run, token ed esiti senza modificare gli
input. Il controllo di truthiness e' valido per il contratto booleano
previsto dall'esercizio.
- L'esercizio 3 e' la soluzione piu' forte della settimana: corretta,
lineare, compatta e capace di contare correttamente le molteplicita'.
- Nessuna funzione modifica gli input.
- Tutti e quattro gli esercizi sono stati completati entro il tempo previsto.



## Primo problema importante

L'esercizio 4 scorre l'intera lista per ogni possibile inizio della finestra.
La correttezza sugli esempi non basta: con 200.000 timestamp il numero di
confronti cresce quadraticamente. Un controllo locale con 5.000 timestamp ha
gia' richiesto circa 0,58 secondi, pur rappresentando soltanto il 2,5% della
dimensione massima.

## Domanda o hint minimo

Quando l'inizio della finestra avanza, quali informazioni della finestra
precedente puoi conservare, invece di ricontrollare tutti i timestamp da capo?

## Edge case e test aggiuntivi

- Gli esercizi 1, 2 e 3 superano i test aggiuntivi compatibili con il contratto
degli input.
- Nell'esercizio 4 un test di scala rende visibile il costo quadratico.
- I test aggiuntivi sono responsabilita' di Codex durante la review; non viene
richiesta la creazione di test personali.



## Regola pratica da salvare

I test visibili verificano alcuni output, non il rispetto dei vincoli. Prima di
chiudere un esercizio, confrontare la complessita' della soluzione con la
dimensione massima dell'input.

## Decisione sui pattern

Nessun nuovo pattern viene considerato masterizzato. String manipulation e'
stata applicata correttamente una volta nel progetto. Sliding window resta da
sbloccare: l'idea e' stata riconosciuta, ma la soluzione non riusa lo stato
della finestra.

## Priorita' per Week 002

- Riproporre sliding window con uno scenario diverso e richiedere una
soluzione lineare.
- Continuare a far preparare a Codex edge case e test di performance durante
la review.
- Continuare con un esercizio breve su frequency map, aumentando gradualmente
la complessita' invece di ripetere il conteggio di coppie identico.

## Dispensa progressiva

La sliding window dell'esercizio 4 inaugura il primo capitolo della dispensa
LaTeX. Il capitolo documenta perche' la scansione annidata, pur producendo gli
output attesi, non e' conforme al vincolo di scala e introduce l'invariante
della finestra mobile a due indici.

Sorgente: `dispensa/chapters/week_001.tex`.
