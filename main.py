
# il print funziona come un echo in PHP oppure un System.out.println in JAVA
print("Hello World!")


# dichiarazione di variabili
# messaggio = input("Scrivi qualcosa: ")

# print(messaggio)


# dichiarazione di un array
arrayDiValori = [1,2,3,4,5] 

# lettura dell'array (in python è possibile stampare tutto l'array senza ricorrere a metodi particolari)
print(arrayDiValori)

# dichiarazione e assegnazione di un valore alla variabile
a = 10
# variabileSoloDichiarata # ERRORE in python ogni variabile dopo essere stata dichiarata deve essergli assegnato un valore


# in python è possibile dichiarare più variabili utilizzando la sintassi sottostante, in questo caso utilizzando una "," 
# ad ogni variabile deve essere assegnato un valore
x, y, z = 1,2,3

print(x,y,z)

# per assegnare a tutte le varibili lo stesso valore la sintassi è questa
x = y = z = 10
print(x,y,z)


# TIP: python riesce a leggere ed assegnare per ogni variabile dichiarata il singolo elemento dell'array,
# quindi nella sintassi sottostante è possbile eseguirne la lettura dei due elementi degli array per le due variabili assegnate
arr = ["Roma","Milano"]
ro, mi = arr
print(ro,mi)


# cicli in Python
for i in range(len(arr)):
    print(arr[i])

for i in range(2):
    print("numero: " + str(i))


# -------- 
# TIPI DI DATI
print()
print("TIPI DI DATI")

"""
str: "ciao"
int: x = 20
float: x = 20.5
bool: x = True oppure x = False
list: x = ["Roma","Milano"]
tuple: ("Roma","Milano")
dict (dictionary): {"nome":"Cristian", "eta",23}
set: x = {"Roma","Milano","Napoli"}
"""

# funzione per sapere che tipo di dato contiene una variabile
tipoDiDato = True
print(type(tipoDiDato))

# questo è il modo in cui è possibile leggere un dictionary
dictio = {
    "nome":"Cristian", 
    "eta":23
    }
print(dictio["nome"])

cast = str(10)
print(type(cast)) # ritorna stringa 

cast = float(10)
print(cast) # stampa 10.0
print(type(cast))# ritorna float

x = "5"
y = "5"
print(x + y) # concatena le due strighe e restituisce "55"


#---------
# LE STRINGHE
print()
print("LE STRINGHE")

"""
  - è possibile prendere parti di stringhe utilizzando la sintassi
  stringa[:5], stringa[2:], stringa[-5:-2] etc...
  
  - modificare una stringa con i metodi
  upper() lower() strip() split() replace()
  
  - usare format() per combinare stringhe e numeri
  
  - escape dei caratteri 
"""

# piccolo tip è possibile scrivere in un loop una stringa e python può eseguire tot cicli per tot lettere della stringa
# es.
i = 0
for carattere in "computer":
    print(i)
    i += 1

print()    
# prendere dei caratteri specificandone il range tra di loro
# es.

stringa = "ciao sono luca"
print(stringa[:3]) # stamperà solamente "cia"

print(stringa[2:]) # stamperà da "ao sono luca" quindi dalla posizione 2 compresa fino alla fine della stringa

print(stringa[:-5]) # stamperà partendo dalla posizione -5 non compresa la stringa "ciao sono"

print(stringa[1:9]) # stamperà la stringa in un range dalla posizione 1 compresa fino alla 9 non compresa

# la funzione strip() toglie gli spazi a inizio e fine della frase come il trim in PHP

stringaStrip = "  Ciao sono luca   "
print(stringaStrip) # prima dello strip
# per i metodi delle stringhe si puo utilizzare la sintassi con il punto
# es.
print(stringaStrip.strip())

# la funzione replace() prende due parametri il primo quello da cambiare e il secondo quello che deve cambiare
stringaReplace = "ciao sono Orlando"
print(stringaReplace.replace("o","w"))# il replace è case sensitive quindi fa distinzioni tra maiuscole e minuscole

# possibile metodo per concatenare numeri e stringhe tramite funzione format()
x = {
    "anni": 23,
    "peso": 97
}
stringaFormat = "Ciao sono \"Antonio\" ho {} anni e peso {} kg" # dentro la stringa c'è anche un esempio di escape
print(stringaFormat.format(x["anni"],x["peso"]))


# ---------------
# OPERATORI ARITMETICI
print()
print("OPERATORI ARITMETICI")

"""
 - operatori aritmetici
 - operatori di assegnamento
 - precedenza operatori
 - metodi min,max,abs,pow
"""
x = 5
y = 9

