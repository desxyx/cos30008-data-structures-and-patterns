import math


def format_number(value):
    rounded = round(value, 2)

    if math.isclose(rounded, round(rounded)):
        return str(int(round(rounded)))

    return str(rounded)


# Vector2D.h + Vector2D.cpp
class Vector2D:
    def __init__(self, x=1.0, y=1.0):
        self.fX = float(x)
        self.fY = float(y)

    def x(self):
        return self.fX

    def y(self):
        return self.fY

    def __add__(self, other):
        # [x1, y1] + [x2, y2] = [x1 + x2, y1 + y2]
        return Vector2D(self.fX + other.fX, self.fY + other.fY)

    def __sub__(self, other):
        return Vector2D(self.fX - other.fX, self.fY - other.fY)

    def __mul__(self, scalar):
        return Vector2D(self.fX * scalar, self.fY * scalar)

    def dot(self, other):
        return self.fX * other.fX + self.fY * other.fY

    def cross(self, other):
        return self.fX * other.fY - self.fY * other.fX

    def length(self):
        value = math.sqrt(self.fX * self.fX + self.fY * self.fY)
        return round(value, 2)

    def normalize(self):
        length = self.length()
        if length == 0:
            return Vector2D(0.0, 0.0)
        return self * (1.0 / length)

    def direction(self):
        value = math.degrees(math.atan2(self.fY, self.fX))
        return round(value, 2)

    def align(self, angle_in_degrees):
        radians = math.radians(angle_in_degrees)

        length = self.length()
        unit_direction = Vector2D(math.cos(radians), math.sin(radians))

        return unit_direction * length

    def __repr__(self):
        return f"[{format_number(self.fX)},{format_number(self.fY)}]"

class Vector3D:
    def __init__(self, x=1.0, y=0.0, w=1.0):
        self.fBaseVector = Vector2D(x, y)
        self.fW = float(w)

    @classmethod
    def from_vector2d(cls, vector2d):
        return cls(vector2d.x(), vector2d.y(), 1.0)

    def x(self):
        return self.fBaseVector.x()

    def y(self):
        return self.fBaseVector.y()

    def w(self):
        return self.fW

    def __getitem__(self, index):
        if index == 0:
            return self.x()
        if index == 1:
            return self.y()
        if index == 2:
            return self.w()
        raise IndexError("Vector3D index out of range.")

    def to_vector2d(self):
        if self.fW == 0:
            raise ZeroDivisionError("w cannot be zero when converting to Vector2D")
        return Vector2D(self.x() / self.fW, self.y() / self.fW)

    def __mul__(self, scalar):
        return Vector3D(self.x() * scalar, self.y() * scalar, self.w() * scalar)

    def __add__(self, other):
        return Vector3D(
            self.x() + other.x(),
            self.y() + other.y(),
            self.w() + other.w(),
        )

    def dot(self, other):
        return (
            self.x() * other.x()
            + self.y() * other.y()
            + self.w() * other.w()
        )

    def __repr__(self):
        return repr(self.to_vector2d())

class Matrix3x3:

    def __init__(self, row1=None, row2=None, row3=None):
        if row1 is None and row2 is None and row3 is None:
            self.fRows = [
                Vector3D(1.0, 0.0, 0.0),
                Vector3D(0.0, 1.0, 0.0),
                Vector3D(0.0, 0.0, 1.0),
            ]
        else:
            self.fRows = [row1, row2, row3]

    def __getitem__(self, row_index):
        return self.row(row_index)

    def row(self, row_index):
        return self.fRows[row_index]

    def column(self, column_index):
        return Vector3D(
            self.fRows[0][column_index],
            self.fRows[1][column_index],
            self.fRows[2][column_index],
        )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix3x3(
                self.fRows[0] * other,
                self.fRows[1] * other,
                self.fRows[2] * other,
            )

        if isinstance(other, Vector3D):
            return Vector3D(
                self.fRows[0].dot(other),
                self.fRows[1].dot(other),
                self.fRows[2].dot(other),
            )

        raise TypeError("Unsupported multiplication")

    def __add__(self, other):
        return Matrix3x3(
            self.fRows[0] + other.fRows[0],
            self.fRows[1] + other.fRows[1],
            self.fRows[2] + other.fRows[2],
        )

    @staticmethod
    def getS(aX=1.0, aY=1.0):
        return Matrix3x3(
            Vector3D(aX, 0.0, 0.0),
            Vector3D(0.0, aY, 0.0),
            Vector3D(0.0, 0.0, 1.0),
        )

    @staticmethod
    def getT(aX=0.0, aY=0.0):
        return Matrix3x3(
            Vector3D(1.0, 0.0, aX),
            Vector3D(0.0, 1.0, aY),
            Vector3D(0.0, 0.0, 1.0),
        )

    @staticmethod
    def getR(angle_in_degree=0.0):
        radians = math.radians(angle_in_degree)
        
        c = math.cos(radians)
        s = math.sin(radians)

        return Matrix3x3(
            Vector3D(c, -s, 0.0),
            Vector3D(s, c, 0.0),
            Vector3D(0.0, 0.0, 1.0),
        )

# Main.cpp
def main():
    a = Vector2D(1.0, 2.0)
    b = Vector2D(1.0, 4.0)
    c = Vector2D(-2.0, 3.0)
    d = Vector2D(0.0, 0.0)

    print("Test vector implementation:")
    print("Vector a =", a)
    print("Vector b =", b)
    print("Vector c =", c)
    print("Vector d =", d)

    a3 = Vector3D.from_vector2d(a)
    b3 = Vector3D.from_vector2d(b)
    c3 = Vector3D.from_vector2d(c)
    d3 = Vector3D.from_vector2d(d)

    print("Vector a3 =", a3)
    print("Vector b3 =", b3)
    print("Vector c3 =", c3)
    print("Vector d3 =", d3)

    print("Test homogeneous vectors:")
    print("Vector", a3, "* 3.0 =", a3 * 3.0)
    print("Vector", a3, "+", b3, "=", a3 + b3)
    print("Vector", a3, ".", b3, "=", a3.dot(b3))
    print("Vector", a3, "[0] =", a3[0], "<=>", a3, ".x() =", a3.x())
    print("Vector", a3, "[1] =", a3[1], "<=>", a3, ".y() =", a3.y())
    print("Vector", a3, "[2] =", a3[2], "<=>", a3, ".w() =", a3.w())

    print("Test 3x3 matrix:")

    MA = Matrix3x3(Vector3D(1.0, 1.0), Vector3D(1.0, 1.0), Vector3D(1.0, 1.0))

    print("MA[0] =", MA[0])
    print("MA[1] =", MA[1])
    print("MA[2] =", MA[2])

    MB = MA * 2.0

    print("MB[0] =", MB[0])
    print("MB[1] =", MB[1])
    print("MB[2] =", MB[2])

    MC = MB + MA

    print("MC[0] =", MC[0])
    print("MC[1] =", MC[1])
    print("MC[2] =", MC[2])

    lS = Matrix3x3.getS(3.2, 3.2)
    lR = Matrix3x3.getR(90.0)
    lT = Matrix3x3.getT(4.0, -1.0)

    print("Scale", a3, "by", 3.2, "=", lS * a3)
    print("Rotate", b3, "by", 90.0, "degrees =", lR * b3)
    print("Translate", c3, "by", lT.column(2), "=", lT * c3)
    print("Translate", d3, "by", lT.column(2), "=", lT * d3)


if __name__ == "__main__":
    main()
