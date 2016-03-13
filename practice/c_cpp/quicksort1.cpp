#include <iostream>

using namespace std;

int *arr,size;

int partition(int left,int right)
{
 int p,temp,l,r;
 
 while(l<=r)
      {
       while(arr[left]<p)
             left++;
       while(arr[right]>p)
             right--;
       if (l<r)
          {
           temp=arr[l];
           arr[l]=arr[r];
           arr[r]=temp;
          }
      }
 
 temp=arr[left];
 arr[left]=arr[r];
 arr[r]=temp;
 
 return r;
}

void quicksort(int left,int right)
{
 if (left<right)
     {
      int pivot= partition(left,right);
      quicksort(left,pivot-1);
      quicksort(pivot+1,right);
     }
}

int main()
{
 int i;

 cout<<"Enter the number of elements in the array: ";
 cin>>size;

 int *arr=new int[size];

 cout<<"Enter the elements:"<<endl;
 for (i=0;i<size;i++)
       cin>>arr[i];
      
 
    
 cout<<"unsorted array:"<<endl;
 for (i=0;i<size;i++)
     cout<<arr[i]<<endl;
 
 quicksort(0,size-1);

 cout<<"sorted array:"<<endl;
 for (i=0;i<size;i++)
      cout<<arr[i]<<endl;
 return 0;
}
