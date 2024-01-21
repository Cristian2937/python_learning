
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



