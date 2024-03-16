#include <iostream>
#include <string>
#include <algorithm>

int checkDigt(std::string& a, std::string& b){
    int n1=a.length(), n2=b.length(), s=0, r;
    if(n1==n2){
        for(int i = 0; i < n1; i++)
        if (a[i] < b[i])
            return 0;
        else if (a[i] > b[i])
            return 1;
    }
    if(n1>n2){
        r = 1;
        s = n1-n2;
    }
    else{
        r = 0;
        s = n2-n1;
    }
    std::string e = "";
    for(int i=0; i<s; i++){
            e+="0";
    }
    if(r)
        b = e+b;
    if(!r)
        a = e+a;
    return r;
}

std::string subtract(std::string a, std::string b){
    int n1=a.length(), n2=b.length(), brrw=0;
    std::string sum="";
    for(int i = n1-1; i >= 0; i--){
        //std::cout<<a[i]<<'-'<<b[i]<<'=';
        if(brrw){
            a[i]--;
            brrw--;
        }
        if(a[i]<b[i]){
            brrw++;
            sum+=std::to_string((a[i]+10-b[i]));
            //std::cout<<(a[i]+10-b[i]);
        }else{
            sum+=std::to_string((a[i]-b[i]));
            //std::cout<<(a[i]-b[i]);
        }
        //std::cout<<'\n';
    }
    std::reverse(sum.begin(), sum.end());
    return sum;
}

int main(){
    std::string a,b;
    while(std::cin>>a>>b){
        if(checkDigt(a,b)){
            std::cout<<subtract(a,b)<<'\n';
        }else{
            std::cout<<subtract(b,a)<<'\n';
        }
    }
    return 0;
}
