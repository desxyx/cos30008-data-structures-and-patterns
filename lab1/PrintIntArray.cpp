#include <iostream>
#include <cstddef>

void printIntArray(int aArray[], size_t aSize)
{
    std::cout << '[';

    for (size_t i = 0; i < aSize; i++ )
    {
        std::cout << aArray[i];
        if (i + 1 < aSize)
        {
            std::cout << ',';
        }
    }
    std::cout << ']' << std::endl;
}