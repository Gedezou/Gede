#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("USAGE: ./recover JPEG\n");
        return 1;
    }



// open new file under the name stored at filename
    FILE *new_file = fopen(argv[1], "r");

    if (new_file == NULL)
    {
        printf("Could Not Find File.\n");
        return 2;
    }

    unsigned char buffer[512];

    int count_image = 0;
    FILE *output_file = NULL;

    // char filename

    // create a new block of memory to store
    char *filename = malloc(8 * sizeof(char));

    // read the blocks of 512 bytes
    while (fread(buffer, sizeof(char), 512, new_file))
        // check iif byte indicatestart of JPEG
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)

        {
            if (output_file != NULL)
            {
                fclose(output_file);
            }

            sprintf(filename, "%03i.jpg", count_image);
            // open output filename
            output_file = fopen(filename, "w");
            //count number of images found
            count_image++;

        }
        // check if input is used for valid input
        if (output_file != NULL)
        {
            fwrite(buffer, sizeof(char), 512, output_file);
        }
    }


    free(filename);
    fclose(new_file);
    fclose(output_file);
    // fclose(filename);
    return 0;

}


//     // Open file
//     char filename = *argv[1];
//     File *file = fopen(, "r" );

//     // Check if file exists
//     if (file == NULL)
//     {
//         printf("No Such File Found.\n");
//         return 1;
//     }
//     uint8_t buffer[4];
//     uint8_t signature[] = {512};

//     fread(buffer, 1, 512, file);
//      fclose(file);

//     // Does the buffer signature match?
//     for (int i = 0; i < 512; i++)
//     {
//         if (buffer[i] != signature[i])
//         {
//             printf("Likely Not A PDF.\n");
//             return 0;
//         }
//     }
//     printf("Likely A PDF.\n");
//     fclose(file);
//     return 0;

// }