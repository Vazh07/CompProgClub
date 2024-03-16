#include <stddef.h>
#include <stdio.h>

void move_zeros(size_t len, int arr[len])
{
    int acpy[len];
    int j = 0;
    for(int i=0; i<len; i++){
      if(arr[i]){
        acpy[j++]=arr[i];
      }
    }
    for(int i=0; i<len; i++){
        if(i>=j) acpy[i]=0;
        arr[i] = acpy[i];
    }
}


int main(){
    int a[] = {1, 2, 0, 1, 0, 1, 0, 3, 0, 1};
    move_zeros(10,a);
}
