# Laboratorio 1 - Minimum Spanning Tree

## Descrizione dell'esercitazione
In questo laboratorio confronteremo tra loro gli algoritmi per il problema del Minimum Spanning Tree visti a lezione.
Algoritmi

Gli algoritmi da implementare sono tre:
- **Algoritmo di Prim** implementato con Heap
- **Algoritmo di Kruskal** nella sua implementazione "naive" di complessità O(mn)
- **Algoritmo di Kruskal** implementato con Union-Find

## Dataset
Il dataset contiene 68 grafi di esempio, di dimensione compresa tra 10 e 100000 vertici, generati in modo randomico con il TestCaseGenerator di stanford-algs. Ogni file descrive un grafo non orientato con pesi interi usando il seguente formato:
```
[numero_di_vertici] [numero_di_archi] 
[un_vertice_arco_1] [altro_vertice_arco_1] [peso_arco_1] 
[un_vertice_arco_2] [altro_vertice_arco_2] [peso_arco_2] 
[un_vertice_arco_3] [altro_vertice_arco_3] [peso_arco_3] 
...
```
Ad esempio, una riga "2 3 -8874" indica che esiste un arco che collega il vertice 2 al vertice 3 con peso -8874. NON si deve presumere che i pesi siano positivi, né che siano distinti.

## Domanda 1
Eseguite i tre algoritmi che avete implementato (Prim, Kruskal naive e Kruskal efficiente) sui grafi del dataset. Misurate i tempi di calcolo dei tre algoritmi e create un grafico che mostri la variazione dei tempi di calcolo al variare del numero di vertici nel grafo. Per ognuna delle istanze del problema, riportate il peso del minimum spanning tree ottenuto dagli algoritmi. 

## Domanda 2
Commentate i risultati che avete ottenuto: come si comportano gli algoritmi rispetti alle varie istanze? C'è un algoritmo che riesce sempre a fare meglio degli altri? Quale dei tre algoritmi che avete implementato è più efficiente? 

## Cosa consegnare
- Una breve relazione sullo svolgimento del progetto. La relazione deve contenere:
    - una sezione introduttiva con la descrizione degli algoritmi e delle scelte implementative che avete fatto;
    - grafici esplicativi dei risultati con le risposte alle due domande;
    - eventuali originalità introdotte nell'elaborato o nell'implementazione;
    - una sezione conclusiva in cui porre i vostri commenti e le vostre conclusioni sull’elaborato svolto e i risultati ottenuti.
- Il codice sorgente dell’implementazione in un unico file di archivio (.zip, .tar.gz, ecc.).

## Note generali
L'esercitazione si può implementare con qualsiasi linguaggio di programmazione. Strutture dati di base come liste, code, pile, insiemi, dizionari o mappe, messe a disposizione dalle librerie standard del linguaggio, sono utilizzabili senza restrizioni. Non è consentito utilizzare librerie che forniscono direttamente le strutture dati e gli algoritmi per rappresentare e manipolare grafi, come NetworkX, JGraphT o simili.
Commenta le parti essenziali del codice in modo che sia possibile cogliere le idee che hanno portato alla scrittura di quel codice. I commenti aiuteranno a chiarire se un bug è un errore concettuale o solo un piccolo errore.
