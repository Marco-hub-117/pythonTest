# Alcuni esempi dei metodi più comunemente usati per le liste in Python

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)

print('Apple number is',fruits.count('apple'))
print('l\'indice della prima banana è', fruits.index('banana'))
print('l\'indice della banana dopo l\'indice quattro è', fruits.index('banana', 4))

print('ora inverto l\'ordine della lista esempio')
fruits.reverse()
print(fruits)

# LIST COMPREHENSION:
# Consite nel creare una lista in un modo coinciso. È possibile farlo usando le parentesi quadrate
# seguite da una clausola for, e poi zero o più for o if 
# ESMEPIO

# metdodo classico:
squares = []
for x in range (10): 
	squares.append(x**2)

print(squares)

# Metodo coinciso:

squares = [x**2 for x in range(10)]
print(squares)

# oppure, per creazione lista di punti secondo una logica
points = [(x,y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(points)

# NESTED LIST COMPREHENSION
# esempio con l'uso delle matrici per creare la matrice trasposta

matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12]
	]

transposed = [[row[i] for row in matrix] for i in range (4)]

print(matrix)
print(transposed)

# ESEMPI TUPLE IN PYTHON
print('\n\n@@@ ESEMPI DI TUPLE DOPO @@@')
t = 12345, 54321, 'hello!' # Questo è un esempio di tupla. 
# Una tupla consiste in un numero di valori separati da virgola
print(t)
print(t[0]) # È possibile accedere ad un valore attraverso gli indici
# Possono esistere le tuple nidificate, per esempio:
u = t, (1, 2, 3, 4, 5)
print(u)

# Le tuple sono immutabili quindi
# t[0] = 8888 non è possibile, genera un errore

# Ma una tupla può contenere oggetti mutabili
v = ([0, 1, 2], [3, 2, 1])

empty = () # le parentesi tonde sono necessarie per creare una tupla vuota
print('La dimensione della tupla empty è',len(empty))
singleton = 'hello', # la virgola finale è necessaria per creare una tupla di dimensione uno
print('La dimensione della tupla singleton è',len(singleton))

# è possibile effettuare lo spacchettamento di una tupla attraverso la seguende assegnazione:
x, y, z = t
# Questa operazione di 'spacchettamento di sequenze' richiede che ci siano 
# tante variabili a sinistra dell'uguale tanti quanti sono gli elementi della sequenza

# ESEMPI DI INSIEMI (SET) IN PYTHON
# È possibile definire un insieme usando la funzione set() oppure le parentesi {}
print('\n\n@@@ ESEMPI DI INSIEMI (SET) DOPO @@@')
basket = {'orange', 'apple', 'apple', 'pear', 'orange', 'banana'}
print(basket) # dalla stampa si noterà che i duplicati saranno stati rimossi
if 'orange' in basket:
	print("orange presente")
else:
	print('orange assente')

if 'ananas' in basket:
	print("ananas presente")
else:
	print('ananas assente')

# Sono possibile le classiche operazioni dugli insiemi, per esempio vediamo sulle lettere uniche di due parole

a = set('abracadabra')
b = set ('alacazam')

print('insieme a:',a)
print('insieme b:',b)

print('a - b:',a - b) # lettere in a, ma non in b
print('a | b:',a | b) # lettere presenti in a o b o in entrambi
print('a & b:',a & b) # lettere in entrambi gli insiemi a e b
print('a ^ b):',a ^ b) # lettere in a o b, ma non in entrambi

# ESEMPI DI DIZIONARI DOPO
print('\n\n@@@ ESEMPI DI DIZIONARI DOPO @@@')
# Un dicctionary è un insieme di coppie di tipo chiave:valore, 
# con il vincolo che ogni chiave è unica all'interno di un dizionario.
# Per creare un dizionario vuoto è possibile usare  le parentesi graffe {}. 
# mettendo un inseme di chiave:valore separato da virgola è possibile inserire dei valori iniziali all'interno del dizionario.
# Se salvo un valore utilizzando una chiave che è già in uso, il valore precedente viene sovrascritto.
# È un errore cercare di estrarre un valore attraverso una chiave che non esiste.
# Usare la funziojne list(dizionario) mi restituisce una lista con tutte le chiavi usate nel dizionario
# Di seguito un breve esempio dell'uso di un dizionario.

tel = {'Jack': 4098, 'Sape': 4139} # inizializzazione dizionario
tel['guido'] = 4127 # aggiungo un nuovo elemento al dizionario
print(tel)
print('Il telefono di Jack è:',tel['Jack'])

# quando le chiavi sono stringhe è più comodo usare questo metodo per creare il dizionario:
pil = dict(vale=46, pecco=63)
print(pil)

# ESEMPI DI TECNICHE DI LOOP DOPO
print('\n\n@@@ ESEMPI DI TECNICHE DI LOOP DOPO @@@')

# con il metodo items() è possibile recuperare contemporaneamente chiave e valore
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)
print()

# quando ciclo su una sequenza, l'indice della posizione e il corrispondente valore 
# possono essere recuperati contemporaneamente usando la funzione enumerate()
for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)
print()

# Per ciclare su due sequenze contemporaneamente conviene usare la funzione zip()
questions = ['name', 'quest', 'favorite color'] 
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('What is your {0}? It is {1}'.format(q, a))
print()

# Funzione reversed() per ciclare al contrario su una sequenza
for x in reversed(range(1,10,2)):
	print(x)
print()

# Funzione set() per eliminare i duplicati su una sequenza, sorted() per ordinarla
# fruits definito sopra a riga 3
for f in sorted(set(fruits)):
	print(f)
print()










