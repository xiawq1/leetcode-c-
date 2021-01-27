#include <stdio.h>
int main()
{
   int a = 700;
   int x = 0;
   int ret = 0;
   while (a > 0)
   {
       x = a % 10;
       ret = ret*10 + x;
       printf("a = %d, x = %d, ret = %d\n", a, x, ret);
       a /= 10;
   }
   printf("%d", ret);
   return 0; 
}