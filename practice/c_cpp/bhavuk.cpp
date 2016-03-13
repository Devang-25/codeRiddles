#include<iostream>
using namespace std;

class Tcase{
public:
  int S,C,N;
  std::string R;
};

int main() {

  int T,diff;
  cin>>T;
  cout<<"\n";
  Tcase tc[T];
  int i;
  //for each Test Case      
  for(i=0;i<T;i++)
    {
      //take input; type:tears & catalysts
      cin >> tc[i].S >> tc[i].N >> tc[i].C;

      //if natural less than target
      if(tc[i].N < tc[i].S){
	//if catalyst is present
	if(tc[i].C>0)
	  {
	    diff = tc[i].S - tc[i].N;
	    if(diff/2 <= tc[i].C)
	      {
		tc[i].R="YES " + diff/2;
		continue;
	      }
	    else
	      {
		tc[i].R="NO";
		continue;
	      }
	  }
	else
	  //natural less and no catalyst; non-achievable target
	  {
	    tc[i].R="NO";
	    continue;	  
	  }
      }
      else
	{
	  //No need for catalyst; natural is sufficient
	  tc[i].R="YES 0";
	}      
    }
  for(i=0;i<T;i++)
    {
      cout<<tc[i].R<<"\n";
    }
  return 0;
}