print(x + y)    # addizione
print(x - y)    # sottrazione
print(x * y)    # moltiplicazione
print(x / y)    # divisione
print(x % y)    # modulo o resto
print(x ** y)   # potenza
print(x // y)   # arrotondamento per difetto

# operatori di assegnamento

x = 5
print("prima era "+ str(x))
x += 2
print("dopo è " + str(x))

x = 10
y = 20
lista = [10,20,3,90]
print("il numero minore è: " + str(min(x,y))) # min funzione per ottenere il numero maggiore tra due numeri oppure una lista
print("il numero minore è: " + str(min(lista))) # min funzione per ottenere il numero maggiore tra due numeri oppure una lista
print("il numero maggiore è: " + str(max(x,y))) # max funzione per ottenere 

x = -10
print("il valore assoluto di -10 è: " + str(abs(x))) # abs funzione per ottenere il valore assoluto di un numero

x = 2
print(pow(x,2)) # pow funzione per elevare a potenza un numero 


# --------------------------
# Condizioni if
print()
print("Condizioni if")

"""
    - if semplice
    - operatori di comparazione ==, ===, !=, !==, >,<,>=,<=
    - elif (else if), else
    - operatori logici and, or
    - versione short hand
    - if innestati
"""

x = 5

# per le condizioni o per le funzioni è necessario indentare il codice
if x > 10:
    print(str(x) + " è maggiore di 10")
elif x == 10:
    print(str(x) + " è uguale a 10")
else:
    print(str(x) + " non è maggiore di 10")
    
    
x = y = 10

if x > 10 and y < 10:
    print("x e y sono maggiori di 10")
else:
    print("x e y sono uguali a 10")
    
if x > 10 or y == 10:
    print("o X o Y sono uguali a 10")
else:
    print("X e Y non sono uguali a 10")
    
if not (x < 10): # l'operatore "not" equivale al operatore logico !
    print("x non è minore di 10")
else:
    print("x è minore di 10")
    
# condizioni if innestate

""" x = input("verifica se pari o dispari: ")

if (int(x) % 2 == 0):
    print("il numero è pari")
    if (int(x) < 10):
        print("Il numero è pari e minore di 10")
    else:
        print("Il numero è pari e maggiore di 10")
else: 
    print("il numero è dispari") """

    
# -----------------------
# CICLI 
print()
print("CICLI")
"""
   - while e sintassi del ciclo while
   - for e sintassi del ciclo for
   - break, continue, else    
"""

# Ciclo while, il ciclo while per non essere mandato in loop infinito ha sempre bisogno di una condizione
# valida per il quale quando raggiunta il ciclo si fermi altrimenti continua all'infinito 

i = 0

# sintassi while semplice
while i <= 6:
    print(i)
    i +=1

print()
# sintassi while con utilizzo del costrutto "break"

i = 1
#       il costrutto break fa si che raggiunta una certa condizione il loop venga stoppato immediatamente
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print()
# sintassi while con costrutto "continue"

i = 1
#       il costrutto continue, secondo una certa condizione fa saltare l'iterazione
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print()
# sintassi while con costrutto "else"

i = 0
stringaFineCiclo = "il ciclo è finito con il numero {}" 
while i < 6:
    print(i)
    i += 1
else:
    print(stringaFineCiclo.format(i))
    
print()
# sintassi ciclo "for"

x = ["Roma","Milano","Terzo mondo"]


for citta in x:
    print(citta)
    
stringa = "stringa"
for r in range(len(stringa)):
    print(stringa[r])
    
    
    
for colonna in range(6):
    for riga in range(10):
        print("(" + str(colonna) + ": " + str(riga) + ")")
else:
    print("fine ciclo for")
    

# -----------------------------
# COLLEZIONI DI DATI
print()
print("COLLEZIONI DI DATI")

"""
    le collezioni in python prevedono:
    - liste o comunemente chiamati array (in python la definizione corretta è liste)
    - tuple
    - dictionary, la sintassi è simile a quella del JSON
    - set
    
        - le liste sono collezioni ordinate e modificabili. Permettono duplicati
        - le tuple sono collezioni ordinate ma immutabili. Permettono duplicati
        - i set sono collezioni NON ordinate e NON indicizzate. NON permettono duplicati
        - i dictionary sono collezioni ordinate e modificabili (dalla versione 3.7). NON permettono duplicati 
"""

tup = ("ROMA","MILANO")
# tup[0] = "TERZO MONDO" # VERO le tuple non possono essere modificate 
print(tup[0])

# SE OCCORRE UTILIZZARE LA SINTASSI SOTTOSTANTE OVVERO INSTANZIARE L'OGGETTO TUPLA E INSERIRE ELEMENTI AL SUO INTERNO
# OCCORRE DICHIARARE CON DOPPIE PARENTESI TONDE es. tuple((ELEMENTI))
tupla = tuple(("ROMA","MILANO","VENEZIA".lower()))

print(tupla)

# STESSO DISCORSO PER LE LISTE SE SI INSTANZIA L'OGGETTO list OCCORRE DICHIARARE UNA DOPPIA PARTENTESI
# es. list(())
lista = list(())
i = 1
while i < 10:
    lista.append(i)
    i += 1
    
print(lista)

# --------------------------
# METODI DELLE LISTE
print()
print("METODI DELLE LISTE")

"""
    per le liste o le collezioni in generale abbiamo alcuni tipi di metodi:
    - len() : per sapere la lunghezza effettiva della nostra lista, 
              come in altri linguaggi di programmazione funziona allo stesso modo,
              ovvero conta gli elementi effettivi non partendo da 0 ma da 1
"""
lunghezza = list((1,2,3,4,5,6,7))
print("Lunghezza della lista: " + str(len(lunghezza)))


"""
    - type() : come dice il nome è una funzione utile per sapere di che tipo di dato stiamo parlando,
               viene applicato non solo alle liste ma a qualsiasi tipo di dato
"""
tipo = list("sono una lista che al suo interno contiene una stringa")
print("Tipo della stringa: " + str(type(tipo)))

"""
    è possibile accedere agli elementi delle liste in diversi modi:
    - indice singolo
    - range [1:3]
    - negativo
"""
accedereAllElemento = [1,2,3,4]
print(accedereAllElemento[-1]) # accedo all'ultimo elemento della lista
print(accedereAllElemento[1:3]) # accedo agli elementi della lista tramite range partendo dalla posizione 1 fino alla posizione 2 escludendo l'ultima 

cambiareGliElementiInRange = ["milano","roma","napoli","verona","civitaVecchia"]
print("prima del cambio in range dei valori: " + str(cambiareGliElementiInRange))

cambiareGliElementiInRange[2:] = ["venezia","frosinone"] # sto effettuando un cambio dei valori della lista con il nuovo range di valori dalla posizione due fino alla fine
print("dopo il cambio in range dei valori: " + str(cambiareGliElementiInRange))


# -----------------
# METODI DELLE LISTE
print()
print("METODI DELLE LISTE") 


print("Aggiungere elementi alla lista")
"""
    è possibile inserire gli elementi all'interno di una lista eseguendo anche utilizzando dei metodi:
    
    -   append() inserisce un valore all'interno della lista posizionandolo alla fine di essa
    
    -   insert() dove inserisce l'elemento all'interno di una lista specificando in quale posizione essere inserito,
        facendo così sposta la lista di N posizioni per inserire l'elemento nella posizione richiesta
    
    -   extend() come dice il nome estende la grandezza di base della lista permettendo di aggiungere al suo interno tutti
        gli altri elementi di una seconda lista 
"""

list_append = [1,2,3,4,5]
print("Prima list_append era: " + str(list_append))
list_append.append(6) # append inserisce alla fine della lista un nuovo elemento
print("Dopo list_append utilizzando il metodo append() diventa: " + str(list_append))


list_insert = 'a'
print("Prima list_append senza metodo insert() era: " + str(list_append))
list_append.insert(2,list_insert) # utilizzo il metodo insert() per inserire N elementi all'interno di una lista 
                                 # scegliendo in che posizione metterli
print("Dopo list_append con metodo insert() diventa: " + str(list_append))

list_extend = ['a','b','c']
print("Prima list_extend era: "+ str(list_extend))

list_extend2 = list(([1,2,3]))
list_extend.extend(list_extend2)
print("Dopo list_extend utilizzando il metodo extend() diventa: "+ str(list_extend))

print()
print("Rimuovere elementi dalla lista")
"""
    Oltre ai metodi che vanno ad aggiungere elementi all'interno di una lista
    abbiamo anche i metodi che vanno a rimuovere elementi in una lista:
    
    -   remove() la funzione rimuove esattamente la prima occorrenza che trova
    
    -   pop() rimuove un elemento specificando a quale indice rimuoverlo, se non specificato
        va a togliere di default l'ultimo elemento della lista
    
    -(costrutto) del, rimuove totalmente la lista probabilmente fa in modo che venga cancellato il suo indirizzo di memoria 
        non permettendone più la sua lettura
    
    -   clear() pulisce la lista ritornando una lista completamente vuota []
"""

list_remove = [1,2,3,4,5,2]
print("Prima di rimuovere un elemento dentro list_remove era: "+ str(list_remove))

list_remove.remove(2) # La funzione remove() va a togliere la prima occorrenza che trova in questo caso 
                      # è andato a togliere il primo 2 che ha trovato

print("Dopo aver rimosso un elemento dentro list_remove diventa: "+ str(list_remove))
print()

list_pop = [1,2,3,4,5]
print("Prima del metodo pop() list_pop era: " + str(list_pop))

list_pop.pop(0) # specificando al metodo pop() l'indice lui toglie il valore corrisposto
list_pop.pop() # non specificando al metodo pop() cosa deve togliere di default toglierà l'ultimo elemento nella lista
print("Dopo il metodo pop() list_pop diventa: " + str(list_pop))
print()
list_del = [1,2,3,4]
del list_del # il costrutto del va a togliere dalla memoria tutto quello che viene posizionato dopo di esso

# print(list_del) # ritorna un errore perchè del ha eliminato la lista/variabile/oggetto dalla memoria

list_clear = list((1,2))

print("Prima del metodo clear() list_clear era: " + str(list_clear))

list_clear.clear()
print("Dopo il metodo clear() list_clear diventa: " + str(list_clear))
print()

# List comprehension
print("LIST COMPREHENSION")
lista_citta = ['milano','roma','udine']

[print(citta) for citta in lista_citta]

diction = dict({ 
    0:{
        "nome":"Cristian",
        "eta": 23
    },
    1:{
        "nome": "Eliseo",
        "eta": 30
    }
})

newArr = [print(diction[d]) for d in diction if diction[d]["eta"] != 30]


list_sort = ["udine","roma","napoli","venezia"]
print("Prima del metodo sort() list_sort era: " + str(list_sort))

list_sort = [s.upper() for s in list_sort] # utilizzo della list comprehension oltre il metodo sort
list_sort.sort()
print("Dopo il metodo sort() ASC list_sort diventa: " + str(list_sort)) # l'ordine viene eseguito in modo ascendete ASC di default

list_sort.sort( reverse=True )
print("Dopo il metodo sort() DESC list_sort diventa: " + str(list_sort)) # l'ordine viene eseguito in modo ascendete 

# -------------------------
print()
print("TUPLE")

"""
    Per dichiarare una tupla occorre utilizzare le parentesi tonde
    es. creazione_tupla = ("roma",).
    
    é importante per la creazione di una tupla dopo averla dichiarata
    al suo interno dopo il primo elemento bisogna inserire una virgola,
    altrimenti python non riesce ad identificarne il tipo corretto
    es. creazione_tupla = ("roma",)
    
    I metodi delle tuple comprendono: len(), type(), tuple()
"""

creazione_tupla_senza_virgola = ("milano")
print("Per aver omesso la virgola dopo il primo elemento ottengo: " + str(type(creazione_tupla_senza_virgola))) # non avendo inserito la virgola dopo il primo valore il tipo non sarà <class 'tuple'> ma <class 'str'>

    
creazione_tupla_con_virgola = ("roma",)
print("Dopo aver inserito una virgola dopo il primo elemento ottengo: " + str(type(creazione_tupla_con_virgola)))

tuple_len = ("milano","roma","napoli")
print("La lunghezza della tupla è di: " + str(len(tuple_len)))

# Accedere agli elementi della tupla

tuple_access = tuple(("milano","roma","napoli"))
print(tuple_access[0:1])

# condizione if per le liste/tuple

if "milano" in tuple_access:
    print("esiste")
    for i in range(len(tuple_access)):
        print(tuple_access[i])
else:
    print("non ESISTE")

# Rimozione di elementi in una tupla

rimuovi_elemento_tupla = tuple(("milano","roma","napoli"))
#rimuovi_elemento_tupla.remove(0) # ERRORE, le tuple possono avere duplicati ma il loro contenuto non può essere rimosso/sostituito
# print(rimuovi_elemento_tupla)

# Per rimuovere un elemento o cambiarlo occorre prima trasformare una tupla in list ed effettuare il cambio/rimozione e successivamente farla ritornare una tupla

tupla_da_cambiare = ("mil","roma","napoli")
print("Prima del cambio dell'elemento abbiamo: {}".format(tupla_da_cambiare[0]))

# escamotage per cambiare gli elementi di una tupla, ovvero, trasformarla prima in lista modificare l'elemento e poi ristraformarla in tupla
tupla_cambiata = list(tupla_da_cambiare)
tupla_cambiata[0] = 'milano'
tupla_da_cambiare = tuple(tupla_cambiata)

print("Dopo il cambio dell'elemento abbiamo: {}".format(tupla_da_cambiare[0]))

# escamotage per eliminare gli elementi di una tupla, ovvero, trasformarla prima in lista eliminare l'elemento e poi ristraformarla in tupla
tupla_da_eliminare = ("milano","roma","napoli")
print("Prima dell'eliminazione dell'elemento abbiamo: " + str(tupla_da_eliminare))

tupla_eliminata = list(tupla_da_eliminare)
tupla_eliminata.remove(tupla_eliminata[0])
tupla_da_eliminare = tuple(tupla_eliminata)

print("Dopo l'eliminazione dell'elemento abbiamo: " + str(tupla_da_eliminare))

# -------------
print()
print("SPACCHETTARE UNA TUPLA")

citta = ("milano","roma","napoli")

# METODO PER SPACCHETTARE UNA TUPLA,(molto statico) 
(x,y,z) = citta
print(x)
print(y)
print(z)

citta = ("milano","roma","napoli","venezia")

(x,y,*z) = citta # utilizzando l'asterisco * in una delle variabili utilizzate per spacchettare prenderà 2 elementi nella tupla 
print(x)
print(y)
print(z)

# -------------
print()
print("UNIRE LE TUPLE")

"""
    Per unire una tupla ad un'altra basta assegnare l'operatore + tra le due
"""

tup1 = ("milano","roma")
tup2 = ("napoli","venezia")
unione = tup1 + tup2
print(unione)

# -------------
print()
print("ACCEDERE ALL'INDICE DI UNA TUPLA")

access_tuple_index = tuple(("milano","roma","napoli","venezia"))
print("Venezia si trova all'indice: " + str(access_tuple_index.index("venezia")))


# ----------------------
print()
print("SET")

"""
    - I set sono collezioni di dati non ordinate, non indicizzate,
      non modificabili e non permettono duplicati.
    
    - E' possibile creare un set con tipi "normali" o "mischiati"
    
    - Metodi principali dei set: len(), type(), set()
    
    - E' possibile accedere agli elementi dei set con un loop
    
    - Modificare gli elementi di un set non è possibile, si possono solamente aggiungere e rimuovere 
    
    - Metodi per aggiungere elementi ai set: add() update()
    
    - Rimuovere elementi ai set con: remove(), discard(), pop(), clear(), del
    
    - Unire i set con: union() e update(),  intersection_update(), intersection(), symmetric_difference_update(), symmetric_difference() 
"""

# dichiarazione di un set
primo_set = {"milano","roma","napoli"}
secondo_set = {"milano",24,True} # i set accettano diversi tipologie di dato

# DATO CHE I SET NON SONO INDICIZZATI I VALORI ALL'INTERNO DEI SET SARANNO SEMPRE LETTI IN MANIERA CASUALE
print(secondo_set)

# PER POTER ACCEDERE AGLI ELEMENTI DI UN SET E' POSSIBILE FARLO TRAMITE LOOP

for elemento in primo_set:
    print(elemento)
    
print()

# Fun fact mettendo tipi diversi all'interno del set non sempre viene letto in maniera casuale
for elemento in secondo_set:
    print(elemento)
    
# Aggiungere un elemento al set

add_elemento = {"milano","roma","napoli"}
print("Prima dell'aggiunta dell'elemento era: "+ str(add_elemento))

add_elemento.add("venezia")
print("Dopo l'aggiunta dell'elemento diventa: "+ str(add_elemento))

# Unire un set ad un altro set

update_set_uno = {"milano","roma"}
update_set_due = {"napoli","venezia"}


update_set_uno.update(update_set_due) # update va ad unire un set all'interno di un altro
print(update_set_uno)

print()
# Rimuovere elementi nel set 

remove_elemento = {"milano","roma","napoli"}
print("Prima era del remove() era:" + str(remove_elemento))
remove_elemento.remove("milano")
print("Dopo il remove() diventa:" + str(remove_elemento))

discard_elemento = {"milano","roma","napoli"}
print("Prima era del discar() era:" + str(remove_elemento))

discard_elemento.discard("venezia")
print("Dopo il discar() diventa:" + str(remove_elemento)) # a differenza del remove, discard non lancia una eccezione se un elemento non è presente nel set 






