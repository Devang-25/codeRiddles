// To print a matrix

#include<stdio.h>
//#define rw 3
//#define cl 4
void main()
{
  int const rw=3;
  int const cl=4;
  int i,j;

  int a[rw][cl]={1,2,3,4,2,3,4,5,3,4,5,6};

  for(i=0;i<3;i++)
    {
      for(j=0;j<4;j++)
	{
	  printf("%d",a[i][j]);
	  if(j==3)
	    {
	      printf("\n");
	    }
	}
    }
}

