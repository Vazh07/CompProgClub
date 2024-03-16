// Solution for problem in 18502.Ventas_pulpería
#include <iostream>
#include <string>
#include <vector>
#include "fileReader.h"
//g++ sol.cpp -o solution -I ../../../FileReader/ -L ../../../FileReader/ -l:libFileReader.so
void solve(){

}

int main(int argc, char* argv[]){
    std::vector<std::string> lines = readFromFile("../test/"+std::string(argv[1])+".tst");
    //std::string solution = solve();
    //std::cout<<solution<<'\n';
    return 0;
}
