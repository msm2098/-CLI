#include <iostream>
using namespace std;
int main(void){

   int a,b,c,d,e;
   cin>>a;
   cin>>b;
   cin>>c;
   cin>>d;
   cin>>e;
   int ver=(a*a)+(b*b)+(c*c)+(d*d)+(e*e);
   int ver2=(ver%10);
   cout<<ver2;

    return 0;
}
