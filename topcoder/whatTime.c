#include<stdio.h>
//using namespace std;
int main()
{ 
  int tm;
  int h=0,m=0,s=0;
  char fin;

  printf("\ntime in sec: ");
  scanf("%d",&tm);
  //  tm = 34440;
  h = tm/(60*60);
  m = (tm/60)-(h*60);
  s = tm-(h*60*60)-(m*60);
  
  /*
  printf("\nh = %d\n",h);
  printf("\nm = %d\n",m);
  printf("\ns = %d\n",s);
  */

  printf("\n%d:%d:%d\n\n",h,m,s);
  return 0;
}
