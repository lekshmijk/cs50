#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main()

{
    string name = get_string("What is your name?\n");

    printf("Hello,%s\n",name);

}
