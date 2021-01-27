#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    srand(time(0));
    int a = rand()%100 + 1;
    int count = 0;
    int n = 0;
    printf("the number between one to hundred");
    do{
        printf("the number you give");
        scanf("%d", &n);
        count += 1;
        if (n > a)
        {
            printf("the number is too big");

        }else if (n < a)
        {
            printf("the number is too small");
        }
        
    }while (n != a);

    printf("got it");
    return 0;
}