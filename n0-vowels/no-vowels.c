

// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

string replace(string input);
int main(int argc, string argv[])
// Write a function to replace vowels with numbers
{
    if (argc != 2)
    {
        printf("Wrong Command-line Argument\n ");
        return 1;
    }
    string word = argv[1];

    string convert = replace(word);

    printf("%s\n", convert);
}

string replace(string input)
{
    string output = input;

    for (int i = 0; i < strlen(input); i++)
    {
        char n = tolower(input[i]);



        switch (n)
        {
            case 'a':
                output[i] = '6';
                break;

            case 'e':
                output[i] = '3';
                break;

            case 'i':
                output[i] = '1';
                break;

            case 'o':
                output[i] = '0';
                break;

            case 'y':
                output[i] = '4';
                break;

            default:
                output[i] = input[i];
                break;
        }
    }

    return output;
}

// Get practice with strings


