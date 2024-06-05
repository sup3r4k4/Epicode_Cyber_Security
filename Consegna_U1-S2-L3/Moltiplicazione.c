#include <stdio.h>
/*Si scriva un programma che segua l'operazione di moltiplicazione tra due numeri inseriti dall'utente.*/
int main() {
    int a = 0, b = 0;

    printf("Dammi due numeri interi dei quali io ti calcolo il prodotto.\n");
    printf("\nInserisci il primo valore:\n");
    scanf("%d", &a);
    printf("Inserisci il secondo valore:\n");
    scanf("%d", &b);
    printf("\nIl prodotto e':  %d\n\n", a * b);
    
    return 0;
}