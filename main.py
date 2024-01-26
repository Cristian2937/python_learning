
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

x = input("verifica se pari o dispari: ")

if (int(x) % 2 == 0):
    print("il numero è pari")
    if (int(x) < 10):
        print("Il numero è pari e minore di 10")
    else:
        print("Il numero è pari e maggiore di 10")
else: 
    print("il numero è dispari")

    
    
# -----------------------









