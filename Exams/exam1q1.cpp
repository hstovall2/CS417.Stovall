/* Hudson Stovall
CS 417
Exam 1
Question 1 Lambda/Hash */

#include <string>
#include <functional>

using namespace std;

struct S 
{
    string firstName;
    string lastName;
    string address;
    int numberOfWidgetsOrdered;
};

auto hashS = [](const S& s) -> size_t 
{
    return hash<string>()(s.firstName) ^ 
           hash<string>()(s.lastName) ^ 
           hash<string>()(s.address) ^ 
           hash<int>()(s.numberOfWidgetsOrdered);
};
