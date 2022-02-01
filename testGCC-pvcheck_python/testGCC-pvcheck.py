# Questo programma serve a testare le funzionalità del package os.
# Qui si vede l'uso della funzione os.system, che richiama comandi da riga di comando.
# Alcuni commenti sull'uso dei comandi da terminale qua sotto:
# 1) il primo comando è usato per compilare il programma, accetta alcuni parametri;
#   -Wall sopprime tutti i warning
#	-o outProgProva permette di scegliere il nome del file compilato
# 2) nel secondo comando si vede ./outProgProva 
#	che esegue il programma compilato precedentemente, 
#	e con > outTesto.txt reindirizza la stampa del programma eseguito
#	sul file di testo.

import os

# Prova di compilazione e esecuzione file C
os.system('gcc -Wall helloworld.c -o outProgProva')
os.system('./outProgProva > outTesto.txt')

# Prova pvcheck (con esempio preso dal git di pvcheck)
os.system('gcc -Wall program2.c -o program2') # Compilo il programma su cui eseguire il pvcheck
os.system('./pvcheck --format csv -f esempio2.test ./program2 > outPvcheck.csv') # creo il file csv che conterrà i risultati del pvcheck
# Spiegazioni parti del comando per lanciare il pvcheck
# ./pvcheck ==> esegue il prgramma
# --format csv ==> l'output sarà in formato csv
# -f ==> seleziona il file .test da usare
# esempio2.test ==> il nome del file .test da usare per il programma selezionato
# ./program2 ==> nome del programma (compilato) da eseguire e da testare con il pvcheck
# > outPvcheck.csv ==> redireziono l'uscita del pvcheck nel file outPvcheck.csv
