#include <sys/types.h>
#include <string.h>
#include <stdio.h>

ssize_t find_short(const char *s)
{
    int k = 0;
    int min = 999;
    int N = strlen(s) - 0;
    for(int i = 0; i <= N; i++){
        if(s[i] != ' ' && i != N){
            k++;
        }
        else if(k<min){
            min = k;
            k = 0;
        }
        else{
            k = 0;
        }
    }
    return min;
}
