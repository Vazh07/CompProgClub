#include <iostream>

int main(){
    int n =0, k=0;
    int arr[n][n];
    int currN = 0;
    int j = 0;
    std::cin>>n>>k;
    for(int i =0; i<k; i++){
        while(std::cin>>currN){
            arr[i][j] = currN;
            j++;
        }
    }
}
