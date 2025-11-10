//This program checks if two words are anagrams of each other.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

bool check_anagram(char string1[20], char string2[20]);
/*
Function check_anagram checks if the two words entered are anagrams or not.
parameters:
(1) string1- First word entered by the user.
(2) string2- second word entered by the user.
returns- True if both the words are anagrams of each other. False if not anagram.
*/

bool check_anagram(char string1[20], char string2[20]){
    bool is_anagram;
    int i,j;
    char string_1[20], string_2[20];

    int x = strlen(string1);
    int y = strlen(string2);

    for (i = 0; string1[i] != '\0'; ++i) {
    string_1[i] = toupper(string1[i]);
    }
    string_1[i] = '\0';

    for (i = 0; string2[i] !='\0'; ++i) {
    string_2[i] = toupper(string2[i]);
    }
    string_2[i] = '\0';
    
        for (i=0; i<x; ++i){
            is_anagram = false;
            for (j=0 ; j<y ; ++j){
                    if (string_1[i] == string_2[j]){
                        is_anagram = true;
                        string_2[j]= '0';
                        break;
                    }
            }
            if (!is_anagram){
                return false;
            }
        }
    
   return true; 
}


int main(){
    char string1[21];
    char string2[21];
    

    printf("Please enter the first word: ");
    scanf("%20s", string1);
    //printf("\n");

    printf("Please enter the second word: ");
    scanf("%20s", string2);
    //printf("\n");


    int x = strlen(string1);
    int y = strlen(string2);
    
  
if (x == y){
    if (check_anagram(string1, string2)){
        printf("%s is an anagram of %s\n", string1, string2);
    }
    else {
        printf("%s is NOT an anagram of %s\n", string1, string2);
    }
}
else {printf("%s is NOT an anagram of %s\n", string1, string2);}
    

return 0;
}