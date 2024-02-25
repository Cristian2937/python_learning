from ast import Name
from itertools import count
from re import M
import sys
print(sys.executable)

from Classi.FirstClass import Persona # SINTASSI PER IMPORTARE UNA CLASSE DA UN FILE
from Classi.SecondClass import Insegnante # l'import delle classi può essere eseguito in qualsiasi punto dell'applicazione
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
print("Dopo il remove() diventa:" + str(remove_elemento)) # remove come dice il nome rimuove un elemento all'interno del set, se le'elemento non esiste lancia un'eccezione
# remove_elemento.remove("venezia")
# print(remove_elemento) # errore, l'elemento non esiste all'interno del set perciò non è possibile effettuare l'eliminazione 

discard_elemento = {"milano","roma","napoli"}
print("Prima era del discar() era:" + str(remove_elemento))

discard_elemento.discard("venezia")
print("Dopo il discar() diventa:" + str(remove_elemento)) # a differenza del remove, discard non lancia una eccezione se un elemento non è presente nel set 


# Rimuovere l'ultimo elemento dal set 
pop_elemento = {"milano","roma","napoli"}

pop_elemento.pop() # ATTENZIONE: il metodo pop rimuove l'ultimo elemento all'interno di un set, ma dato che il set non è una collezione ordinata l'ultimo elemento verrà rimosso in maniera casuale 
print(pop_elemento)

# Cancellare dalla memoria un set
# PER ELIMINARE DALLA MEMORIA UN SET OCCORRE UTILIZZARE IL COSTRUTTO "del"

del_elemento = {1,2,3,4}
del del_elemento 
# print(del_elemento) # ERRORE: del ha cancellato dalla memoria il set e quindi non è più possibile recuperarne il contenuto

# ------------
print()
print("UNIRE I SET")
# Unire i set

union_set1 = {"roma","milano"}
union_set2 = {"napoli","verona","roma"}
union_all = union_set1.union(union_set2) # union ripulisce i valori duplicati facendo in modo che se ne ottenga solamente uno

print(union_all)


union_update1 = {"roma","milano"}
union_update2 = {"milano","napoli"}

union_update1.update(union_update2) # update come union aggiorna il set e ripulisce i duplicati mostrandone solamente uno

print(union_update1)

print()

set_intersection_update1 = {"roma","milano","napoli"}
set_intersection_update2 = {"milano","venezia","padova"}

# intersection update effettua l'operazione dentro direttamente dentro il set
set_intersection_update1.intersection_update(set_intersection_update2) # restituisce solamente i valori duplicati, fa l'esatto contrario di union e update

print(set_intersection_update1)

set_intersection1 = {"milano","roma"}
set_intersection2 = {"napoli","roma"}

set_intersectionUnion = set_intersection1.intersection(set_intersection2) # al contrario di intersection_update, intersection restituisce un nuovo set e non un valore "None" quindi opera su se stesso
print(set_intersectionUnion)

print()

symmetric_difference1 = {"milano","roma","napoli"}
symmetric_difference2 = {"milano","roma","venezia"}

symmetric_difference1.symmetric_difference_update(symmetric_difference2) # symmetric_difference_update come intersection_update agisce direttamente dentro ad uno dei set senza instanziarne uno nuovo, 
                                                                         # ma non accetta i duplicati

new_symmetric_difference = symmetric_difference1.symmetric_difference(symmetric_difference2) # symmetric_difference per farlo funzionare occorre che sia instanziato in una nuova variabile, 
                                                                                             # symmetric_difference ritorna ogni singolo elemento duplicato che è contenuto in entrambi i set

print(symmetric_difference1)
print(new_symmetric_difference)


# -------------
print()
print("I DICTIONARY")

"""
    I dictionary sono collezioni di dati ordinate, modificabili, ma non accettano duplicati
"""

# Sintassi di un dictionary

persona_dictionary = {
    "Persona1": {
     "nome": "Cristian",
    "cognome": "Pignatiello",
    "eta": 28,
    "eta": 23   
    }
}

