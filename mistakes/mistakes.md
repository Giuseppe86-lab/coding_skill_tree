2026-08

❌ Pensato troppo in termini matematici.

✓ Se il problema riguarda le cifre,
provare subito str(number).

❌ Investito troppo tempo
sullo stesso esercizio.

✓ Quando vedo due tabelle
pensare subito a un lookup.

✓ Usare "key in dict"
invece di get() per controllare
l'esistenza della chiave.

❌ Considerato il passaggio dei test
visibili sufficiente anche con O(n^2).

✓ Confrontare sempre la complessita'
con il vincolo massimo dell'input.

❌ Usata la truthiness quando la specifica
richiedeva esattamente `success is True`.

✓ Tradurre letteralmente i predicati e non
assumere tipi non dichiarati dal contratto.

❌ Riconosciuta la sliding window, ma
reinizializzato lo stato per ogni inizio.

✓ `right` aggiunge, `left` rimuove: somma
e finestra devono persistere tra iterazioni.

❌ Ricalcolato `distinct` scorrendo tutto
il registro a ogni query.

✓ Aggiornare l'aggregato solo nelle
transizioni di stato `0 -> 1` e `1 -> 0`.

❌ Deduplicato con membership su una lista
crescente, ottenendo tempo quadratico.

✓ Lista per l'ordine, set per verificare
in tempo medio costante gli elementi visti.

❌ Aggiornato un aggregato a ogni operazione
oltre la soglia, anche senza cambio di stato.

✓ Confrontare stato prima e dopo: modificare
l'aggregato solo se la soglia viene attraversata.
