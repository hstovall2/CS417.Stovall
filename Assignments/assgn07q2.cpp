//Hudson Stovall
//Assignment 7
//Question 2

#include <iostream>
#include <string>
using namespace std;

struct Office 
{
    string m_street;
    string m_city;
    int32_t m_cubicle;
    Office(string street, string city, int32_t cubicle)
        : m_street(street), m_city(city), m_cubicle(cubicle) {}
};

class Employee 
{
private:
    string m_name;
    Office* m_office;
    Employee(string name, Office* office) : m_name(name), m_office(office) {}
public:
    Employee(const Employee &rhs)
        : m_name(rhs.m_name), m_office(new Office(*rhs.m_office)) {}
    Employee& operator=(const Employee &rhs) 
    {
        if (this == &rhs) return *this;
        m_name = rhs.m_name;
        m_office = new Office(*rhs.m_office);
        return *this;
    }
    friend ostream &operator<<(ostream &os, const Employee &e) 
    {
        return os << e.m_name << " works at "
                  << e.m_office->m_street << ", " << e.m_office->m_city
                  << ", cubicle #" << e.m_office->m_cubicle;
    }

    friend class EmployeeFactory;
};

class EmployeeFactory 
{
public:
    static Employee createEmployee(string name, string street, string city, int32_t cubicle) 
    {
        Office* office = new Office(street, city, cubicle);
        return Employee(name, office);
    }
};

//test program
int main() 
{
    Employee e1 = EmployeeFactory::createEmployee("Alice", "123 Maple St", "Springfield", 101);
    Employee e2 = EmployeeFactory::createEmployee("Bob", "456 Oak St", "Greendale", 202);
    cout << e1 << endl;
    cout << e2 << endl;
    return 0;
}
