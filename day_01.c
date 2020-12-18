#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>

int to_number(char* num_str, int* num)
{
    int result = 0;
    size_t size = strlen(num_str);
    
    for (int i = 0; i < size; i++)
    {
        int number = num_str[i] - '0';
        if (number >= 0 && number <= 9)
            result += (int) (pow(10, (double) (size - (i + 1)))) * number;
        else
            return 0;
    }
    *num = result;

    return 1;
}

/**
 * This function took me days to debug and it finally works...
 * I hate the fact that I implemented this in Haskell within less than an hour...
 * As i'm writing this I also realised that sscanf existed F
 */ 
void read_numbers_from_file(char* path, int** result, int* numbers_sz)
{
    FILE* fp = fopen(path, "r");    // unsafe
    assert(fp);

    int* numbers = (int*) calloc(0, sizeof(int));
    assert(*numbers);

    // Temp buffer that will be used 
    char* temp_str = (char*) calloc(1, sizeof(char));  // start with 1 for null-teminator '\0'
    assert(temp_str);

    int temp_strsz, count, c;
    *numbers_sz = 0;
    temp_strsz = count = c = 0;

    // For each line put each character into a string, when \n or EOF is encountered convert the resulting string into a number
    // then put that number into the array
    while ((c = fgetc(fp))) 
    {
        if (c == '\n' || c == EOF)
        {
            // This is for when the file is empty
            if (count == 0)
                break;

            // Terminate the string
            temp_str[temp_strsz+1] = '\0';
            // Increase the size of the array of numbers by 1
            *numbers_sz += 1;
            numbers = (int*) realloc(numbers, *numbers_sz * sizeof(int));
            assert(numbers);
            
            // Convert the string from this line into a number
            to_number(temp_str, &numbers[*numbers_sz-1]);
            
            // Reset for the next line
            temp_str = (char*) calloc(1, sizeof(char));  // start with 1 for null-teminator '\0'
            assert(temp_str);
            temp_strsz = count = 0;
        }
        else
        {
            // Has the number of characters read exceeded the size of the string?
            if (count++ > temp_strsz)
            {
                // Resize it
                temp_str = (char*) realloc(temp_str, (++temp_strsz + 1) * sizeof(char));
                assert(temp_str);
            }
            temp_str[temp_strsz] = c;
        }
    }

    free(temp_str);
    temp_str = 0;
    *result = numbers;
    fclose(fp);
}

int main()
{
    int sum = 0;
    int* nums = 0;
    int size = 0;
    long long product = 0;

    read_numbers_from_file("day_01.txt", &nums, &size);
    assert(nums);

    for (int x = 0; x < size; x++)
    {
        for (int y = 0; y < size; y++)
        {
            for (int z = 0; z < size; z++)
            {
                if (x == y || y == z || x == z)
                    continue;
                
                sum = nums[x] + nums[y] + nums[z];
                product = nums[x] * nums[y] * nums[z];
                if (sum == 2020)
                {
                    printf("%i %i %i\n", nums[x], nums[y], nums[z]);
                    printf("%lld\n", product);
                    break;
                }
            }
            if (sum == 2020)
                break;
        }
        if (sum == 2020)
            break;
    }

    return 0;
}