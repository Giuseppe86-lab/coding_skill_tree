# Coding Skill Tree

Questo repository traccia il percorso di Giuseppe Sinatra per diventare
molto forte nei coding assessment entro Agosto 2027, con focus su Python,
problem solving, strutture dati, pattern ricorrenti e gestione del tempo.

Il progetto e' pensato come:

- sistema di allenamento settimanale;
- diario tecnico del percorso;
- tracker misurabile di progressi, XP e pattern acquisiti;
- portfolio pubblico di crescita tecnica.

## Obiettivo

Allenarsi per arrivare a un livello competitivo nei coding assessment per
ruoli AI Engineering, Data Engineering, Tech, Consulting, Big Tech e Quant.

Il target non e' solo risolvere esercizi, ma imparare a:

- riconoscere velocemente il pattern giusto;
- scegliere una soluzione semplice e corretta prima di ottimizzare;
- gestire il tempo sotto pressione;
- scrivere codice Python leggibile;
- testare edge case in modo sistematico;
- trasformare ogni errore in una regola riutilizzabile.

## File principali

- `README.md`: mappa pubblica del progetto e regole generali del percorso.
- `PROJECT_CONTEXT.md`: contesto iniziale del percorso, livello attuale,
  punti forti, debolezze e strategia.
- `AGENTS.md`: istruzioni operative per Codex. Codex deve leggerlo prima di
  creare esercizi, review o aggiornamenti.
- `PLAYER.md`: scheda giocatore con livello attuale, obiettivi e target.
- `SKILL_TREE.md`: albero dei pattern e delle skill sbloccate o da sbloccare.
- `LESSONS_LEARNED.md`: diario cumulativo degli apprendimenti.
- `xp.md`: livello, XP, streak, pattern sbloccati e boss fight vinte.
- `mistakes/mistakes.md`: errori ricorrenti e contromisure.
- `weekly/`: cartelle settimanali con esercizi, soluzioni, note e review.
- `dispensa/`: sorgenti della dispensa LaTeX progressiva sugli algoritmi
  affrontati e sulle ottimizzazioni emerse in review.
- `output/pdf/dispensa_algoritmi.pdf`: versione offline aggiornata della
  dispensa.
- `monthly/`: report mensili e boss fight.

## Struttura consigliata

```text
coding_skill_tree/
+-- README.md
+-- AGENTS.md
+-- PROJECT_CONTEXT.md
+-- PLAYER.md
+-- SKILL_TREE.md
+-- LESSONS_LEARNED.md
+-- xp.md
+-- mistakes/
|   +-- mistakes.md
+-- dispensa/
|   +-- main.tex
|   +-- chapters/
|       +-- week_001.tex
+-- weekly/
|   +-- week_001/
|   |   +-- README.md
|   |   +-- quest.ipynb
|   |   +-- notes.md
|   |   +-- review.md
|   +-- week_002/
+-- monthly/
    +-- 2026-08/
    |   +-- boss_fight.md
    |   +-- report.md
    +-- 2026-09/
```

Le cartelle possono essere create progressivamente: non serve anticipare
tutto, ma ogni settimana deve lasciare una traccia ordinata.

## Flusso settimanale

Ogni settimana e' una quest.

Una settimana standard contiene:

- un singolo notebook con 4 esercizi Python progressivi;
- almeno 1 pattern nuovo o appena imparato;
- almeno 1 esercizio di consolidamento su pattern gia' visti;
- timebox consigliato per ogni esercizio;
- note sugli errori;
- review finale;
- aggiornamento della dispensa LaTeX quando emergono nuovi algoritmi o
  implementazioni non conformi ai vincoli;
- aggiornamento di XP, skill tree e lessons learned.

### Sequenza

1. Leggere il contesto: `PROJECT_CONTEXT.md`, `PLAYER.md`,
   `SKILL_TREE.md`, `LESSONS_LEARNED.md`, `mistakes/mistakes.md`.
2. Creare o aprire la cartella della settimana in `weekly/week_XXX/`.
3. Risolvere gli esercizi uno alla volta, rispettando il timebox.
4. Scrivere note brevi su ragionamento, blocchi e intuizioni.
5. Fare review delle soluzioni.
6. Dopo la review, aggiungere alla dispensa gli algoritmi nuovi e i confronti
   tra implementazioni inefficienti e corrette.
