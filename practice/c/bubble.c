#include <stdio.h>

void main( )
{
	int arr[5], int k ;
	for(k=0;k<=5;k++)
	{
	scanf("%d",&arr[k]);
	}
	int i, j, temp ;
	for ( i = 0 ; i <= 3 ; i++ )
	{
		for ( j = 0 ; j <= 3 - i ; j++ )
		{
			if ( arr[j] > arr[j + 1] )
			{
				temp = arr[j] ;
				arr[j] = arr[j + 1] ;
				arr[j + 1] = temp ;
			}
		}
	}

	printf ( "\n\nArray after sorting:\n") ;

	for ( i = 0 ; i <= 4 ; i++ )
		printf ( "%d\t", arr[i] ) ;
}
