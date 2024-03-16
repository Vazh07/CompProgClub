#include <iostream>

int main(){
    std::string names="";
    std::string naming="";
    std::cin>>names;
    for(int i = 0; i<names.length(); i++){
        if(i==0) naming+=names[i];
        else if(names[i]=='-') naming+=names[i+1];
    }
    std::cout<<naming;
}
