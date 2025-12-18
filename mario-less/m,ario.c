#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("size: ");
    }
    while (n < 1 || n > 8);

    for (int i = 0; i < n; i++)
    {
        // prints spaces with the input but - 1 so not to create an extra space
        for (int j = n - 1; j > i; j--)
        {
            printf(" ");
        }
        // prints hashes
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }

        printf("\n");
    }
}