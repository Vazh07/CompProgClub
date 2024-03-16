// Solution for problem in 18493.Contando_retahílas
#include <iostream>
#include <string>
#include <vector>
#include "fileReader.h"
//g++ sol.cpp -o solution -I ../../../fileReader/include -L ../../../fileReader/lib -lfileReader
//g++ sol.cpp -o solution -I ../../../fileReader/include -L ../../../fileReader/lib -l:libfileReader.a
std::string solve(int size, std::vector<std::string> words){
    const char vowels[5]={'a','e','i','o','u'};
    int max = 0;
    int mIndx = 0;
    int indx = 0;
    for(const std::string& word : words){
        int count = 0;
        for(const char c : word){
            for(const char v: vowels){
                if(c==v) count++;
            }
        }
        if(count>=max){
             max = count;
             mIndx = indx;
        }
        indx++;
    }
    return words.at(mIndx) +':'+ std::to_string(max);
}

int main(int argc, char* argv[]){
    std::vector<std::string> lines = readFromFile("../test/"+std::string(argv[1])+".tst");
    size_t size = std::stoi(lines.at(0));
    std::vector<std::string> words;
    for(size_t i =1; i<=size; i++){
        words.push_back(lines[i]);
    }
    std::string solution = solve(size,words);
    std::cout<<solution<<'\n';
    return 0;
}
