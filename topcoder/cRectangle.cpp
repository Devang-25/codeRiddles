// classes example
#include <iostream>
#include <cstdio>

using namespace std;


class CRectangle {
  int x, y;
public:
  void set_values (int,int);
  int area () {return (x*y);}
};

void CRectangle::set_values (int a, int b) {
  x = a;
  y = b;
}

int main () {
  CRectangle rect;
  rect.set_values (3,4);
  cout << "area: " << rect.area();
  
  std::string name = "arcolife"; int age = 21; std::string result; 
  char numstr[21]; // enough to hold all numbers up to 64-bits
  sprintf(numstr, "%d", age);
  result = name + numstr;
  cout<<"\n"<<result;
  return 0;

}
