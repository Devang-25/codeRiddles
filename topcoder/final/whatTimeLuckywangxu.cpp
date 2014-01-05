//points : 199.65/200 -- SRM 144 DIV 2

#include <iostream>
#include <stdlib.h>
using namespace std;

class Time 
{
  
public:
  Time(void) {}
  ~Time(void) {}
  static string Time::whatTime(int seconds)
  {
    //    std::string result;
    if( seconds >= 0 && seconds < 60*60*24)
      {

	int ss = seconds % 60;
	int mm = (seconds / 60 ) % 60;
	int hh = seconds / 3600;
	string result;
	char buf[3];
	sprintf(buf, "%d",hh);
	result.append(buf);
	result.append(":");	
	sprintf(buf, "%d",mm);
	result.append(buf);
	result.append(":");	
	sprintf(buf, "%d",ss);
	result.append(buf);
	return result;
      }
    else
      {
	return "Overflowed";
      }
  }

};
