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
