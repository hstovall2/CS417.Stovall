//Hudson Stovall
//Assignment 6 Refactoring #4

#include <iostream>
#include <string>

class Pricing 
{
public:
    static double calculateTotal(double price, int quantity) {
        return price * quantity;
    }
    static double applyDiscount(double total) {
        return (total > 100) ? total * 0.1 : 0;
    }
};

class Shipping 
{
public:
    static double calculateShipping(int quantity) {
        return (quantity > 10) ? 0 : 5;
    }
};

class Order 
{
private:
    std::string customerName;
    std::string productName;
    int quantity;
    double price;

public:
    Order(const std::string& customerName, const std::string& productName, int quantity, double price)
        : customerName(customerName), productName(productName), quantity(quantity), price(price) {}

    void processOrder() {
        double total = Pricing::calculateTotal(price, quantity);
        double discount = Pricing::applyDiscount(total);
        double finalPrice = total - discount;

        std::cout << "Total price (after discount): " << finalPrice << std::endl;

        double shippingCost = Shipping::calculateShipping(quantity);
        std::cout << "Shipping cost: " << shippingCost << std::endl;

        double finalAmount = finalPrice + shippingCost;
        std::cout << "Order processed for: " << customerName << std::endl;
        std::cout << "Final amount to be paid: " << finalAmount << std::endl;
    }
};

int main() 
{
    Order order("John Doe", "Laptop", 12, 80);
    order.processOrder();
    return 0;
}
