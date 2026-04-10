from pathlib import Path

class Vector2D:

    def __init__(self, x=0.0, y=0.0):
        self.fX = x
        self.fY = y

    def subtract(self, other):
        return Vector2D(self.fX - other.fX, self.fY - other.fY)

    def scale(self, scalar):
        return Vector2D(self.fX * scalar, self.fY * scalar)

    def length(self):
        return (self.fX * self.fX + self.fY * self.fY) ** 0.5

    def to_string(self):
        if int(self.fX) == self.fX and int(self.fY) == self.fY:
            return f"[{int(self.fX)},{int(self.fY)}]"
        return f"[{self.fX},{self.fY}]"


MAX_VERTICES = 30

class Polygon:

    def __init__(self):
        self.fVertices = [Vector2D() for _ in range(MAX_VERTICES)]
        self.fNumberOfVertices = 0

    def readData(self, filename):
        self.fNumberOfVertices = 0

        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split()

                if len(parts) != 2:
                    continue

                x = float(parts[0])
                y = float(parts[1])

                if self.fNumberOfVertices < MAX_VERTICES:

                    self.fVertices[self.fNumberOfVertices] = Vector2D(x, y)
                    self.fNumberOfVertices += 1

    def getNumberofVertices(self):
        return self.fNumberOfVertices

    def getVertex(self, index):
        return self.fVertices[index]

    def getPerimeter(self):
        perimeter = 0.0

        for i in range(self.fNumberOfVertices):

            next_index = (i + 1) % self.fNumberOfVertices

            current_vertex = self.fVertices[i]

            next_vertex = self.fVertices[next_index]

            segment = next_vertex.subtract(current_vertex)

            perimeter += segment.length()

        return perimeter

    def scale(self, scalar):
        result = Polygon()

        result.fNumberOfVertices = self.fNumberOfVertices

        for i in range(self.fNumberOfVertices):
            result.fVertices[i] = self.fVertices[i].scale(scalar)

        return result


filename = Path(__file__).with_name("Data.txt")

lPolygon = Polygon()
lPolygon.readData(filename)

print("Data read: ")

for i in range(lPolygon.getNumberofVertices()):
    print("Vertex #" + str(i) + ":" + lPolygon.getVertex(i).to_string())

print("The perimeter of lPolygon is " + str(round(lPolygon.getPerimeter(), 2)))

print("Scale polygon by 3.2:")
lScaled = lPolygon.scale(3.2)
print("The perimeter of lScaled is " + str(round(lScaled.getPerimeter(), 2)))

lFactor = round(lScaled.getPerimeter() / lPolygon.getPerimeter(), 2)
print("Scale factor: " + str(lFactor))
