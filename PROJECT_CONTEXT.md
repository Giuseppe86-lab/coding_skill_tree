# Project Context

Questo file conserva il contesto iniziale del percorso, cosi' Codex e Giuseppe
possono continuare il lavoro senza dipendere dalla memoria di una chat.

## Obiettivo annuale

Diventare forte e sicuro nei coding assessment entro Agosto 2027, con un
livello competitivo per ruoli AI Engineering, Data Engineering, Consulting,
Big Tech, Quant e technology-oriented.

Il percorso dura circa un anno e deve produrre:

- competenza tecnica reale;
- velocita' sotto pressione;
- capacita' di riconoscere pattern;
- portfolio pubblico ordinato;
- storico di errori, review e miglioramenti.

## Livello iniziale

- Python: buono, ma da rendere piu' rapido in contesti assessment.
- Problem solving: in crescita, con margine forte su pattern recognition.
- Data manipulation: punto forte.
- Algoritmi: area da costruire con progressione guidata.
- Strutture dati: basi presenti, da consolidare su problemi misti.
- Speed: discreta, ma da allenare con timebox e simulazioni.

## Punti forti iniziali

- Lookup.
- Dizionari.
- Set.
- Data manipulation.
- Parsing.
- Ragionamento strutturato.
- Capacita' di riflettere sugli errori dopo la soluzione.

## Debolezze iniziali

- Pattern recognition non ancora automatica.
- String manipulation da rendere piu' naturale.
- Tendenza a pensare troppo in modo matematico anche quando una conversione a
  stringa sarebbe piu' semplice.
- Rischio di investire troppo tempo su un problema bloccato.
- Poca pratica su sliding window, two pointers, binary search, grafi e dynamic
  programming.

## Errori emersi dal test CodeSignal iniziale

- Troppo tempo investito su un singolo esercizio.
- Tendenza a cercare una soluzione matematica quando il problema poteva essere
  trattato come manipolazione di stringhe.
- Mancato uso immediato di `str(number)` nei problemi sulle cifre.
- Necessita' di riconoscere piu' velocemente situazioni da lookup quando ci
  sono due liste, tabelle o collezioni collegate.
- Bisogno di distinguere meglio tra controllo di presenza (`key in dict`) e
  recupero di valore (`dict.get(key)`).

## Pattern gia' acquisiti

- Hash map.
- Lookup.
- Join logico tra collezioni.
- Frequency count.
- Long-to-wide.
- Uso di set per membership.
- Parsing semplice.

## Pattern prioritari da allenare

- String manipulation.
- Sliding window.
- Two pointers.
- Binary search.
- Regex.
- Heap.
- BFS e DFS.
- Dynamic programming.

## Strategia di timeboxing

Durante gli esercizi:

- leggere prima tutto il testo;
- identificare input, output, vincoli ed edge case;
- provare a nominare il pattern prima di scrivere codice;
- stabilire un timebox;
- se si resta bloccati, segnare il blocco e passare oltre;
- tornare sul problema solo dopo aver protetto i punti piu' facili.

Timebox consigliato:

- esercizio facile: 10-15 minuti;
- esercizio medio: 20-30 minuti;
- esercizio difficile: 35-45 minuti;
- boss fight mensile: tempo totale fisso, senza pause lunghe su un singolo
  problema.

## Regole operative personali

- Se il problema riguarda cifre, provare subito `str(number)`.
- Se ci sono due collezioni collegate, costruire un lookup.
- Se si devono contare elementi, pensare a frequency map.
- Se serve controllare esistenza in un dizionario, usare `key in dict`.
- Scrivere prima una soluzione semplice e corretta.
- Testare almeno caso base, caso vuoto e caso limite.
- Aggiornare `LESSONS_LEARNED.md` dopo ogni errore utile.

## Come Codex deve usare questo file

Codex deve leggere questo file prima di:

- creare nuove quest settimanali;
- recensire soluzioni;
- proporre boss fight;
- aggiornare XP o skill tree;
- scegliere quali pattern allenare.

Questo file descrive il punto di partenza. Se il livello cambia, va aggiornato
senza cancellare lo storico utile presente negli altri file.
