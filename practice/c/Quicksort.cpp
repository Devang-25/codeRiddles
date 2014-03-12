#include<iostream>
#define n 10;

using namespace std;

int split(int A[n],int i,int j)
{
int pivot= i;
i=i+1;
int temp;

while(i<=j)
	{
		while(A[pivot] > A[i])
			{ i++; }
		while(A[pivot] < A[j])
			{ j--; }
		
		// swapping
		if(i<j)
		{		
			temp=A[i];
			A[i]=A[j];
			A[i]=temp;
		}			
	}

//swap with pivot element
temp=A[pivot];
A[pivot]=A[j];
A[j]=temp;

return j;

}

void Quicksort(int A[n], int start, int end)
{
int post;
if(start<end)
	{
		post= split(A,start,end);
		Quicksort(A,start,post-1);
		Quicksort(A,post+1,end);
	}

}

void main()
{
int start=0, end=9;
int ar[10]={12,4,8,14,5,7,3,13,6,9};
Quicksort(ar,start,end);

for(int i=0;i<10;i++)
	cout<<ar[i]<<" ";
}


