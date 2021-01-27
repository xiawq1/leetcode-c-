#include <stdio.h>
int main()
{
    int x;
    int n = 0;
    scanf("%d", &x);
    if (x > 0)
    {
        {
        ++n;
        x /= 10;

    }
    }else{
        n = 1;
    }
    while (x>0)
    
    printf("%d\n", n);
    return 0;
}