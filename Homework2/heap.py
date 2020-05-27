
class heap:
    def __init__(self):
        # desc: costruisco le strutture dati richieste dallo heap
        # A: coda di priorita, contiene la label di ciascuna 
        #    nodo ordinato nello heap secondo l'ordine di arrivo
        # position: dizionario che ha per chiave la label del nodo 
        #           e valore la sua posizione nella coda
        # value: dizionario che ha per chiave la label del nodo e 
        #        per valore il costo localmente migliore

        self.A = []
        self.position = dict()
        self.value = dict()

    def add(self,index,val):
        # desc: inserisce un nodo con label index nella coda ed il suo peso
        # index: label del nodo da inserire da inserire
        # value : costo di arrivo al nodo index
        # tempo : O(log(len(A)))

        self.value[index] = val
        n = len(self.A) 
        self.A.append(index)  #metto l'indice in ultima posizione
        self.position[index] = n
        self.bubbleUp(n)

    def isEmpty(self):
        # desc : True se la list e' vuota False altrimenti
        # tempo : O(1)

        return len(self.A) == 0
    
    def bubbleUp(self, i):
        # desc: aggiorna lo heap dopo l'inserimento o la modifica del nodo in posizione i
        # i : posizione del nodo da controllare
        # tempo : O(log(len(A)))

        p = (i-1)//2
        
        while i > 0 and self.value[self.A[i]] < self.value[self.A[p]]:
            #scambio A[i] <-> A[p]
            self.position[self.A[p]] = i
            self.position[self.A[i]] = p
            
            tmp = self.A[p]
            self.A[p] = self.A[i]
            self.A[i] = tmp
            
            i=p
            p=(i-1)//2

    def decreaseKey(self,node_index,newValue):
        # desc : decrementa la value e aggiorna la coda
        # node_index : label del nodo da aggiornare eventualmente
        # newValue : costo da confrontare con quello localmente migliore
        # tempo : O(log(len(A)))

        if self.value[node_index] < newValue:
            return False
        else: 
            self.value[node_index]=newValue
            i = self.position[node_index]
            self.bubbleUp(i)
            return True

    def extractMin(self):
        #desc: estrae il nodo con costo minimo e aggiorna la coda
        #tempo : O(log(len(A))
        
        n = len(self.A)

        minEl = self.A[0]
        del self.position[self.A[0]]
        del self.value[self.A[0]]
        
        self.A[0] = self.A[n-1]
        self.position[self.A[n-1]] = 0
        self.A.pop() #decremento n

        self.trickledown(0)
        return minEl

    def trickledown(self,i):
        #desc: aggiorna la posizione del nodo in posizione i 
        #      suoi figli hanno un costo minore 
        #i: posizione del nodo da controllare
        #tempo : O(log(len(A))

        l = i * 2 + 1
        r = i * 2 + 2 
        smallest = i
        if l < len(self.A) and self.value[self.A[l]] <  self.value[self.A[i]]:
            smallest = l

        if r < len(self.A) and self.value[self.A[r]] <  self.value[self.A[smallest]]:
            smallest = r
        
        if smallest != i:
            self.position[self.A[smallest]] = i
            self.position[self.A[i]] = smallest

            tmp = self.A[i]
            self.A[i]=self.A[smallest]
            self.A[smallest] = tmp
            self.trickledown(smallest)
    
