#include <stdio.h>

int main(){

    int x, z;
    long int res = 1;

    printf("Digite o primeiro valor: ");
    scanf("%d", &x);
    printf("Digite o segundo valor: ");
    scanf("%d", &z);

    for(int i = 0; i < z; i++){
        res *= x;
    }

    printf("O numero %d elevado a %d = %ld\n", x, z, res);

    return 0;
}