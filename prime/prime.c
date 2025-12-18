#include <cs50.h>
#include <stdio.h>

bool prime(int number);

int main(void)
{
    int min;
    do
    {
        min = get_int("Minimum: ");
    }
    while (min < 1);
    // int main is = get_int
    int max;
    do
    {
        max = get_int("Maximum: ");
    }
    while (min >= max);
    // int max is equal to the max number
    for (int i = min; i <= max; i++)
    {
        if (prime(i))
        {
            printf("%i\n", i);
        }
    }
}

bool prime(int number)
{
    // reprsent if prime is == to 1 or 100
    if (number <= 1)
    {
        return false;
    }
    // return false is not true

    if (number == 2 || number == 3)
    {
        return true;
    }
    // find primes, for loop
    for (int i = 2; i < number; i++)
    {
        if (number % i == 0)
        {
            return false;
        }
    }

    // print return true if not false
    return true;

}
