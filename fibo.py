# Fibonacci numbers module

def fibStampa(n):	# Scrive la serie di finonacci fino a n
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a + b
	print()

def fib(n):	# Ritorna una lista contenente la serie di fibonaci fino a n
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result

# La parte di codice seguente verrà eseguita solo se questo modulo verrà chiamato come script
# perchè l'if seguente è vero solo se il module viene eseguito come main file
# Quindi se da riga di comando chiamo "python3 fibo.py 1000" mi verrà eseguito il codice,
# ma se importo questo modulo all'interno di un altro programma il codice seguente non sarà eseguito.
if __name__ == "__main__":
	import sys
	fibStampa(int(sys.argv[1]))