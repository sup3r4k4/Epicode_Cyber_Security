#include <stdio.h>
#include <string.h>

/*
Lo scopo di oggi è realizzare un piccolo gioco di domanda/risposta in C, il numero e le domande sono a vostra scelta. Il gioco dovrà funzionare in modo tale da:
● Presentare una rapida introduzione all’utente con lo scopo del programma.
● Mostrare all’utente un menu di scelta iniziale tra:
    A) Iniziare una nuova partita;
    B) Uscire dal gioco.
● Ricevere in input la scelta dell’utente.
● Creare o meno una nuova partita in base all’input utente.
● Ricevere in input nome dell’utente in caso di nuova partita.
● Presentare un set di domande all’utente a risposta multipla (almeno 3 risposte a domanda).
● Valutare la risposta utente per ogni domanda ed aggiornare una variabile «punteggio in caso di risposta esatta».
● Scrivere a schermo a fine partita il punteggio totalizzato dal giocatore corrente.
● Presentare nuovamente il testo per la scelta tra:
    A) Iniziare una nuova partita;
    B) Uscire dal gioco.
*/

//Definizione funzione per interrompere esecuzione a fine quiz
void finequiz(int punteggio_finale) {
    printf("FINE!!! Il tuo punteggio totale e': %d punti!!\n\n", punteggio_finale);
}
// definizione funzione del quiz vero e proprio
void quiz() {

    int risposta = 0, punteggio_finale = 0;
    char nome_utente[30];
            
            printf("Come ti chiami?  ");
            scanf("%s", &nome_utente);
            printf("\nD'accordo %s si parte!!\n", nome_utente);
            
            printf("\nDOMANDA N.1:\nPer cosa usi la funzione 'printf()'?\n\n");
            printf("1. Per mandare in stampa una pagina Word.\n2. Per stampare a schermo l'output di un programma.\n3. Per allocare memoria.\n");
            printf("\nLa tua risposta: ");
            scanf("%d", &risposta);

            //Utilizzo lo switch per effettuare il controllo sulla risposta data alle domande
            switch(risposta){
            case 1:
                printf("Risposta errata!! Punteggio 0\n");
                break;
            case 2:
                printf("Risposta esatta!! Punteggio +5\n");
                punteggio_finale += 5; //ad ogni risposta esatta aggiorno il punteggio
                break;
            case 3:
                printf("Risposta errata!! Punteggio 0\n");
                break;
            default:
                printf("Risposta inesistente...sai leggere?!\n");
                break;
            }

            printf("\nDOMANDA N.2:\nCome definisci la funzione 'main()'?\n\n");
            printf("1. La prima funzione principale che chiama tutte le altre funzioni.\n2. La funzione che contine tutto il codice del programma.\n3. E' messa li' per bellezza.\n");
            printf("\nLa tua risposta: ");
            scanf("%d", &risposta);
            switch(risposta){
                case 1:
                    printf("Risposta esatta!! Punteggio +5\n");
                    punteggio_finale += 5;
                    break;
                case 2:
                    printf("Risposta errata!! Punteggio 0\n");
                    break;
                case 3:
                    printf("Risposta errata!! Punteggio 0\n");
                    break;
                default:
                    printf("Risposta inesistente...sai leggere?!\n");
                    break;
            }

            printf("\nDOMANDA N.3:\nCome ti può tornare utile il ciclo for nella programmazione?\n\n");
            printf("1. Si puo usare per stampare tutti i numeri di un array di interi a schermo.\n2. Si puo' usare per ripetere una istruzione un numero definito di volte.\n3. Entrambe le risposte sono corrette.\n");
            printf("\nLa tua risposta: ");
            scanf("%d", &risposta);
            
            switch(risposta){
                case 1:
                    printf("Risposta errata!! Punteggio 0\n");
                    finequiz(punteggio_finale); //invoco la funzione che permettere di stampare a schermo il punteggio finale
                    break;
                case 2:
                    printf("Risposta errata!! Punteggio 0\n");
                    finequiz(punteggio_finale);
                    break;
                case 3:
                    printf("Risposta esatta!! Punteggio +5\n");
                    punteggio_finale += 5;
                    finequiz(punteggio_finale);
                    break;
                default:
                    printf("Risposta inesistente...sai leggere?!\n");
                    finequiz(punteggio_finale);
                    break;
            }               
           
}

int main() {

    char scelta_menu;

    do{
        printf("\nPiccolo programma che segue un breve quiz a scelta multipla\nin cui verra' assegnato un punteggio ad ogni risposta corretta.\n\n");
        printf("***MENU DI GIOCO***\nA. Inizia Partita\nB. Esci dal gioco\n");
        printf("\nDigita scelta:");
        scanf("%c", &scelta_menu);

        //effettuo un controllo sulla risposta dell'utente per decidere se avviare la partita o uscire dal gioco
        if(scelta_menu == 'a' || scelta_menu == 'A'){
            quiz();
        }if(scelta_menu == 'b' || scelta_menu == 'B') {
            printf("Sei uscito dal gioco.\n");
        }else{
            printf("Errore comando non valido!!\n\n");
        }
    }while(scelta_menu == 'a' || scelta_menu == 'A'); //utilizzo un ciclo do-while per mantenere a schermo il menu anche alla fine del quiz

    return 0;
}