//Hudson Stovall
//Assignment 6 Refactoring #1

#include <iostream> 

class Rectangle 
{
protected:
    int width;
    int height;

public:
    Rectangle(int w, int h) : width(w), height(h) {}

    int area() const {
        return width * height;
    }

    int perimeter() const {
        return 2 * (width + height);
    }
};

class Square : public Rectangle 
{
public:
    Square(int side) : Rectangle(side, side) {}
};

int main() 
{
    Rectangle rect(4, 5);
    Square sq(3);

    std::cout << "Rectangle area: " << rect.area() << std::endl;
    std::cout << "Square area: " << sq.area() << std::endl;

    return 0;
}
