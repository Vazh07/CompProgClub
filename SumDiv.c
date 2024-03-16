#include <stdio.h>

int solution(int number) {
    int sum = 0;
    for(int i = 1; i<=number; i++){
      if(i%3==0)
        sum+=3;
      if(i%5==0)
        sum+=5;
    }
    return sum;
}

int main(){

    printf("%d",solution(4));

    return 0;
}
