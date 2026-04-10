
// COS30008, Tutorial 3, 2026

#include "Polygon.h"
#include <iostream>
#include <fstream>
#include <cmath>

int main( int argc, char* argv[] )
{
    if ( argc < 2 )
    {
        std::cerr << "Arguments missing." << std::endl;

        std::cerr << "Usage: VectorOperations <filename>" << std::endl;
        
        return 1;
    }

    std::ifstream lInput( argv[1], std::ifstream::in );
    if ( !lInput.good() )
    {
        std::cerr << "Cannot open input file: " << argv[1] << std::endl;
        return 2;
    }

    Polygon lPolygon;
    lPolygon.readData( lInput );
    
    lInput.close();

    std::cout << "Data read:" << std::endl;
    
    for ( size_t i = 0; i < lPolygon.getNumberOfVertices(); i++ )
    {
        std::cout << "Vertex #" << i << ": " << lPolygon.getVertex( i ) << std::endl;
    }

    std::cout << "The perimeter of lPolygon is " << lPolygon.getPerimeter() << std::endl;
    std::cout << "Scale polygon by 3.2:" << std::endl;
    Polygon lScaled = lPolygon.scale( 3.2f );
    std::cout << "The perimeter of lScaled is " << lScaled.getPerimeter() << std::endl;
    float lFactor = round( lScaled.getPerimeter() * 100.0f / lPolygon.getPerimeter() ) / 100.0f;
    std::cout << "Scale factor: " << lFactor << std::endl;
    
	return 0;
}