print(len(persona_dictionary))

print(type(persona_dictionary))

print(persona_dictionary) # dato che il dictionary non permette duplicati, non lancia errori se ne trova ma prenderà solamente l'ultimo valore duplicato

print(persona_dictionary["Persona1"]["nome"]) # accesso per chiave tramite parentesi quadre
print(persona_dictionary["Persona1"].get("nome"))

print(persona_dictionary.keys()) # con .keys() ottengo tutte le chiavi del dictionary

print(persona_dictionary.values()) # .values() restituisce tutti i valori all'interno del dictionary

print(persona_dictionary.items()) # .items() restituisce una tupla contenente una coppia chiave/valore

print("nome" in persona_dictionary["Persona1"]) # metodo per verificare se una chiave esiste in un dictionary

persona_dictionary["Persona1"].update({"nome":"Antonio"})
persona_dictionary["Persona1"].update({"colore":"Antonio"})
print(persona_dictionary)

# metodo per togliere un elemento dal dictionary
persona_pop_dictionary = {
    "Persona1": {
     "nome": "Cristian",
    "cognome": "Pignatiello",
    "eta": 28,
    "eta": 23
    }
}
persona_pop_dictionary["Persona1"].pop("eta")

print(persona_pop_dictionary)


persona_pop_item_dictionary = {
    "Persona1": {
     "nome": "Cristian",
    "eta": 28,
    "eta": 23,
    "cognome": "Pignatiello"
    }
}
persona_pop_item_dictionary["Persona1"].popitem() # popitem elimina l'ultimo elemento all'interno di un dictionary
print(persona_pop_item_dictionary)

persona_clear_dictionary = {
    "Persona1": {
     "nome": "Cristian",
    "eta": 28,
    "eta": 23,
    "cognome": "Pignatiello"
    }
}

persona_clear_dictionary.clear() # .clear() svuota tutto il dictionary

persona_del_dictionary = {
    "Persona1": {
     "nome": "Cristian",
    "eta": 28,
    "eta": 23,
    "cognome": "Pignatiello"
    }
}

# per i dicionary il del può eliminare dalla memoria anche solamente un elemento presenre all'interno del dictionary
del persona_del_dictionary["Persona1"]["nome"]
# print(persona_del_dictionary["Persona1"]["nome"])

del persona_del_dictionary
# print(persona_del_dictionary) # ERRORE perchè è stato eliminato dalla memoria

# CICLARE SUI DICTIONARY
# 1) utilizzando il ciclo for:

persona_for_dictionary = {
    "Persona1": {
     "nome": "Cristian",
    "eta": 28,
    "eta": 23,
    "cognome": "Pignatiello"
    }
}

# ciclare gli elementi di un dictionary con al suo interno altri elementi
for persone in persona_for_dictionary.items():
    print(persone)

print()
persona_dictionary = {
     "Persona1": {
     "nome": "Cristian",
     "cognome": "Pignatiello",
     "eta": 23,
     "indirizzo": {
         "citta":"Roma",
         "cap":"00175"
     }
    }
}

for key,dati in persona_dictionary.items():

    for k,dato in dati.items():
        print(k)
        if (k == "indirizzo"):
            for ind in dato:
                print(ind)
        print(dato)

# -------------
print()
print("FUNZIONI")

"""
    - Creare una funzione
    - Chiamare una funzione
    
    - Arbitrary arguments, Keyword Arguments, Arbitrary Keyword Arguments
    - Parametri di default
    - Return dei valori
"""

# Dichiarare una funzione
def ciao():         # per dichiarare una funzione non viene utilizzato il costrutto function come gli altri linguaggi ma "def"
    print("Ciao!!")

ciao()              # Una volta creata la funzione per richiamarla occore richiamare il nome della funzione


# Aggiungere dei parametri alle funzioni
def fai_la_pasta(tipo_pasta):
    print("metti l'aqua")
    print("fai bollire")
    print("Metti su "+ tipo_pasta)
    
fai_la_pasta("Mezze maniche")

