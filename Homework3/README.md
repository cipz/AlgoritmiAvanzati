# Laboratorio 3 - Minimum Cut

## Descrizione dell'esercitazione
Lo scopo di questo laboratorio è valutare le prestazioni dell'algoritmo di Karger per il problema del minimum cut rispetto a quattro parametri:
- Il tempo impiegato dalla procedura di Full Contraction
- Il tempo impiegato dall'algoritmo completo per ripetere la contrazione un numero sufficientemente alto di volte
- Il discovery time, ossia il momento in cui l'algoritmo trova per la prima volta il taglio di costo mimimo
- L'errore nella soluzione trovata rispetto al risultato ottimo

## Dataset
Il dataset contiene i 40 grafi del dataset di stanford-algs, di dimensione compresa tra 6 e 200 vertici. 
Per ogni istanza del dataset, il file `input_random_numistanza_numvertici.txt` descrive il grafo, mentre il file `output_random_numistanza_numvertici.txt`
contiene il risultato atteso (numero di archi del taglio minimo). 
Ogni file di input  contiene la rappresentazione come liste di adiacenza di un grafo non orientato. 
I vertici sono numerati da 1 a `numvertici`. 
In ogni riga del file, la prima colonna indica l'etichetta del vertice, mentre gli elementi successivi formano la lista di tutti i vertici a cui il
vertice è adiacente. Ad esempio una riga come `"6 155 56 52 120 ..."` indica che il vertice con etichetta 6 è adiacente 
ai vertici con etichette `155,56,52,120, ..., ecc`.

## NOTA:
I risultati attesi sono stati calcolati con un algoritmo non deterministico: potrebbero esserci degli errori nelle istanze di grandi dimensioni. Se il risultato che ottenete è inferiore al risultato previsto per un grafo di dimensione pari o superiore a 150, è probabile che il risultato corretto sia il vostro e non quello presente nel dataset.

## Domanda 1
Misurate i tempi di calcolo della procedura Full_Contraction sui grafi del dataset. Mostrate i risultati con un grafico che mostri la variazione dei tempi di calcolo al variare del numero di vertici nel grafo. Confrontate i tempi misurati con la complessità asintotica di Full_contraction.

## Domanda 2
Misurate i tempi di calcolo dell'algoritmo di Karger sui grafi del dataset, usando un numero di ripetizioni che garantisca una probabilità minore o uguale a 1n
di sbagliare. Mostrate i risultati con un grafico che mostri la variazione dei tempi di calcolo al variare del numero di vertici nel grafo. Confrontate i tempi misurati con la complessità asintotica dell'algoritmo.
Nelle istanze più grandi, il tempo di calcolo necessario a completare tutte le iterazioni potrebbe risultare eccessivo. In questo caso utilizzate un timeout oppure abbassate il numero di ripetizioni per ottenere tempi di esecuzione ragionevoli.

## Domanda 3
Misurate il l discovery time dell'algoritmo di Karger sui grafi del dataset. Il discovery time è il momento (in secondi) in cui l'algoritmo trova per la prima volta il taglio di costo mimimo.  Confrontate il discovery time con il tempo di esecuzione complessivo per ognuno dei grafi nel dataset.

## Domanda 4
Per ognuno dei grafi del dataset, riportate il risultato risultato ottenuto dalla vostra implementazione, la soluzione attesa e l'errore relativo calcolato come SoluzioneTrovata−SoluzioneAttesa/SoluzioneAttesa.
