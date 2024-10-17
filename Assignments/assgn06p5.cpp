//Hudson Stovall
//Assignment 6 #5

#include <iostream>
#include <string>

class Customer {
public:
    std::string name;
    std::string address;
    Customer(const std::string& name, const std::string& address) : name(name), address(address) {}
};

class Order {
public:
    double totalAmount;
    Order(double totalAmount) : totalAmount(totalAmount) {}
};

class ShippingLabel 
{
public:
    static void print(const Customer& customer) {
        std::cout << "Ship to: " << customer.name << std::endl;
        std::cout << "Address: " << customer.address << std::endl;
    }
};

int main() 
{
    Customer customer("John Doe", "123 Elm St");
    Order order(250.0);
    ShippingLabel::print(customer);
    return 0;
}
