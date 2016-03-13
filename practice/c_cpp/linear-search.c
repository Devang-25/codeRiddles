#include<stdio.h>
void main(){
int i,data[10],n,item;
int loc;
for(i=1;i<=10;i++){
scanf("%d",&data[i]);
}
printf("enter the num you have to search");
scanf("%d",&item);
for(i=1;i<=10;i++){
if(data[i]==item){
loc=i;
printf("%d",loc);
}
}
}
