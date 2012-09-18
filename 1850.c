#include <stdio.h>

int factorial(int k)
{
    if(k==0)
        return 1;
    int i, c=1;
    for(i=2; i<=k; i++)
        c *= i;
    return c;
}
int comb(int n,int t)
{
    if(n>t)
        return factorial(n)/(factorial(n-t)*factorial(t));
    if(n==t)
        return 1;
    if(n<t)
        return 0;
}
int main()
{
    char word[10];
    /* Get input */
    scanf("%s", word);
    return 0;
}
