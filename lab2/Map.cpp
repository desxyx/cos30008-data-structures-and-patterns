#include "Map.h"

std::istream& operator >> (std::istream& aStream, Map& aObject)
{
    aStream >> aObject.key >> aObject.value;
    return aStream;
}

std::ostream& operator << (std::ostream& aStream, const Map& aObject)
{
    aStream << static_cast<char>(aObject.value);
    return aStream;
}