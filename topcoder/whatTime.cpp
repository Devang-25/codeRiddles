#include <iostream>
#include <cstdio>

//#include <boost/lexical_cast>

using namespace std;

class Time 
{
  
public:
  int tm;
  string whatTime() {
    std::string result;
    char numstr[20];
    //    std::string sp = ":";
    int h = tm/(60*60);
    int m = (tm/60)-(h*60);
    int s = tm-(h*60*60)-(m*60);
    //cout<<"\nh = "<<h<<" m = "<<m<<" s = "<<s<<"\n";
    //result = boost::lexical_cast<std::string>(h) + sp + boost::lexical_cast<std::string>(m) + sp + boost::lexical_cast<std::string>(s);
    
    sprintf(numstr, "%d:%d:%d",h,m,s);
    //:%d:%d", h,m,s);
    //result = numstr + sp;
    //result = numstr + "\n";
    return numstr;
  }
};

int main()
{
  int tm1;
  cin>>tm1;
  if(0<=tm1 && tm1<=86399)
    {
      Time t1;  
      t1.tm = tm1;
      std::string res = t1.whatTime();
      //char res = t1.whatTime();
      cout<<res;
      return 0;      
    }
  
  //  else 
  // { exit(0); }
}

/*
class Box
{
   public:
   double breadth;        // Breadth of a box
   
   // Member functions declaration
   double getVolume(void);
   void setBreadth( double bre );

};

// Member functions definitions
double Box::getVolume(void)
{
    return length * breadth * height;
}

void Box::setBreadth( double bre )
{
    breadth = bre;
}

*/
