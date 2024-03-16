#include <iostream>
const int MAX_SIZE = 50;

int isSymetric(int s, int (*m)[MAX_SIZE]){
    int trs[s*s] = {0};
    int mlt = 0;
    for (int i = 0; i < s; i++) {
        for (int j = 0; j < s; j++) {
            if(m[i][j] == m[j][i]){
                trs[mlt+i+j] = 1;
            }
        }
        mlt++;
    }
    int s_counter = 0;
    for(int i = 0; i<s*s; i++){
       if(trs[i]) s_counter++;
    }
    if(s*s == s_counter) return 1; return 0;
}

void solve(int s, int (*m)[MAX_SIZE]){
    std::cout<<isSymetric(s, m);
}

int main() {
    int s;
    std::cin >> s;
    int mtrx[MAX_SIZE][MAX_SIZE] = {0};
    for (int i = 0; i < s; i++) {
        for (int j = 0; j < s; j++) {
            std::cin >> mtrx[i][j];
        }
    }
    /*std::cout << "Matrix entered:" << std::endl;
    for (int i = 0; i < s; i++) {
        for (int j = 0; j < s; j++) {
            std::cout << mtrx[i][j] << " ";
        }
        std::cout << std::endl;
    }*/
    solve(s, &mtrx[0]);
    return 0;
}
