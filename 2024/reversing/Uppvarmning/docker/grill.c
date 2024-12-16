#include <stdlib.h>
#include <stdio.h>
#include <string.h>


char * Solution;
char * flag;
char seenSolutions[10][34];
int wonRounds = 1;
void getFlag() {
    flag = malloc(70);
    strcpy(flag, "cratectf{GrillenGl0mdeUseAfterZ33}");
    printf("Här skulle det ha funnits en flagga, men jag var så upptagen med att grilla att jag glömde hur man använder formatsträngar :(\n");
}

void newSolution(int * inpKnobs, char * userInput) {
    char * newSolution = malloc(150);
    char * appendege = malloc(5);
    char * newAllSolution;
   // fgets(newSolution, 10, stdin);
    
    sprintf(newSolution, "%d: ", wonRounds);

    for (int i = 0; i < 32; i++) {
            if (inpKnobs[i] == 1) {
                sprintf(appendege, "%d,", i + 1);
                strcat(newSolution, appendege);
            }
    }
    free(appendege);
    strcat(newSolution, "\n");
    
    if (Solution != 0) {
        newAllSolution = (char *) malloc(strlen(Solution) + strlen(newSolution) + 1);
        strcpy(newAllSolution, Solution);
        strcat(newAllSolution, newSolution);
        free(newSolution);
        free(Solution);
        Solution = newAllSolution;
    } else {
        Solution = (char *) malloc(strlen(newSolution) + 1);
        strcpy(Solution, newSolution);
        free(newSolution);
    }
    strcpy(seenSolutions[wonRounds], userInput);
    wonRounds += 1;
}

