#include<stdio.h>
// int main()
// {
//     int n;
//     int sum = 1;
//     int i = 1;
//     scanf("%d", &n);
//     while (i <= n)
//     {
//         sum *= i;
//         i += 1;

//     }
//     printf("%d", sum);
//     return 0;
// }

int main()
{
    int n;
    scanf("%d", &n);
    int i = 1;
    int sum = 1;
    for (i = 1; i<=n; i+=1)
    {
        sum *= i;
    }
    printf("%d", sum); 
    return 0;
}