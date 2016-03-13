#include<stdio.h>
#include<iostream>
using namespace std;




int main()
{
    int t[10],i,a,j;
 
    for(i=0;i<10;i++)
    {
        cout << "Type elements of the array: ";
        cin >> t[i];
	
    }
	for(i=0;i<9;i++)
	{
	a=t[i];
	for(j=0;j<9;j++){

	if(t[i]==a){
cout<<"not a unique array";
}
}
}

cout<<"unique array";
return 0;

    
}

