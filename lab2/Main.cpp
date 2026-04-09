#include <iostream>
#include <fstream>
#include <string>
#include "Map.h"


void readData(std::istream& aInstream, Map aArray[], int aSize)
{
    for ( int i = 0; i < aSize; i++)
    {
        aInstream >> aArray[i];
    }
}


void performInsertionSortKeyValuePairs(Map aArray[], int aSize)
{

    for (int i = 1; i < aSize; i++)
    {

        Map lElem = aArray[i];

        int j = i - 1;
        while (j >= 0 && lElem.key < aArray[j].key)
        {
            aArray[j + 1] = aArray[j];
            j -= 1;
        }
        aArray[j + 1] = lElem;
    }
}


void printValues(Map aArray[], int aSize)
{
    for( int i = 0; i < aSize; i ++)
    {
        std::cout << aArray[i];
    }
    std::cout << std::endl;
}


int main(int argc, char* argv[])
{

    if (argc !=2)
    {

        std::cerr << "Illegal command invocation." << std::endl;
        std::cerr << "Usage: Records Data.txt" << std::endl;

        return 1;
    }

    std::ifstream lInput(argv[1]);


    if ( !lInput.good())
    {
        std::cerr << "Error opening" << argv[1] <<std::endl;
        return 2;
    }


    int lSize = 0;
    lInput >> lSize;

    std::cout << "Number of entries: " << lSize << std::endl;

    Map* lArray = new Map[lSize];

    readData(lInput, lArray, lSize);
    performInsertionSortKeyValuePairs(lArray, lSize);
    printValues(lArray, lSize);
    delete[] lArray;
    return 0;

}
