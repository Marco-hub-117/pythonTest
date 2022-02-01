# In questo programma sono presenti alcuni esempi per l'input-output in python

import math

# per usare una "formatted string literals" mettere una f o F prima di una stringa;
# All'interno della stringa è ora possibile includere delle espressioni all'interno delle {}
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

# È possibile inoltre usare il metodo string.format()
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} Yes votes {:2.2%}'.format(yes_votes, percentage))
print()

print('The value of pi is approximately {math.pi:.3f}.')
print()

piloti = {'Vale': 46, 'Pecco': 63, 'Merd': 93 }

for nome, numero in piloti.items():
	print(f'{nome:10} ==> {numero:10d}')
print()

# Per maggiori informazioni per formattare al meglio le stringhe:
# https://docs.python.org/3/library/string.html#formatspec


# Di seguito ci sranno alcuni esempi nella lettura/scrittura di file
print('@@@ ESEMPI NELLA LETTURA/SCRITTURA DI FILE @@@')

# per aprire un file usare open()
# Accetta due argomenti:
# - il nome del file da aprire
# - il metodo per aprire il file, con la seguente convenzione:
#		- 'r' per aprire in sola lettura
#		- 'w' per aprire in sola scrittura
#		- 'a' per aprire il file per 'appendere' i dati alla fine del file.
#		- 'r+' per aprire in lettura e scrittura
#		- 'b' a seguito della modalità apre il file in modalità binaria

f = open('workfile', 'w')	# se il file non esiste, viene creato
f.close()	# devo chiudere il file una volta finito il suo utilizzo.

# È buona norma usare la keyword "with" per aprire i file.
# Il vantaggio principale è che il file viene automaticamente chiuso quando finisco di usarlo

with open('workfile', 'r+') as f:
	read_data = f.read()

# Possiamo verificare che il file viene automaticamente chiuso:
print('Il file è chiuso?',str(f.closed))

# Di seguito un'esempio di scrittura e lettura di un file
lines = [
	'riga lista 1\n',
	'riga lista 2\n',
	'riga lista 3\n']
with open('./fileTest/esempioScritturaLettura.txt','w') as file:
	file.write('Questa è una prova\n')
	file.writelines(lines)

with open('./fileTest/esempioScritturaLettura.txt','r') as file:
	for line in file:
		print(line)