7. Compilare e verificare visivamente il PDF offline.
8. Aggiornare i file di progresso.

## Dispensa progressiva

La dispensa e' un unico manuale cumulativo, costruito settimana dopo settimana
in `dispensa/`. Non sostituisce la review: trasforma gli errori piu' istruttivi
in materiale di ripasso durevole.

Ogni capitolo viene scritto soltanto dopo il completamento della quest e puo'
contenere:

- formulazione del problema e ipotesi;
- approccio iniziale e diagnosi tecnica dell'inefficienza;
- algoritmo efficiente, invariante e correttezza;
- analisi di complessita' temporale e spaziale;
- edge case e segnali utili per riconoscere il pattern;
- riquadri cromatici distinti per implementazione non conforme e
  implementazione corretta.

Il registro deve essere professionale, rigoroso e vicino a quello di una
dispensa universitaria, mantenendo pero' l'orientamento pratico ai coding
assessment.

## Review

La review deve valutare:

- correttezza;
- complessita' temporale e spaziale;
- chiarezza del codice;
- edge case;
- pattern riconosciuto;
- gestione del tempo.

La review non deve limitarsi a dire se una soluzione funziona. Deve spiegare:

- cosa e' andato bene;
- qual e' stato il primo errore importante;
- quale regola pratica va salvata;
- se il pattern puo' essere considerato acquisito o solo allenato.

## XP

Gli XP servono a rendere visibile il progresso. Non sono un voto assoluto:
sono un sistema di feedback.

Regole consigliate:

- +25 XP per esercizio facile risolto correttamente entro il timebox;
- +40 XP per esercizio medio risolto correttamente entro il timebox;
- +60 XP per esercizio difficile risolto correttamente entro il timebox;
- +15 XP per una buona analisi di edge case;
- +20 XP per una review scritta bene;
- +30 XP quando un errore ricorrente viene trasformato in una regola;
- +50 XP quando un pattern viene risolto in autonomia piu' volte.

Un pattern non si considera masterizzato dopo un solo esercizio. Serve
risolverlo piu' volte, in autonomia, con tempi accettabili e pochi errori.

## Boss Fight Mensili

Ogni mese termina con una boss fight: una mini-simulazione di coding
assessment.

La boss fight contiene:

- 3 o 4 esercizi;
- difficolta' mista;
- tempo totale limitato;
- almeno un problema che combina piu' pattern;
- review finale con punteggio, XP e piano per il mese successivo.

La boss fight serve a misurare:

- velocita';
- lucidita' sotto pressione;
- scelta dell'ordine degli esercizi;
- capacita' di lasciare un problema bloccato;
- qualita' delle soluzioni semplici.

## Strategia durante gli assessment

Regole operative:

- leggere tutti gli esercizi prima di iniziare;
- partire dai punti facili;
- non restare bloccato troppo a lungo su un singolo problema;
- se un problema riguarda cifre, provare subito `str(number)`;
- se compaiono due tabelle o due liste collegate, pensare subito a un lookup;
- se serve controllare esistenza in un dizionario, usare `key in dict`;
- prima scrivere una soluzione corretta, poi ottimizzare;
- eseguire i test visibili; Codex prepara edge case e test di performance
  aggiuntivi durante la review.

## Regole di aggiornamento

Dopo ogni settimana aggiornare:

- `weekly/week_XXX/review.md`;
- `LESSONS_LEARNED.md`;
- `SKILL_TREE.md`;
- `mistakes/mistakes.md`;
- `xp.md`.

Dopo ogni mese aggiornare:

- `monthly/YYYY-MM/report.md`;
- `monthly/YYYY-MM/boss_fight.md`;
- `PLAYER.md`, se il livello percepito cambia;
- `PROJECT_CONTEXT.md`, se cambia la strategia generale.

## Regola piu' importante

Il repository deve contenere il contesto durevole del percorso.

Le chat possono aiutare, ma non devono essere l'unica memoria del progetto.
Ogni decisione importante, errore ricorrente, pattern acquisito e review utile
deve finire in un file Markdown del repository.
