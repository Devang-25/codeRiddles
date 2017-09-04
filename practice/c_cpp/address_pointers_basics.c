// Run as:
// $ gcc address_pointers_basics.c -o basics.out  && ./basics.out
//

#include <stdio.h>

//#include <conio.h>

void main() {
	int x = 5;
	//int p;
	int *p;
	p = &x;
	printf("Value of x = %d\n", x);
	printf("Address of x through p = %p\n", p);
	printf("Address of (x + 1) through p = %p\n", p+1);
	printf("Value of x through p = %d\n", *p);
	int A[] = {2,3,6,8};
	for(int i=0; i<5; i++) 
	{
		printf("\nFor element %d of Array A[]\n", i);
		printf("Address = %p\n", &A[i]);
		printf("Address = %p\n", A+i);
		printf("Value = %d\n", A[i]);
		printf("Value = %d\n", *(A+i));
	}

	return;
}

