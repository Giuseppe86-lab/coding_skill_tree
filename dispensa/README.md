# Dispensa progressiva di algoritmi

Questa directory contiene i sorgenti LaTeX del manuale offline costruito a
partire dalle review settimanali.

## Struttura

- `main.tex`: preambolo, stile tipografico e ordine dei capitoli;
- `chapters/week_XXX.tex`: contenuto tecnico emerso nella settimana;
- `../output/pdf/dispensa_algoritmi.pdf`: PDF cumulativo generato.

Un capitolo viene aggiunto soltanto dopo la review della relativa quest, per
non anticipare soluzioni o suggerimenti.

## Compilazione

Dalla radice del repository:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -jobname=dispensa_algoritmi -outdir=output/pdf dispensa/main.tex
```

Per rimuovere i soli file ausiliari conservando il PDF:

```bash
latexmk -c -jobname=dispensa_algoritmi -outdir=output/pdf dispensa/main.tex
```

Ogni nuova versione deve essere renderizzata in immagini e controllata
visivamente prima di essere considerata definitiva.
