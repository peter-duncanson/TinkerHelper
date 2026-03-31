#include <stdio.h>
#include <string.h>
#include <stdbool.h>

const char *fileName = "info.txt";

int main(int argc, char *argv[])
{
    char *component = argv[1];
    char *codeType  = argv[2];
    char *command   = argv[3];

    FILE *referenceFile = fopen(fileName, "r");

    if (referenceFile == NULL)
    {
        printf("Could not find a text file to reference for information!\n");
        return 1;
    }
    if(!(strcmp(argv[1], "r") || strcmp(argv[1], "R")))
    {
        
    }
    char lineBuffer[64];

    while(fgets(lineBuffer, sizeof(lineBuffer), referenceFile))
    {
    }
    

    

    fclose(fileName);
    return 0;
}