print()

# dichiarare le funzioni mettendo un asterisco "*" prima della variabile rende possibile l'assegnazione di più argomenti
def fai_la_pasta(*opzioni):
    print("metti l'aqua")
    print("fai bollire")
    print("Metti su "+ opzioni[0])
    if opzioni[1]:                 # DATO CHE L'ASTERISCO RENDE POSSIBILE AGGIUNGERE PIù ARGOMENTI ALLA VOLTA, RENDE POSSIBILE COSTRUIRE CONDIZIONI APPOSITE PER I DIVERSI PARAMETRI
        print("Metti anche il sugo")
    
fai_la_pasta("Spaghetti",True) # True è il secondo argomento in *opzioni
print()

# Keyword arguments permette di non seguire l'ordine degli argomenti a patto che si utilizzi una specifica sintassi
def fai_la_pasta(tipo_pasta, sugo): 
    print("metti l'aqua")
    print("fai bollire")
    print("Metti su "+ tipo_pasta)
    if sugo:
        print("Metti anche il sugo")
        
fai_la_pasta(sugo=True, tipo_pasta="Bucatini")  # Sintassi per le Keyword arguments 
print()

# Sintassi per dichiarare parametri di default nel caso non si vengano aggiunti argomenti nel momento in cui viene richiamata la funzione
def fai_la_pasta(tipo_pasta = "Spaghetti"): 
    print("metti l'aqua")
    print("fai bollire")
    print("Metti su "+ tipo_pasta)
    
fai_la_pasta()
print()


def fai_la_pasta(tipo_pasta = "Spaghetti")-> str:  # per far si che il valore di ritorno sia quello che vogliamo noi utilizzare la sintassi "-> tipo_di_dato"
    print("metti l'aqua")
    print("fai bollire")
    return "Metti su "+ tipo_pasta

print(fai_la_pasta())



# ---------
print()
print("Classi e oggetti")

"""
    - Creare una classe
    - Instanziare un oggetto
    - Il parametro self
    - Modificare, eliminare proprietà di un oggetto
    - Eliminare l'oggetto
"""

# Sintassi per instanziare l'oggetto
persona1 = Persona()
persona1.set_nome("Jhon")
persona1.set_cognome("Lennon")
print(persona1.nome,persona1.cognome)

# ----------
print()
print("Ereditarietà")

"""
    - Creare una classe figlia (guardare SecondClass nel file Classi)
    - Costruttore della classe figlia (guardare SecondClass nel file Classi)
    - La funzione super
    - Proprietà esclusive della classe Figlia
    - i metodi e l'overriding
"""

insegnante1 = Insegnante() # questa classe al suo interno ha ereditato la classe Persona (guardare SecondClass nel file Classi)
insegnante1.set_nome("Giovanni")
insegnante1.set_cognome("Il bro")
insegnante1.set_categoria("Tutor")
print(insegnante1.to_string() + " ed è "+ insegnante1.get_categoria()) # metodo to string custom (guardare SecondClass nel file Classi)
insegnante1.saluta()

# --------
print()
print("MODULI")

"""
    - Cos'è un modulo : un modulo è un file esterno con all'interno delle funzioni
    - Creare un modulo
    - Funzioni e variabili in un modulo
    - Creare un alias
    - Moduli built in (platform,math)
    - Funzione dir()
    - Importare solo una parte del modulo
"""
                        # l' "as" può essere utilizzato per dichiarare alias per i moduli
import moduli.firstModule as miomodulo # E' possibile importare i moduli in qualsiasi punto dell'applicazione

persona = miomodulo.persona1 # ho importato dal modulo firstModule il dictionary persona1
miomodulo.saluta(persona["nome"])# ho importato dal modulo firstModule la funzione saluta

# E' possibile importare anche solo una parte di un modulo nel caso in cui non ci occorre tutto il suo contenuto es.
from moduli.firstModule import persona2 
persona = persona2  # da firstModule importo solamente il dictionary persona2
print(persona["nome"])

print()

