#include<iostream>

using namespace std;

int main(){
    int K, Q, R, B, Kn, P;

    cin>>K>>Q>>R>>B>>Kn>>P;

    K=1-K;
    Q=1-Q;
    R=2-R;
    B=2-B;
    Kn=2-Kn;
    P=8-P;
    cout<<K<<" "<<Q<<" "<<R<<" "<<B<<" "<<Kn<<" "<<P;

    return 0;
}
