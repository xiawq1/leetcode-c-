#include<stdio.h>
int main()
{
    int sum = 0;
    int count = 0;
    int n;
    scanf("%d", &n);
    while (n != -1)
    {
        sum = sum+n;
        count++；
        scanf("%d", &n);   
    }
    printf("%f", sum*0.1/count);
    return 0;
}