# ALCUNI moduli built-in di python:
import platform as pt
system = pt.system()
processor = pt.processor()
print(system)
print(processor)


import math # Modulo math in python
pi_greco = math.pi
print(pi_greco)

print(math.floor(2.90))

# IMPORTANTE ED UTILE
"""
    Se vogliamo sapere quali metodi/argomenti/attributi esistono all'interno di un modulo
    possiamo utilizzare la funzione dir()
"""

print(dir(math)) # Quì tramite la funzione dir ottengo tutti i metodi disponibili all'interno del modulo math

print()

print(dir(pt)) # Quì tramite la funzione dir ottengo tutti i metodi disponibili all'interno del modulo platform

# -----------
print()
print("DATE")

import datetime as dt # assegnare sempre un alias per gli import

dataNow = dt.datetime.now() # con .now() si ottiene il current timestamp
print(dataNow)

dataPrecisa = dt.datetime(2024,2,13) # sintassi per dichiarare una data partendo da un timestamp preciso
print(dataPrecisa)

dataFormat = dt.datetime.strftime(dt.datetime.now(),"%d/%m/%Y %H:%M:%S") # .strftime(tempo,formato) prende due parametri, 
                                                                # il primo sarebbe il timestamp effettivo, il secondo invece il formato che si vuole ottenere 
print(dataFormat)

# -----------
print()
print("JSON")

"""
    - Leggere i JSON
    - Dati convertibili in JSON:
        # dict
        # list
        # tuple
        # string
        # int
        # float
        # True
        # False
        # None
    
    - Formattare il JSON
    - Ordinare il JSON
"""
import json

json_esempio = '{"nome":"Luca","cognome":"Rossi","eta":25}'

json_loads = json.loads(json_esempio)
print(json_loads)
print("Tipo del JSON: " + str(type(json_loads))) # una volta trasformato in JSON 

for load in json_loads:
    print("Chiave: "+ str(load) +", valore: " + str(json_loads[load]))

print()   
json_dict = {
    "nome": "Jhonny",
    "eta": 24
}

json_load = json.dumps(json_dict) # .dumps() trasforma un dictionary in un JSON, o meglio in una stringa (il JSON di base è una stringa)
print(json_load)
print(type(json_load)) # ritorna str perchè il JSON di base è una stringa

json_format = {
    "nome": "Jhonny",
    "eta": 24,
    "isOnline": False,
    "interessi": ["sport"],
    "moneteInTasca": None
}

json_formatted = json.dumps(json_format,indent = 4) # con indent è possibile indentare il JSON in modo da ottenere una formattazione più leggibile
print(json_formatted)

print()

json_formatted = json.dumps(json_format,indent = 4,separators=(". ","= ")) # se si aggiunge separators=(tuple) si possono cambiare i separatori all'interno del JSON
print(json_formatted)

print()

json_formatted = json.dumps(json_format,indent = 4,separators=(". "," = "),sort_keys=True) # se si aggiunge sort_keys=bool si possono ordinare le chiavi se True le ordina in modo crescente False in modo decrescente all'interno del JSON
print(json_formatted)

# -----------
print()
print("PIP")

"""
    - Introduzione a PIP e ai pacchetti
    - Check e installazione PIP (python get-pip.py), download pacchetti
    - Usare, rimuovere e mostrare pacchetti
    
    (pypi.org sito per scaricare i pacchetti in python)
    
    - IMPORTANTE!: per gli importi di moduli esterni fare attenzione al tipo di interprete che si utilizza
"""

import camelcase

camelcase_instance = camelcase.CamelCase()
frase = "hello world"

print(camelcase_instance.hump(frase))

# ----------
print()
print("Try Except")

"""
    - Errore vs Error handling
    - Multiple exception
    - else
    - finally (esempio file)
    - raise/throw exception

"""

# Come gestire gli errori in python:
#   - attraverso il try except

# print(variabile_inesistente) # ERRORE: variabile_inesistente non è definita

# NameError
try:
    print(variabile_inesistente)
