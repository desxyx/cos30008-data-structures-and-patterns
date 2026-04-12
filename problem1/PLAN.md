# Problem Set 1 — Execution Plan

## What needs to be delivered

Two new source files (DO NOT touch any existing file):

| File to create | What it implements |
|---|---|
| `Vector3D_PS1.cpp` | `operator==` and `toString()` for Vector3D |
| `Matrix3x3_PS1.cpp` | `operator==`, `operator*` (matrix×matrix), `transpose()`, `det()`, `hasInverse()`, `inverse()`, `operator<<` for Matrix3x3 |

## Files that must NOT be modified

`Vector2D.h`, `Vector2D.cpp`, `Vector3D.h`, `Vector3D.cpp`,
`Matrix3x3.h`, `Matrix3x3.cpp`, `Main.cpp`

To activate tests: uncomment `#define P1` and `#define P2` in `Main.cpp`
(but that file is not ours to edit — Des will do this or confirm separately)

---

## Vector3D_PS1.cpp

**Include:** `Vector3D.h`, `<cmath>`, `<sstream>`

### `bool Vector3D::operator==( const Vector3D& aOther ) const noexcept`

Compare all three components using epsilon:

```
std::abs( x() - aOther.x() ) < eps
&& std::abs( y() - aOther.y() ) < eps
&& std::abs( w() - aOther.w() ) < eps
```

`eps` is already declared in `Vector3D.h` as `std::numeric_limits<float>::epsilon()`.

### `std::string Vector3D::toString() const noexcept`

Use `std::stringstream`. Write `[x,y,w]` using default float precision (6 significant digits).

Expected results to verify against:
- `Vector3D(1.0f, 2.0f, 3.0f)` → `[1,2,3]`
- `Vector3D(pi, pi, pi)` → `[3.14159,3.14159,3.14159]`
- `Vector3D(1.23456789f, 9.876543210f, 12435.0987654321f)` → `[1.23457,9.87654,12435.1]`

---

## Matrix3x3_PS1.cpp

**Include:** `Matrix3x3.h`, `<cassert>`, `<sstream>`

Use `const Matrix3x3& M = *this;` idiom throughout (consistent with existing Matrix3x3.cpp style).

### `bool Matrix3x3::operator==( const Matrix3x3& aOther ) const noexcept`

Compare row by row using Vector3D::operator==:
```
M[0] == aOther[0] && M[1] == aOther[1] && M[2] == aOther[2]
```

### `Matrix3x3 Matrix3x3::operator*( const Matrix3x3& aOther ) const noexcept`

Result[i][j] = row(i).dot( column(j) of aOther ).
Call `aOther.column()` exactly 3 times (once per column, stored in local variables).
No loops — direct construction:

```cpp
Vector3D c0 = aOther.column(0);
Vector3D c1 = aOther.column(1);
Vector3D c2 = aOther.column(2);
return Matrix3x3(
    Vector3D( M[0].dot(c0), M[0].dot(c1), M[0].dot(c2) ),
    Vector3D( M[1].dot(c0), M[1].dot(c1), M[1].dot(c2) ),
    Vector3D( M[2].dot(c0), M[2].dot(c1), M[2].dot(c2) )
);
```

### `Matrix3x3 Matrix3x3::transpose() const noexcept`

The columns of M become the rows of M^T.
Call `column()` exactly 3 times:

```cpp
return Matrix3x3( column(0), column(1), column(2) );
```

### `float Matrix3x3::det() const noexcept`

Cofactor expansion along row 0. Using 0-indexed M[row][col]:

```
M[0][0] * (M[1][1]*M[2][2] - M[1][2]*M[2][1])
- M[0][1] * (M[1][0]*M[2][2] - M[1][2]*M[2][0])
+ M[0][2] * (M[1][0]*M[2][1] - M[1][1]*M[2][0])
```

No loops.

### `bool Matrix3x3::hasInverse() const noexcept`

```cpp
return det() != 0.0f;
```

### `Matrix3x3 Matrix3x3::inverse() const noexcept`

Assert invertibility first: `assert( hasInverse() )`.
Apply the explicit 3×3 inverse formula (from PDF), divided by `det()`:

```
Row 0: [ M22*M33 - M23*M32,  M13*M32 - M12*M33,  M12*M23 - M13*M22 ]
Row 1: [ M23*M31 - M21*M33,  M11*M33 - M13*M31,  M13*M21 - M11*M23 ]
Row 2: [ M21*M32 - M22*M31,  M12*M31 - M11*M32,  M11*M22 - M12*M21 ]
```

Index mapping (1-based formula → 0-indexed code):
- M11 = M[0][0], M12 = M[0][1], M13 = M[0][2]
- M21 = M[1][0], M22 = M[1][1], M23 = M[1][2]
- M31 = M[2][0], M32 = M[2][1], M33 = M[2][2]

Multiply the whole result matrix by `(1.0f / det())` using existing `operator*(float)`.

No loops.

### `std::ostream& operator<<( std::ostream& aOStream, const Matrix3x3& aMatrix )`

Rely on `Vector3D::toString()` for each row:

```cpp
aOStream << "[" << aMatrix[0].toString() << ","
                << aMatrix[1].toString() << ","
                << aMatrix[2].toString() << "]";
```

Expected: `[[25,-3,-8],[6,2,15],[11,-3,4]]`

---

## Known gotchas / watch points

1. **`operator[]` on Vector3D** uses `reinterpret_cast` into raw memory order `[fBaseVector.fX, fBaseVector.fY, fW]` — so `[0]` = x, `[1]` = y, `[2]` = w. Consistent with what the PDF calls M_ij.

2. **toString() vs operator<<**: The existing `Vector3D::operator<<` delegates to `Vector2D` (which rounds to integers). That is NOT the same as `toString()`. The Matrix3x3 output operator must call `toString()`, not use `operator<<` on the rows.

3. **No loops**: The PDF explicitly says matrix multiplication, det, transpose, inverse must all be computed without loops. Use direct expressions.

4. **`inverse()` marked `noexcept`** in the header — but it calls `assert()`. `assert` aborts on failure rather than throwing, so `noexcept` is still valid here. Follow what the header says.

5. **`column()` returns by value** (not reference) — confirmed in `Matrix3x3.h`. Safe to store in a local `Vector3D`.

6. **Epsilon (`eps`)** is defined in `Vector3D.h`. It will be visible in `Vector3D_PS1.cpp` via `#include "Vector3D.h"`.

---

## Stage 2 checklist (for reference after Stage 1 is approved)

- [ ] Write `Vector3D_PS1.cpp`
- [ ] Write `Matrix3x3_PS1.cpp`
- [ ] Verify output matches expected exactly (both P1 and P2 blocks)