void printSolution() {
    if (Solution == 0) {
        printf("Inga lösningar!");
        return;
    }
    printf("Lösningshistorik (knoppar som blev påslagna): \n%s\n", Solution);
}
void knobsAndDials() {
    char * userInput = (char *)malloc(34);
    int input[32];  
    char * shouldLeaveSolution = (char *)malloc(3);
    printf("\nNy dag, nya möjligheter!\nVilka knoppar vill du aktivera? [010111000...] ");
    fgets(userInput, 34, stdin);
    for (int i = 0; i < wonRounds; i++) {
        if (strcmp(userInput, seenSolutions[i]) == 0) {
            printf("Tråkigt, jag har redan sett den kombinationen av knoppar...\n");
            exit(0);
        }
    }
    int valid = 1;
    for (int i = 0; i < 33 - 1; i++) {
            if(memcmp((void * )&userInput[i], (void * ) "0", 1) == 0 || memcmp((void * )&userInput[i], (void * ) "1", 1) == 0) {
                
            }
            else {
                valid = 0;
            }
    }
    if (strlen(userInput) != 33) valid = 0;
    if (valid){
        //printf("%s", userInput);
        for (int i = 0; i < 33 - 1; i++) {
            input[i] = userInput[i] - 0x30;
            //printf("%d", input[i]);
        }
        
        if (((((input[10] ^ input[17]) ^ (input[22] & input[18])) & ((input[19] ^ (input[23] ^ input[19])) ^ (input[8] | input[20]))) == 0) && ((((input[29] ^ input[4]) ^ input[4]) | (input[12] | input[26])) == 0) && (((input[10] & (input[28] & (input[15] | input[4]))) | input[28]) == 0) && ((((input[13] & input[16]) & input[13]) & input[20]) == 0) && (((input[3] | (input[27] | input[9])) | ((input[6] & input[14]) ^ (input[1] | input[26]))) == 0) && (((input[13] ^ (input[2] & (input[8] | input[20]))) & (input[11] & input[9])) == 0) && (((input[15] | input[4]) | ((input[5] | input[17]) | ((input[6] & input[14]) ^ (input[1] | input[26])))) == 0) && ((((input[30] & input[2]) ^ input[1]) | input[15]) == 0) && ((input[7] & (input[24] | input[31])) == 0) && ((((input[15] | input[4]) | input[30]) & (input[6] & input[14])) == 0) && ((input[29] ^ (input[16] | (input[5] | input[17]))) == 0) && ((input[0] | ((input[10] & (input[28] & (input[15] | input[4]))) | input[27])) == 0) && (((((input[29] ^ input[4]) ^ input[4]) ^ (input[10] ^ input[17])) | ((input[10] | input[14]) & input[30])) == 0) && (((input[28] & (input[15] | input[4])) & (input[3] | input[6])) == 0) && ((input[19] ^ (input[8] | input[22])) == 0) && ((((input[2] & (input[8] | input[20])) & (input[24] | input[5])) ^ input[18]) == 0) && ((((input[30] & input[2]) | (input[27] | input[9])) & input[22]) == 0) && (((input[21] | input[28]) & (((input[13] & input[16]) & input[13]) | input[25])) == 0) && (((input[31] | input[19]) ^ (input[21] | (input[21] | input[28]))) == 0) && ((((input[24] | input[31]) & (input[28] & (input[15] | input[4]))) ^ ((input[3] | (input[27] | input[9])) ^ (input[15] ^ (input[29] & input[7])))) == 0) && ((((input[11] & input[1]) | input[0]) ^ (input[27] | input[9])) == 0) && (((((input[8] | input[22]) & input[21]) ^ ((input[31] | input[19]) | input[6])) ^ (input[11] | ((input[15] | input[4]) | input[30]))) == 0) && (((input[14] | input[6]) & (input[18] ^ input[19])) == 0) && (((((input[12] | input[26]) ^ input[18]) & (input[11] & input[1])) & ((input[22] & input[18]) | input[3])) == 0) && (((input[11] & ((input[22] & input[18]) | input[15])) ^ (input[27] ^ (input[24] | input[31]))) == 0) && ((((input[23] | input[7]) | input[13]) & (input[1] | input[26])) == 0) && (((input[16] & input[21]) | ((input[21] | input[28]) | input[23])) == 0) && ((input[4] & input[24]) == 0) && ((input[26] & ((input[10] | input[14]) ^ (input[31] & input[28]))) == 0) && ((((input[16] | (input[5] | input[17])) & (input[21] | (input[21] | input[28]))) ^ ((input[0] ^ input[25]) ^ input[31])) == 0) && ((((input[12] | input[26]) | (input[23] ^ input[19])) ^ ((input[13] & input[16]) | (((input[13] & input[16]) & input[13]) | input[25]))) == 0) && ((((input[8] | input[22]) & input[21]) & (((input[0] ^ input[25]) & input[3]) ^ input[26])) == 0)) {
            printf("Köttet blev perfekt, spara lösning för framtida bruk? [y/n]");
            fgets(shouldLeaveSolution, 3, stdin);
            if (strcmp(shouldLeaveSolution, "y\n") == 0) {
                newSolution(input, userInput);
            }
            getFlag();
            
            if (wonRounds == 10) {
                printf("Nu tror jag att det var färdiggrillat...");
		exit(0);
            }
        } else {
            printf("Köttet brändes för grillen blev för varm...\n");
            if (Solution != 0){
                free(Solution);
            }

        }
    } else {
        printf("Strängen ska vara 32 lång och endast innehålla 1 och 0.\n");
    }

    
    free(userInput);
    free(shouldLeaveSolution);
}
void welcome(){
    printf("                       _ _ _ _ _\n");
    printf("         _______________|_____|_________________\n");
    printf("        /                                       \\\n");
    printf("       / _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \\\n");
    printf("      |                                           |\n");
    printf("      |                                           |\n");
    printf("      | _________________________________________ |\n");
    printf("        /#######################################\\\n");
    printf("       /#########################################\\\n");
    printf("      /___________________________________________\\\n");
    printf("      |      * * * * * * * * * * * * * * * *      |\n");
    printf("      |      * * * * * * * * * * * * * * * *      |\n");
    printf("      |___________________________________________|\n");
    printf("              | |  ||                || | |\n");
    printf("              | |  @@                @@ | |\n");
    printf("              | |                       | |\n");
    printf("              @@@                       @@@\n");
    printf("    (               )     (  (      )        (        (  (  \n" );
    printf("    )\\ `  )  `  )  /((  _ )\\ )(    (     (   )\\  (    )\\))( \n" );
    printf(" _ ((_)/(/(  /(/( (_))\\(_((_|()\\   )\\  ' )\\ |(_) )\\ )((_))\\ \n" );
    printf("| | | ((_)_\\((_)_\\_)((_) _` |((_)_((_)) _(_/((_)_(_/( (()(_)\n" );
    printf("| |_| | '_ \\) '_ \\) V /\\__,_| '_| '  \\() ' \\)) | ' \\)) _` | \n" );
    printf(" \\___/| .__/| .__/ \\_/      |_| |_|_|_||_||_||_|_||_|\\__, | \n");
    printf("      |_|   |_|                                      |___/  \n\n");

    printf("Hjälp mig att grilla den perfekta köttbiten.\n");
}
int main(int argc, char ** argv) {
    char * choice =  (char *) malloc(3);
    setvbuf(stdout, NULL, _IONBF, 1024);
    welcome();
    while (1) {
        knobsAndDials();
        printf("Skriv ut sparade lösningar? [y/n]");
        fgets(choice, 3, stdin);
        if (strcmp(choice, "y\n") == 0) {
            printSolution();
            exit(0);
        }
        if (flag != 0) {
            free(flag);
            flag = 0;
        }
    }
    return 0;
}
