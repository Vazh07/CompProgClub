// Solution for problem in 18490.Tortillas_horneadas
#include <iostream>

int solve(int a, int b){
    //un gramo de maíz por cada centímetro cuadrado de la tortilla
    a+=5;
    b+=3;
    return a*b;
}

int main(){
    int solution = solve(10,7);
    std::cout<<solution<<'\n';
    return 0;
}
