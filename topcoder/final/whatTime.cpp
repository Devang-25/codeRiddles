//points : 60.0/200 -- SRM 144 DIV 2 (10% penalty and time factor included) otherwise 65.0
#include <iostream>
#include <cstdio>
using namespace std;

class Time 
{
  
public:
  string whatTime(int seconds)
  {
    //    std::string result;
    if(0<=seconds && seconds<=86399)
      {
	char result[15];
	int h = seconds/(60*60);
	int m = (seconds/60)-(h*60);
	int s = seconds-(h*60*60)-(m*60);
	sprintf(result, "%d:%d:%d",h,m,s);
	cout << result << "\n";
	return result;
      }
  }
};


int main()
{
  int seconds;
  cin>>seconds;
    {
      Time time;  
      std::string result = time.whatTime(seconds);
      cout<<result;
    }
  return 0;
}
