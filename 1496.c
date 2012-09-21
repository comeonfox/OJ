#include <stdio.h>
#include <string.h>
#define sigma 26

double factorial(int k)
{
    if(k==0)
        return 1;
    int i;
    double c=1;
    for(i=2; i<=k; i++)
        c *= i;
    return c;
}
double comb(int n,int t)
{
    double mul=1, i;
    if(t>n-t)
        t = n-t;
    if(n>t)
    {
         for( i=n-t+1; i<=n; i++)
           mul *= i;
         return mul/factorial(t);
    }
    if(n==t)
        return 1;
    if(n<t)
        return 0;
}
int isLegal(char *w, int len)
{
    int i;
    for(i=len-1; i>0; i--)
        if(w[i]-w[i-1] <= 0)
          return 0;
    return 1;
}
int main()
{
    char word[11];
    /* Get input */
    while(scanf("%s", word)!=EOF)
    {
        int len = strlen(word);
        if(!isLegal(word, len))
        {
            printf("0\n");
            continue;
        }
        int i=0, wc=0, t=1;
        double sum=0,cb = 0;
        while(t<len)
        {
            cb = comb(sigma, t);
            t++;
            sum += cb;
            cb = 0;
        }
        while(wc<len)
        {
            if( i< (int)(word[wc]-'a'))
            {
                cb = comb(sigma-i-1, len-wc-1);
                i++;
                sum += cb;
                cb = 0;
            }
            else
            {
                wc++;
                if(wc<len)
                  i++;
            }
        }
        printf("%.0f\n", sum+1);
    }
    return 0;
}
