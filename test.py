# Questo è il primo commento 
print("hello!")

# esempio stupido di ciclo for
for x in range(3):
	print(x)

# ESEMPI DI CALCOLI NUMERICI
print("\n@@@ ESEMPI DI CALCOLI NUMERICI DOPO @@@\n")

esempioEspressione = 50 - 5*6
print(esempioEspressione)

divisione = 9/4 #La divisione restituisce sempre un float...
print("Divisione che restituisce float: ",divisione)

divisione = 9//4 #... ma usando "//" ogni parte frazionale viene scartata
print("Divisione che restituisce intero: ",divisione)

resto = 9%4 # questo operatore restituisce il resto della divisione
print("resto della divisione: ", resto)

potenza = 5**2 # L'operatore "**" equivale alla potenza
print("Il risultato di 5**2 è: ", potenza)

# ESEMPI DI USO DI STRINGHE
print("\n@@@ ESEMPI USO STRINGHE DOPO@@@\n")

print("\"\\\" è usato come carattere di escape, \ninfatti è possibile includere  \" o \' in una stringa")

# come non far interpretare \ come carattere di stringa
# È possibile mettere il carattere r seguito dalla stringa virgolettata 
# per far interpretare la succesiva stringa come una stringa pura, come nel seguente esempio:

print("C:\some\name") # In questo caso \n viene considerato come carattere di new line
# OUTPUT:
# C:\some
# ame

print(r"C:\some\name") # In questo caso la stringa viene interpretata come pura
# OUTPUT:
# C:\some\name

# è possibile includere automaticamente gli a capo per generare un output
# su più linee usando i "triple-quotes" --> "..." o '...', nel seguente modo
print("""
Nome:		Marco
Cognome:	Martellotta	
	""")

# È possibile concatenare più stringhe usando + 
# oppure usando * è possibile ripetere più volte una stringa
print(3*"si" + "iuuuum")

# e possibile concatenare più stringhe senza l'uso del +, 
# particolarmente utile quando devo spezzare una stringa su più righe
print ("Stringa sulla prima lineaaaaaaa, verrà lunghiiiiiiiiii"
	"iiiiiiiissima!") 

# È possibile accedere ai singoli caratteri di una stringa usando indici numerici;
# indici numerici parrtono a contare dall'ultimo carattere;
# Se si cerca di accedere ad un indice troppo grande verrà generato un'errore

word = "Python"
print(word[0])  # stampo il primo carattere della stringa
print(word[-1]) # stampo l'ultimo carattere della stringa

# È possibile fare pure delle operazioni di 'slicing' usando i due punti 
print(word[0:2]) # stampa "Py", perchè il carattere 0 è incluso mentre il carattere 2 è escluso
print(word[2:5]) 
print(word[:2])	# Dal primo carattere incluso al secondo carattere escluso
print(word[2:]) # dal carattere a posizione due (il terzo) all'ultimo  
# Nota che se ho una stringa s allora è sempre vero che s[:i] + s[i:] = s


# ESEMPI DI USO DI LISTE
print("\n@@@ ESEMPI USO LISTE DOPO@@@\n")

# In Python una lista è un insieme di valori separati dalla virgola racchiusi tra parentesi quadre

squares = [ 1, 4, 9, 16, 25]
print(squares)

# È possibile indicizzare le liste esattamente come le stringhe
print(squares[:3])
print (squares[0])

# È possibile anche concatenare le liste
print(squares+[36,39,64,81,100])

# Al contrario delle stringhe che sono immutabili, è possibile correggere elementi di una lista
cubes = [1, 8, 10, 64] # c'è qualcosa di sbagliato
print(cubes)
cubes[2] = 3**3
print(cubes)

# è possibile concatenare un elemento ad una lista usando il metodo append
cubes.append(5**3)
print(cubes)

# È possibile sostituire parte di una lista o cancellare parte di una lista nel seguente modo

letters = ["a", "b", "c", "d", "e", "f"]
print(letters)
letters[2:4] = ["C", "D"]
print(letters)
letters[2:4] = []
print(letters)

# Esempio di stampa della serie di fibonacci, con qualche considerazione

a, b = 0, 1 # In questo modo assegno ad a il valore 0 e a b il valore 1
while a<1000:
	print(a, end=",") 	# con il secondo argomento passato alla print in questo modo
						# sostituisco il carattere finale predefinito (\n) con il carattere ,
	a, b = b, a+b 	# nota che l'espressione a+b viene valutata prima di qualsisi assegnamento a variabiule, 
					# in questo modo la serie di fibonacci viene calcolata correttamente
print('')

# @@@ ESEMPI DI CONTROLLO DEL FLUSSO DI PROGRAMMA @@@

print("\n@@@ ESEMPI DI CONTROLLO DEL FLUSSO DI PROGRAMMA @@@\n")
x = -1

# Costrutto simile a case switch con l'utilizzo di else if annidati
if x<0: 
	x = 0 
	print("Negativo, cambiato in zero")
elif x == 0: 
	print(" x è uguale a zero")
elif x == 1:
	print("x è uguale a uno")
else: 
	print("x è maggiore di uno")

# esempio di uso del ciclo for

words = ['cat', 'dog', 'aoooo']
for w in words:
 	print(w, len(w))

# Iterare su una collezione
users = {'Marco': 'attivo', 'Davide': 'inattivo', 'Laura': 'inattivo'}
print(users)
# è utile creare una collezione copia
for user, status in users.copy().items():
	if status == 'inattivo': 
		del users[user]
print(users)


# ESEMPIO ELSE PER I CICLI
for n in range(2,10):
	for x in range (2,n):
		if n % x == 0: # ho trovato che x è un divisore di n
			print(n, 'uguale a ', x, '*', n//x) # creo la stampa
			break	# interrompo il for più interno, passo all'n successivo se non ho finito
	else: 	# NB: l'else si riferisce al for, arrivo qui solo se non c'è stata nessuna occorrenza di un break,
			# L'else per i loop funziona in modo similare all'else per uno statemnt "try"
		print(n, ' è un numero primo') # arrivo qui se non ho incontrato nessun divisore, quindi n è primo


# ESEMPIO CONTINUE STATEMENT
for num in range(2,10):
	if num % 2 == 0:
		print (num, 'è un numero pari')
		continue # passo alla prossima iterazione del ciclo senza eseguire nessuna istruzione successiva a questa all'interno del ciclo
	print (num, 'è un numero dispari')

# ESEMPIO DEFINIZIONE DI UNA FUNZIONE
def fib(n): 	# stampa la serie di fibonacci fino ad n
	""" Stampa la serie di fibonacci fino ad un numero n """
	a, b = 0, 1
	while a < n:
		print(a, end= ' ')
		a, b = b, a+b
	print()

fib(1000)	# chiamo la funzione che ho appena definito

def fib2(n): # ritorna una serie di fibonacci fino ad n
	""" Ritorna una lista contenente la serie di fibonacci fino ad n """
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result	

f100 = fib2(100)
print(f100)

# ALTRE NOZIONI PER LE FUNZIONI --> https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions

