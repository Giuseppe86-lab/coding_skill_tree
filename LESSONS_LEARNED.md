# Lessons Learned

Questo file raccoglie gli apprendimenti cumulativi del percorso. Va aggiornato
dopo ogni settimana, review importante o boss fight.

L'obiettivo non e' accumulare appunti, ma trasformare gli errori in regole
pratiche riutilizzabili nei coding assessment.

## Regole gia' emerse

### Time management

- Non investire troppo tempo su un esercizio solo perche' sembra "quasi
  finito".
- Se dopo alcuni minuti non emerge una strategia chiara, fermarsi e
  riclassificare il problema.
- In assessment, conviene assicurare prima i punti facili e poi tornare sui
  problemi piu' lunghi.

### Numeri e cifre

- Se un problema riguarda cifre, posizioni, inversioni o manipolazioni di
  numeri, provare subito a convertire con `str(number)`.
- Non forzare una soluzione matematica quando una soluzione su stringa e'
  piu' leggibile e veloce.

### Tabelle, liste collegate e lookup

- Quando compaiono due tabelle, due liste o due insiemi di oggetti collegati
  da una chiave, pensare subito a un dizionario di lookup.
- Costruire prima la struttura di supporto, poi risolvere la richiesta.
- Per controllare se una chiave esiste in un dizionario, preferire
  `key in dict` quando serve distinguere presenza e valore.

### Pattern recognition

- Prima di scrivere codice, chiedersi: "Che pattern e'?"
- Se ci sono conteggi, frequenze o duplicati, considerare una hash map.
- Se bisogna passare da righe lunghe a colonne o aggregazioni, pensare al
  pattern long-to-wide.
- Se si cercano elementi gia' visti, usare set o dizionari.

### Soluzione semplice prima dell'ottimizzazione

- In assessment, una soluzione chiara e corretta vale piu' di una soluzione
  elegante ma incompleta.
- Ottimizzare solo dopo avere una versione funzionante e testata.
- Scrivere piccoli test manuali prima di dichiarare chiuso un esercizio.

### Semantica esatta dei predicati

- Tradurre letteralmente i requisiti: `value is True` e un controllo di
  truthiness non sono equivalenti.
- Un valore come `1` o una stringa non vuota e' truthy, ma non e' l'oggetto
  booleano `True`.
- Non aggiungere al contratto ipotesi sui tipi che il testo non dichiara.

## Pattern acquisiti o in consolidamento

### Acquisiti

- Lookup con dizionario.
- Hash map.
- Set per appartenenza.
- Frequency count.
- Parsing semplice.
- Trasformazioni long-to-wide.

### In consolidamento

- String manipulation.
- Pattern recognition rapido.
- Gestione del timebox.

### Da sbloccare

- Sliding window.
- Two pointers.
- Binary search.
- Regex.
- Heap.
- BFS.
- DFS.
- Dynamic programming.

## Template per nuovi apprendimenti

Usare questo formato dopo una review:

```markdown
## YYYY-MM-DD - Titolo breve

### Situazione

Descrizione sintetica dell'esercizio o dell'errore.

### Errore o blocco

Cosa non ha funzionato.

### Regola imparata

La regola pratica da riusare.

### Pattern collegato

Pattern allenato o scoperto.

### Prossima azione

Come consolidare l'apprendimento.
```

## Log

### 2026-08-02 - Contesto iniziale

Il percorso parte con buone basi in Python, lookup, dizionari, set, data
manipulation e parsing. Le aree critiche iniziali sono pattern recognition,
string manipulation, sliding window, binary search, grafi e gestione del tempo.

La prima strategia e': leggere bene il problema, riconoscere il pattern,
usare timebox rigidi e salvare ogni errore come regola pratica.

### 2026-08-07 - Week 001: predicati esatti e vincoli di scala

#### Situazione

Quattro esercizi completati entro il timebox. String manipulation e frequency
map sono state applicate correttamente; la prima sliding window ha prodotto gli
output attesi con una scansione completa per ogni timestamp. La verifica
aggiuntiva dell'aggregazione ha inoltre distinto `success is True` dalla
truthiness generica.

#### Errore o blocco

I test visibili dell'esercizio sulla finestra passavano, ma la submission era
O(n^2) con un vincolo di 200.000 elementi. Nell'aggregazione,
`1 if record.get("success") else 0` contava anche valori truthy non booleani,
in contrasto con la specifica.

#### Regola imparata

- Il passaggio dei test visibili non dimostra il rispetto dei vincoli.
- Prima di chiudere, stimare la complessita' usando la dimensione massima.
- Se il requisito dice `is True`, usare un predicato altrettanto esatto.

#### Pattern collegato

Sliding window, aggregazione con dizionario, validazione degli input e
semantica dei predicati.

#### Prossima azione

Allenare una sliding window lineare su un problema diverso e un esercizio con
valori truthy eterogenei. Codex preparera' edge case e test di performance
aggiuntivi durante le review.

### 2026-08-11 - Week 002: lo stato deve sopravvivere

#### Situazione

Quattro esercizi completati. Predicati esatti e aggregazione sono corretti;
sliding window e registro dinamico producono gli output attesi ma ripetono
lavoro gia' svolto.

#### Errore o blocco

Nella finestra sul budget, somma e indici vengono reinizializzati per ogni
possibile inizio, mantenendo il costo O(n^2). Nel registro, ogni query
`distinct` riconta tutte le chiavi e produce O(qm) nel caso peggiore.

#### Regola imparata

- Riconoscere un pattern significa anche conservarne lo stato tra iterazioni.
- In una sliding window con valori non negativi, aggiornare la somma quando
  `right` entra e sottrarre `costs[left]` quando `left` esce.
- Per un conteggio di categorie attive, aggiornare il totale soltanto nelle
  transizioni di frequenza `0 -> 1` e `1 -> 0`.

#### Pattern collegato

Sliding window con somma corrente, frequency map, query online e invarianti
incrementali.

#### Prossima azione

Risolvere autonomamente problemi diversi che richiedano gli stessi invarianti,
senza ripetere la formulazione della Week 002.

### 2026-08-19 - Week 003: la soglia si attraversa, non si riconta

#### Situazione

La sliding window e' stata implementata autonomamente in O(n), correttamente e
entro il timebox. Anche l'aggregazione annidata e' corretta e lineare, ma ha
richiesto 45 minuti su 25. La normalizzazione delle stringhe produce gli output
attesi ma deduplica tramite una lista; il monitor online mantiene un contatore
aggregato con transizioni non esatte.

#### Errore o blocco

- Il controllo di appartenenza su una lista crescente rende quadratica la
  deduplicazione di molti nomi distinti.
- Il numero di worker sovraccarichi viene aggiornato a ogni operazione sopra o
  sotto soglia, invece che soltanto quando il worker cambia stato.

#### Regola imparata

- Per deduplicare preservando l'ordine, usare una lista per l'output e un set
  per la membership.
- Per un aggregato basato su soglia, confrontare lo stato precedente con lo
  stato successivo e aggiornarlo soltanto quando i due differiscono.

#### Pattern collegato

Sliding window con conteggio, deduplicazione stabile, aggregazione annidata e
query online con transizioni di soglia.

#### Prossima azione

Ripetere una sliding window su una nuova formulazione e allenare transizioni
che restano per piu' operazioni consecutive dallo stesso lato della soglia.
