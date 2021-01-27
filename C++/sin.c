#include<stdio.h>
int main()
{
    int x;
    
    for ( x = 2; x < 100; x ++ )
    {
        int i;
        int isprime = 1;
        for ( i = 2; i < x; i ++ )
        {
            if ( x % i == 0 )
            {
                isprime = 0;
                break;
            }

        }
        if (isprime == 1)
        {
            printf("%d\n", x);
        }


    }
    printf("\n");
    return 0;
}

//函数
int isprime(int i)
{
    int ret = 1;
    int k;
    for (k=2; k<i-1; k++)
    {
        if (i%k == 0)
        {
            ret = 0;
            break;
        }
    }
    return ret;
}