except NameError:
    print("Si è verificato un problema perchè variabile_inesistente non è definita")
finally:
    print("Il finally viene sempre eseguito dopo un try...except")
    
print()
    
cinque = 5
try:
    print("ciao " + cinque)
except TypeError:
    print("non è possibile unire una stringa e un intero insieme")
else:
    print("Nessun problema")
    
meno_uno = -1

# if meno_uno < 0:
    # raise Exception("Numero minore di zero") # il "raise" a quanto pare esegue la stessa logica del throw, una volta lanciato l'errore non è più possibile andare avanti con l'applicazione

# ------------
print()
print("User Input")

"""
    - Creare persona
    - Creare tupla operazioni
    - Definire start
    - Chiamare start
    - Aggiungere traccia per modifica ed eliminazione
"""

persona = {
    "nome":"Luca",
    "cognome":"Rossi",
    "eta": 25
}

operazioni = ("aggiungere","modificare","eliminare","uscire")

def start():
    operazione = input("Cosa vuoi fare? ")
    if operazione == operazioni[0]:
        ins = input("Aggiungi chiave valore separati da una virgola: ")
        aggiungi(ins.split(","))
    elif operazione == operazioni[1]:
        mod = input("Cosa vuoi modificare: ")
        modifica(mod.split(","))
    elif operazione == operazioni[2]:
        el = input("Cosa vuoi eliminare? ")
        elimina(el.split(","))
    
def aggiungi(param):
    chiave = param[0]
    valore = param[1]
    persona[chiave] = valore
    print(persona)
    
def modifica(param):
    chiave = param[0]
    valore = param[1]
    persona[chiave] = valore
    print(persona)
        
        
def elimina(param):
    chiave = param[0]
    # valore = param[1]
    # persona[chiave] = valore
    persona.pop(chiave)
    print(persona)
    
# INIZIO OPERAZIONE
#SCOMMENTARE QUANDO SI VUOLE RIPROVARE A FAR PARTIRE LA FUNZIONE
# while True:
#     start()


# ---------------
print()
print("FORMATTAZIONE DELLE STRINGHE")

"""
    - Formattazione base
    - Valori multipli
    - Indici
    - Indici nominali
"""


peso = 65
altezza = 178

# FORMATTAZIONE STRINGA TRAMITE INDICI NUMERATI
frase = "Ciao sono Luca e sono alto {0} cm e peso {1}kg".format(altezza,peso)
print(frase)
# FORMATTAZIONE STRINGA TRAMITE INDICI NOMINATIVI
frase = "Ciao sono Luca e sono alto {altezza} cm e peso {peso}kg".format(altezza= altezza,peso= peso)
print(frase)

# -------------------
print()
print("LAVORARE CON I FILE")

"""
    File handling
        # r - Read: apre il file per leggerne il contenuto, errore se non esiste
        # a - Append: apre il file per mettere in coda il contenuto, lo crea se non esiste
        # w - Write: apre il file per scrivere, lo crea se non esiste
        # x - Create: crea il file, errore se già esiste
    
    - Aprire un file
    - Leggere un file: intero o una parte
    - Scrivere in un file
    - Creare un file
    - Eliminare file (check) e eliminare la cartella   
"""


FILESTREAM = "testo.txt"
fileOpen = open(FILESTREAM,"w")
fileOpen.write("Hello World")

fileOpen.close()

fileAppend = open(FILESTREAM,"a")
fileAppend.write("\nHello world 2")

fileAppend.close()
   
fileRead = open(FILESTREAM,"r")
print(fileRead.read())

fileRead.close()

# ELIMINARE UN FILE

import os

# os.remove("testo.txt") # RIMUOVE UN FILE DALLA DIRECTORY INDICANDO IL PATH DOVE DEVE ANDARE AD ELIMINARE IL FILE

# ELIMINARE UNA CARTELLA SEMPRE CON L'IMPORT os
if os.path.exists("prova"):
    os.rmdir("prova")
    print("Cartella eliminata con successo!!")
else:
    print("Nessuna cartella trovata")

   



