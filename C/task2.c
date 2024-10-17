// ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

// If the function is passed a valid PIN string, return true, else return false.


#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

bool validate_pin(const char *pin) {
    if((strlen(pin) == 6) || (strlen(pin) == 4)){
        for(int i = 0; i < strlen(pin); i++){
            if(isdigit(pin[i]) == 0)
                return false;
        }
        return true;
    }
    return false;
}

int main(){
    printf("%s\n", validate_pin("123") ? "true" : "false");
    printf("%s\n", validate_pin("1234") ? "true" : "false");
    printf("%s\n", validate_pin("12345") ? "true" : "false");
    printf("%s\n", validate_pin("123456") ? "true" : "false");
    printf("%s\n", validate_pin("123a") ? "true" : "false");
    printf("%s\n", validate_pin("123a45") ? "true" : "false");
}