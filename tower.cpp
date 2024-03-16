#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> towerBuilder(unsigned nFloors) {
    std::vector<std::string>ts;
    std::vector<int>p;
    char t = '*';
    char s = ' ';
    int fn = 1, r=0;
    p.push_back(1);
    for(int i=0; i<nFloors-1; i++){
        fn+=2;
        p.push_back(fn);
    }
    for(const int n1: p){
        r=static_cast<int>(fn-n1)/2;
        std::string s1 = "";
        for(int j1=0;j1<r;j1++){
            s1+=s;
        }
        for(int j2=0;j2<n1;j2++){
            s1+=t;
        }
        for(int j3=0;j3<r;j3++){
            s1+=s;
        }
        ts.push_back(s1);
    }
    return ts;
}

int main(){
    std::vector<std::string>t = towerBuilder(6);
    for (const std::string& str : t) {
        std::cout << str << std::endl;
    }
}
