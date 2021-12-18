#include<iostream>

using namespace std;

int main(){
        int x, n, p, y = 0;
        
        cin>>x>>n;
        
        for(int i = 0; i < n; i++){
                cin>>p;
                y += (x-p);
        }
        cout<<x + y;

        return 0;
}
