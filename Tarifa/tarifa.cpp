#include<iostream>
using namespace std;
int main(){
int x,n,p,y;
cin>>x>>n;
y=0;
for(int i=0;i<n;i++){
        cin>>p;
        y=(x-p)+y;}
cout<<x+y;
return 0;
}
