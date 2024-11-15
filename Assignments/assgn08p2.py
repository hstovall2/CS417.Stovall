#Hudson Stovall
#Assignment 8 Problem 2
#Bridge

class Formatter:
    def drawLine(self, x1, y1, x2, y2):
        raise NotImplementedError
    def drawPixel(self, x, y, color):
        raise NotImplementedError
    def drawCircle(self, x, y, radius):
        raise NotImplementedError

class Shape:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter
    def draw(self):
        raise NotImplementedError

class Screen(Formatter):
    def drawLine(self, x1, y1, x2, y2):
        print(f"Screen: Drawing line from ({x1}, {y1}) to ({x2}, {y2})")
    def drawPixel(self, x, y, color):
        print(f"Screen: Drawing pixel at ({x}, {y}) with color {color}")
    def drawCircle(self, x, y, radius):
        print(f"Screen: Drawing circle at ({x}, {y}) with radius {radius}")

class Printer(Formatter):
    def drawLine(self, x1, y1, x2, y2):
        print(f"Printer: Drawing line from ({x1}, {y1}) to ({x2}, {y2})")
    def drawPixel(self, x, y, color):
        print(f"Printer: Printing pixel at ({x}, {y}) with color {color}")
    def drawCircle(self, x, y, radius):
        print(f"Printer: Printing circle at ({x}, {y}) with radius {radius}")

class XMLFormatter(Formatter):
    def drawLine(self, x1, y1, x2, y2):
        print(f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' />")
    def drawPixel(self, x, y, color):
        print(f"<pixel x='{x}' y='{y}' color='{color}' />")
    def drawCircle(self, x, y, radius):
        print(f"<circle x='{x}' y='{y}' radius='{radius}' />")

class Square(Shape):
    def draw(self):
        print("Drawing a square:")
        self.formatter.drawLine(0, 0, 1, 0)
        self.formatter.drawLine(1, 0, 1, 1)
        self.formatter.drawLine(1, 1, 0, 1)
        self.formatter.drawLine(0, 1, 0, 0)

class Circle(Shape):
    def draw(self):
        print("Drawing a circle:")
        self.formatter.drawCircle(0, 0, 1)

class Polygon(Shape):
    def __init__(self, formatter: Formatter, vertices):
        super().__init__(formatter)
        self.vertices = vertices
    def draw(self):
        print("Drawing a polygon:")
        for i in range(len(self.vertices)):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % len(self.vertices)]
            self.formatter.drawLine(x1, y1, x2, y2)

def main():
    screenFormatter = Screen()
    printerFormatter = Printer()
    xmlFormatter = XMLFormatter()
    square = Square(screenFormatter)
    circle = Circle(printerFormatter)
    polygon = Polygon(xmlFormatter, [(0, 0), (1, 0), (0.5, 1)])
    square.draw()
    print()
    circle.draw()
    print()
    polygon.draw()

if __name__ == "__main__":
    main()
