#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>


int main(void)
{
    string  text = get_string("Text: ");
    // string  text = (islower) && (isalpha) == 97; //to 122;
    int letters = 0;
    int words = 1;
    int sentences = 0;
//string count_letters = Text;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letters ++;
        }
//count_words(string[text])
        else if (text[i] == ' ')
        {
            words++;
        }
//count_sentences(string Text);
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences ++;
        }

    }

    //printf("letters %i\n", letters);
    // printf("words %i\n", words);
    // printf("sentences %i\n", sentences);




    float L = letters / (float) words * 100;
    // printf("L %f\n", L);

    float S = sentences / (float) words * 100;
    // printf("S %f\n", S);

    int index = round(0.0588 * L - 0.296 * S - 15.8);
    //printf("Grade Level %d\n", index);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }

}



