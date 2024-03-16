#include <iostream>

int main(){
    int x=0,y=0,n=0;
    std::cin>>x>>y>>n;
    std::string fb = "";
    for(int i = 1; i<n+1; i++){
        fb = "";
        if(i%x==0) fb="Fizz";
        if(i%y==0) fb+="Buzz";
        if(fb.length()) std::cout<<fb<<'\n';
        else std::cout<<i<<'\n';
    }
}
