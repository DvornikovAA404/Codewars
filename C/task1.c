#include <stdio.h>

int solution(int number) {
    int sum = 0;
    for (int i = 0; i < number; i++){
            if(i%3==0 || i%5==0){
                sum += i;
            }
        }
    return sum;
}

int main(){
    printf("%d\n", solution(10));
}