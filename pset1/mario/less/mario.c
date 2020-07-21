#include <stdio.h>
#include <cs50.h>

int main()
{
    int h;
    do
    {
       h = get_int("Please enter height:");
    }
    while (h < 1 || h > 8);
    
   for (int i = 0; i < h; i++) //i is rows
   {
       for(int j = i; j < h-1; j++) //j is space          
        {
        printf(" ");
        }
    for (int k = 0; k <= i; k++) //k is #           
    {
     printf("#");
    }

    printf("\n");
   }

}
