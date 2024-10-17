//Hudson Stovall
//Assignment 6 Refactoring #3

#include <iostream>
#include <vector>
#include <string>

class TaskManager {
private:
    std::vector<std::string> tasks;

public:
    void addTask(const std::string& task) {
        tasks.push_back(task);
    }

    void printTasks() const {
        for (const auto& task : tasks) {
            std::cout << task << std::endl;
        }
    }
};

class Employee {
private:
    std::string name;
    int salary;

public:
    Employee(const std::string& name, int salary) : name(name), salary(salary) {}

    void giveRaise(int amount) {
        salary += amount;
    }

    void printEmployeeInfo() const {
        std::cout << "Name: " << name << ", Salary: " << salary << std::endl;
    }
};

int main() {
    Employee emp("John Doe", 50000);
    emp.printEmployeeInfo();

    TaskManager taskManager;
    taskManager.addTask("Finish report");
    taskManager.addTask("Attend meeting");

    std::cout << "Tasks:" << std::endl;
    taskManager.printTasks();

    return 0;
}
