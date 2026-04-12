
// COS30008, Problem Set 1, 2026

#include "Matrix3x3.h"

#include <cassert>

bool Matrix3x3::operator==( const Matrix3x3& aOther ) const noexcept
{
    const Matrix3x3& M = *this;

    return M[0] == aOther[0] && M[1] == aOther[1] && M[2] == aOther[2];
}

Matrix3x3 Matrix3x3::operator*( const Matrix3x3& aOther ) const noexcept
{
    const Matrix3x3& M = *this;

    Vector3D c0 = aOther.column(0);
    Vector3D c1 = aOther.column(1);
    Vector3D c2 = aOther.column(2);

    return Matrix3x3(
        Vector3D( M[0].dot(c0), M[0].dot(c1), M[0].dot(c2) ),
        Vector3D( M[1].dot(c0), M[1].dot(c1), M[1].dot(c2) ),
        Vector3D( M[2].dot(c0), M[2].dot(c1), M[2].dot(c2) )
    );
}

Matrix3x3 Matrix3x3::transpose() const noexcept
{
    return Matrix3x3( column(0), column(1), column(2) );
}

float Matrix3x3::det() const noexcept
{
    const Matrix3x3& M = *this;

    return M[0][0] * ( M[1][1] * M[2][2] - M[1][2] * M[2][1] )
         - M[0][1] * ( M[1][0] * M[2][2] - M[1][2] * M[2][0] )
         + M[0][2] * ( M[1][0] * M[2][1] - M[1][1] * M[2][0] );
}

bool Matrix3x3::hasInverse() const noexcept
{
    return det() != 0.0f;
}

Matrix3x3 Matrix3x3::inverse() const noexcept
{
    assert( hasInverse() );

    const Matrix3x3& M = *this;

    float d = 1.0f / det();

    return Matrix3x3(
        Vector3D( M[1][1]*M[2][2] - M[1][2]*M[2][1],  M[0][2]*M[2][1] - M[0][1]*M[2][2],  M[0][1]*M[1][2] - M[0][2]*M[1][1] ),
        Vector3D( M[1][2]*M[2][0] - M[1][0]*M[2][2],  M[0][0]*M[2][2] - M[0][2]*M[2][0],  M[0][2]*M[1][0] - M[0][0]*M[1][2] ),
        Vector3D( M[1][0]*M[2][1] - M[1][1]*M[2][0],  M[0][1]*M[2][0] - M[0][0]*M[2][1],  M[0][0]*M[1][1] - M[0][1]*M[1][0] )
    ) * d;
}

std::ostream& operator<<( std::ostream& aOStream, const Matrix3x3& aMatrix )
{
    return aOStream << "[" << aMatrix[0].toString() << ","
                           << aMatrix[1].toString() << ","
                           << aMatrix[2].toString() << "]";
}
