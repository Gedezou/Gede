#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size

    int n;

    do
    {
        n = get_int("start size: ");

    }
    while (n < 9);

    //printf("The Number is %i\n", n);

    // TODO: Prompt for end size
    int i;
    do
    {
        i = get_int("End size: ");
    }
    while (i < n);


    // TODO: Calculate number of years until we reach threshold

    //int number_years
    int number_years = 0;
    while (n < i)
    {
        n = n + (n / 3) - (n / 4);
        number_years ++;
    }


    printf("Years: %i\n", number_years);
    // TODO: Print number of years
    //printf("The Number is %i\n", n);
}