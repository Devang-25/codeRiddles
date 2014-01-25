#include<iostream>
#include<cstdlib>

using namespace std;

class Tcase{
public:
  int N,K,M;
public:
  int atoms(int N, int K, int M)
  {
    if(N<=M)
      {
	int t = 0;
	while(N<=M){
	  t++;
	  N = N*K;
	}
	return t-1;
      } 
    return 0;
  }
};
int main() {  
  int i,P;
  cin>>P;
  if((1<=P) && (P<=10^4)){
    Tcase tc[P];  
    int A[P];
    for(i=0;i<P;i++)
      {
	cin >> tc[i].N >> tc[i].K >> tc[i].M;
	A[i] = tc[i].atoms(tc[i].N, tc[i].K, tc[i].M);
      } 
    for(i=0;i<P;i++)
      {
	cout << A[i]<<"\n";
      }
  }
  return 0;
}
