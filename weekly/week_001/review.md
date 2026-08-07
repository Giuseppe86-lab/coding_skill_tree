# Week 001 — Review

Stato: completata il 2026-08-04 e verificata integralmente il 2026-08-07.

## Risultato complessivo

- Esercizi completati: 4/4
- Esercizi corretti rispetto a specifica e vincoli: 2/4
- Esercizi parzialmente corretti: 2/4
- Tempo totale dichiarato: 37 minuti su 85
- XP ottenuti: +65
- Pattern allenati: string manipulation, aggregazione con dizionario,
  frequency map, sliding window
- Pattern consolidati: nessuna nuova mastery; hash map e frequency count sono
  confermati come punti forti

## Valutazione

| Esercizio | Correttezza | Complessita' | Leggibilita' | Edge case | Pattern recognition | Timebox |
|---|---|---|---|---|---|---|
| 1 | Corretta | O(cifre totali) tempo, O(d) spazio | Chiara; evita la doppia conversione di ogni cifra | Zero, ripetizioni, lista e selezione vuote superati | `str(n)` riconosciuto subito | 14/15 min |
| 2 | Parziale: usa la truthiness invece di `success is True` | O(n) tempo, O(k) spazio | Struttura chiara; la copia del record e' superflua | Campi mancanti, `None`, `False` e zero superati; valori truthy non booleani falliscono | Aggregazione con lookup riconosciuta | 13/20 min |
| 3 | Corretta | O(n+m) tempo, O(u) spazio | Chiara; `.get()` e' ridondante dopo il controllo di presenza | Molteplicita', negativi, liste vuote e conteggio oltre 32 bit superati | Frequency map riconosciuta | 5/20 min |
| 4 | Corretta sugli output, non conforme al vincolo di scala | O(n^2) tempo, O(1) spazio | Comprensibile; `input` oscura il built-in | Bordi, duplicati, vuoto e durata non positiva superati; scala fallita | Sliding window nominata ma non implementata autonomamente | 5/30 min |

## Cosa e' andato bene

- Tutti e quattro gli esercizi sono stati affrontati e i tempi sono stati
  registrati entro i rispettivi timebox.
- L'esercizio 1 applica autonomamente la regola `str(number)` e non modifica
  gli input.
- L'esercizio 3 e' la soluzione piu' forte della settimana: corretta,
  lineare, compatta e capace di preservare le molteplicita'.
- La submission originale dell'esercizio 4 gestisce correttamente la semantica
  dell'intervallo semiaperto; il difetto e' di scala, non di output.
- Nessuna delle quattro submission modifica gli input.

## Primo problema importante

Nell'esercizio 2 la specifica richiede di incrementare `successful_runs`
soltanto quando `success is True`. L'espressione
`1 if record.get("success") else 0` applica invece la truthiness: un valore
come `1` o `"yes"` viene contato come successo pur non essendo l'oggetto
booleano `True`. Il testo non restringe il campo ai soli booleani, quindi
questa e' una differenza di correttezza entro il contratto, non un caso fuori
specifica.

## Domanda o hint minimo

Quale confronto Python traduce letteralmente la condizione "soltanto quando
il valore e' `True`" senza accettare altri valori truthy?

## Secondo problema: vincolo di scala

La submission originale dell'esercizio 4 scorre l'intera lista per ogni
possibile inizio della finestra. Con 10.000 timestamp ha richiesto circa 2,29
secondi; con il limite di 200.000 elementi il costo quadratico non e'
ammissibile. La soluzione lineare di riferimento ha elaborato 200.000
timestamp in circa 0,03 secondi nello stesso ambiente.

La cella successiva alla submission e' esplicitamente marcata `#AI soluzione`.
I test visibili del notebook sono eseguiti dopo questa ridefinizione e quindi
validano la versione AI, non la submission originale. In review le due
versioni sono state caricate e testate separatamente.

## Test aggiuntivi eseguiti

- Esercizio 1: ticket ripetuti, zero, cifre assenti, selezione vuota e
  verifica di non mutazione; tutti superati.
- Esercizio 2: modello stringa vuota, campi mancanti, `None`, `False`, zero e
  non mutazione superati; fallito il test con `success` uguale a `1` e
  `"yes"`, che devono restare esclusi.
- Esercizio 3: molteplicita', negativi, liste vuote, non mutazione e
  10.000.000.000 coppie valide; tutti superati.
- Esercizio 4: vuoto, duplicati, timestamp negativi, bordo destro esclusivo,
  durata non positiva e 1.000 confronti casuali con un oracolo esaustivo;
  output corretti per entrambe le versioni. Il benchmark separato conferma il
  divario tra O(n^2) e O(n).

I test aggiuntivi sono responsabilita' di Codex durante la review; l'assenza
di test personali non e' stata penalizzata.

## Dati mancanti

Non mancano esercizi ne' tempi. In `notes.md` non sono pero' compilati le
previsioni manuali, gli edge case considerati, le decisioni allo scadere del
timebox e il debrief personale. Queste informazioni qualitative non vengono
ricostruite a posteriori e non sono usate per assegnare mastery o XP. I tempi
sono valutati come tempi dichiarati, non come misurazioni indipendenti.

## Regole pratiche da salvare

- Se la specifica richiede `is True`, non sostituire il requisito con un
  controllo generico di truthiness.
- I test visibili verificano alcuni output, non il rispetto dei vincoli:
  confrontare sempre la complessita' con la dimensione massima dell'input.
- Verificare quale definizione di una funzione e' attiva quando il notebook
  contiene piu' celle che la ridefiniscono.

## Decisione sui pattern

Nessun nuovo pattern viene considerato masterizzato. String manipulation e'
stata applicata correttamente una volta nel progetto. Sliding window resta da
sbloccare: l'idea e' stata nominata, ma l'implementazione lineare presente nel
notebook e' dichiarata come soluzione AI e non costituisce evidenza di
esecuzione autonoma.

## XP

- +25 XP: esercizio 1 facile, corretto entro il timebox.
- +40 XP: esercizio 3 medio, corretto entro il timebox.
- Nessun XP per gli esercizi 2 e 4, perche' non soddisfano integralmente la
  specifica o i vincoli.
- Totale Week 001: +65 XP. Il precedente totale provvisorio di +90 e' stato
  corretto sulla base dei test aggiuntivi.

## Priorita' per Week 002

- Implementare autonomamente una sliding window O(n) su uno scenario diverso.
- Allenare la traduzione letterale dei predicati di specifica, distinguendo
  identita', uguaglianza e truthiness.
- Mantenere un esercizio di frequency map con complessita' leggermente
  maggiore, senza ripetere lo stesso conteggio di coppie.
- Compilare durante la quest almeno blocchi, decisioni al timebox e debrief,
  cosi' da rendere valutabile anche il processo.

## Dispensa progressiva

L'aggiornamento e' necessario per due criteri di `AGENTS.md`: la settimana ha
introdotto la sliding window e la submission dell'esercizio 4 e'
funzionalmente corretta ma non conforme alla scala; inoltre l'esercizio 2
espone un errore riutilizzabile sulla semantica dei predicati. Il capitolo
`dispensa/chapters/week_001.tex` conserva le submission nei riquadri rossi,
distingue errore logico e inefficienza, e presenta soltanto implementazioni di
riferimento validate dai test della review.
