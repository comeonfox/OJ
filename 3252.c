#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXLEN 32
#define printB(x) printf("len: %d\nones: %d\n", x->lenBin, x->onesNum)
#define print(x) printf("%.0f\n",x)

typedef struct binary_struct{
    int *bin;            /*the binary array*/
    int *ones;           /*an array that stores the positions
                                  of 1 in the binary array
                                */
    int lenBin;                 /*the length of the binary array*/
    int onesNum;                /*number of ones*/
} binary;
binary* toBin(int dec)
{
    binary *b=(binary *)malloc(sizeof(binary));
    int bin[MAXLEN],onestemp[MAXLEN], ones[MAXLEN];
    int i=0, onesNum=0,j;
    while(dec>0)
    {
       bin[i++] = dec % 2;
       dec = dec / 2;
    }
    b->lenBin = i;
    for(i=0; i<b->lenBin; i++)
      if(bin[i])
        onestemp[onesNum++]=i;
    //reverse ones
    for(i=onesNum-1,j=0; i>=0; i--)
      ones[i]=onestemp[j++];
    b->bin = bin;
    b->onesNum = onesNum;
    b->ones=ones;
    return b;
}
void ripOffOnes(binary *b)
{
    /* Rip off redundent ones to make a round number*/
    if(b->onesNum > b->lenBin/2)
    {
        int i;
        for( i=0; i<b->onesNum - b->lenBin/2; i++)
          b->bin[b->ones[b->onesNum-i-1]] = 0;
        b->onesNum = b->lenBin/2;
    }
}
int chopBit(binary *b)
{
    memset(b->bin, 1, b->lenBin-1);
    b->lenBin--;
    b->onesNum = b->lenBin;
    int i;
    for( i=0; i<b->onesNum; i++)
      b->ones[i]=i;
    return b->lenBin;
}
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
long long int comb(int n,int t)
{
    long long int mul=1LL, i;
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
void ripTail(binary *b)
{
    if(b->onesNum > 0)
        b->bin[b->ones[--b->onesNum]] = 0;
}

long long int getAll(binary *b)
{
    int i,j=1;
    long long int all=0LL;
    for(  i=b->onesNum-1,j=1; i>0; i--)
       all += comb(b->ones[i],j++);
    return all+1;
}
int compare(binary *b, binary *c)
{
    int i;
    if(b->lenBin > c->lenBin)
      return 1;
    else
      if(b->lenBin < c->lenBin)
        return -1;
      else
        {
            for(i=b->lenBin-1; i>=0; i--)
              if(b->bin[i]!= c->bin[i])
              {
                  if(b->bin[i]>c->bin[i])
                    return 1;
                  else
                    return -1;
              }
            return 0;
        }
}
int main()
{
    int start, finish;
    long long int sum = 0LL;
    binary *bs, *bf;
    scanf("%d %d", &start, &finish);
    bs=toBin(start);
    bf=toBin(finish);

    int i,j;
    for(i=1; i<bf->lenBin; i++)
        for(j=1; i-j>=j; j++)
        {
          if(i==30)
              printf("%lld\n", comb(i-1,j-1));
          sum += comb(i-1,j-1);
        }
    while(bf->onesNum>0)
    {
        ripOffOnes(bf);
        sum += getAll(bf);
        ripTail(bf);
    }

    for(i=1; i<bs->lenBin; i++)
      for(j=1; i-j>=j; j++)
      {
        sum -= comb(i-1,j-1);
        }
    while(bs->onesNum>0)
    {
        ripOffOnes(bs);
        sum -= getAll(bs);
        ripTail(bs);
    }
    printf("%lld\n", sum+1);
    return 0;
}
