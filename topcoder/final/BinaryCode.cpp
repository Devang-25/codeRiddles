//http://stackoverflow.com/questions/9354192/reading-a-list-of-integer-in-a-single-input-line-in-c

// SRM 144 DIV 2 550

#include<iostream>
#include <cstdio>
#include<stdlib.h>

using namespace std;

class BinaryCode
{
public:
  string decode(string message)
  {
    //std::string result;
    len = strlen(message);
    //char result[len];

    //sprintf(result, "%d:%d:%d",h,m,s);

    // cout << result << "\n";
    return len;

  }
};

int main()
{

  std::string ip;
  //ip = getline();
  cin << ip;
  BinaryCode bc;
  std::string len = bc.decode(ip);
  cout << "length of input string "<<len;
  return 0;
}
