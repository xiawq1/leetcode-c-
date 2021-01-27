#include <stdio.h>
int main()
{
    int x;
    scanf("%d", &x);
    int one, two, five;
    for (one = 1; one < x*10; one += 1)
    {
        for (two = 1; two < x*10/2; two += 1)
        {
            for (five = 1; five < x*10/5; five += 1)
            {
                if (one + 2*two + 5*five == x*10)
                {
                    printf("%done yuan, %dtwo yuan, %dfive yuan, get x yuan%d\n", one, two, five, x);
                    goto out;
                } 
                
            }
        }
    }
out:
    return 0;
}