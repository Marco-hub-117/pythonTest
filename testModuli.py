import fibo
# È possibile anche importare nei seguenti due modi
from fibo import fib, fibStampa 	# Importo solo quello che mi serve
import fibo as fib 		# Importo dando un nome che posso scegliere a piacere
# è possibile combinare anche questi statement:
from fibo import fib as fibonacci

fibo.fibStampa(1000)
print(fibo.fib(1000))

fibLista = fibo.fib 		# Posso anche assegnare ad una variabile la funzione contenuta in un modulo.

print(fibLista(3000))

# La funzione dir() è utile per scoprire quali nomi un modulo definisce, ritorna una lista ordinata di stringhe
print(dir(fibo))

# Per Informazioni sui packages guardare:
# https://docs.python.org/3/tutorial/modules.html#packages