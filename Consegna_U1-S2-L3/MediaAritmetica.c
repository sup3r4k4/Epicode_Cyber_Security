#include <stdio.h>
/*Si scriva un programma in linguaggio C che legga due valori interi e visualizzi la loro media aritmetica.*/
int main() {
    int primo_numero = 0, secondo_numero = 0;
    float media = 0.0;

    printf("Dammi due numeri interi dei quali io ti calcolo la media aritmetica.\n");
    printf("Inserisci il primo numero:  ");
    scanf("%d", &primo_numero);
    printf("Inserisci il secondo numero:  ");
    scanf("%d", &secondo_numero);
    media = (float)(primo_numero + secondo_numero) / 2;
    printf("La media aritmetica tra %d e %d e' uguale a: %.1f", primo_numero, secondo_numero, media);

    return 0;
}