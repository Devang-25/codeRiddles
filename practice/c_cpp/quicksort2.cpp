#include <iostream>

using namespace std;



int partition(int A[5], int p , int r)
{
   int x,temp , j,i;
x= A[r];
i= p- 1;
for(j=p; j<= r-1 ;j++ )
{

if (A[j]<= x)
{
i = i+1;
temp= A[j];
A[j]=A[i];
A[i]= temp;

}

}
temp= A[r];
A[r]= A[i+1];
A[i+1]= temp;

return i + 1;
}
void quicksort(int A[5],int p ,int r)
{
int q=0;
if (p < r)
{
q = partition(A, p , r);
quicksort(A,p, q-1);
quicksort(A,q+1,r);
}
}

int main()
{

  int A[5]={30, 40 , 20, 95, 50};

cout<<" the elements of array after sorting are:"<<endl;
quicksort(A, 0, 4); 
       for(int i=0; i <= 4; i ++ ){
cout<<A[i]<<endl;
}


}
