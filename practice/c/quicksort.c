
#include <conio>

using namespace std;


#define maxsize 6
int A[maxsize];

void quicksort(int a, int b)
{
  int rtidx=0,ltidx=0,k=a,l=0,pivot;
  int leftarr[maxsize],rtarr[maxsize];
  pivot=A[a];
  if(a==b)return;
  while(k<b)
  {
    ++k;
	 if(A[k]<A[a])
	 {
	  leftarr[ltidx]=A[k];
	  ltidx++;
	  }
		else
		{
		rtarr[rtidx]=A[k];
		rtidx++;
		 }
		  }

	 k=a;
	 for(l=0;l<ltidx;++l)A[k++]=leftarr[l];
	 A[k++]=pivot;
	 for(l=0;l<rtidx;++l)A[k++]=rtarr[l];
	 if(ltidx>0)quicksort(a,a+ltidx-1);
	 if(rtidx>0)quicksort(b-rtidx+1,b);
	 }

void printarr(int a)
{
  int i;
  for(i=0;i<a;i++)
  {
  printf("%d",A[i]);
  printf("\n");
  }
  }

int main()
{
  int i,s;
  printf("enter the number of numbers to be entered \n");
  scanf("%d",&s);
  for(i=0;i<s;i++)
  {
	 printf("enter the number \n" );
	 scanf("%d",&A[i]);
	 }
  printf("array before sorting ");
  printarr(s);
  quicksort(0,s-1);
  printf("array after sorting");
  printarr(s);
  }
