// Solution for problem in 18502.Ventas_pulpería
#include <iostream>
#include <string>
#include <vector>
#include "fileReader.h"
//g++ sol.cpp -o solution -I ../../../FileReader/ -L ../../../FileReader/ -l:libFileReader.a
//g++ sol.cpp -o solution -I ../../../fileReader/include -L ../../../fileReader/lib -l:libfileReader.a
int solve(std::vector<int> prc, std::vector<int> qty, int g){
    int r=0;
    for(const int p : prc){
        for(const int q: qty){
            if(p*q>=g){
                r+=p*q;
            }
        }
    }
    return 0;
}

int main(int argc, char* argv[]){
    std::vector<std::string> lines = readFromFile("../test/"+std::string(argv[1])+".tst");
    std::vector<int> prc;
    std::vector<int> qty;
    //int vals[3] = {0};
    const std::string& qVals = lines[0];
    std::vector<std::string> vals = splitString(qVals, ' ');
    for (const std::string qVal : vals){
        std::cout<<qVal<<std::endl;
    }
    //int solution = solve(prc,qty,vals[2]);
    //std::cout<<solution<<'\n';
    return 0;
}
