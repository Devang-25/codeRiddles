#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

int main(void)
{
  unsigned int lim, i, j;

  printf("Find primes upto: ");
  scanf("%d", &lim);
  lim += 1;
  bool *primes = calloc(lim, sizeof(bool));

  unsigned int sqrtlim = sqrt(lim);
  for (i = 2; i <= sqrtlim; i++)
    if (!primes[i])
      for (j = i * i; j < lim; j += i)
	primes[j] = true;

  printf("\nListing prime numbers between 2 and %d:\n\n", lim - 1);
  for (i = 2; i < lim; i++)
    if (!primes[i])
      printf("%d\n", i);

  return 0;
}
