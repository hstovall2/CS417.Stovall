//Hudson Stovall
//Assignment 7
//Question 1

#include <iostream>
#include <fstream>
#include <string>
#include <memory>
using namespace std;

enum class Severity { WARNING, ERROR, UNRECOVERABLE };

class Logger 
{
private:
    static unique_ptr<Logger> instance;
    ofstream logFile;
    Logger() = default;
public:
    static Logger& getInstance() 
    {
        if (!instance) instance.reset(new Logger());
        return *instance;
    }
    void Startup(const string &fileName) { logFile.open(fileName, ios::app); }
    void Shutdown() { if (logFile.is_open()) logFile.close(); }
    void LogMessage(Severity severity, const string &service, const string &message) 
    {
        if (!logFile.is_open()) return;
        string severityText = (severity == Severity::WARNING) ? "WARNING" :
                              (severity == Severity::ERROR) ? "ERROR" : "UNRECOVERABLE";
        logFile << "[" << severityText << "] " << "Service: " << service << " - " << message << endl;
    }
};
unique_ptr<Logger> Logger::instance = nullptr;

//test program
int main() 
{
    Logger& logger = Logger::getInstance();
    logger.Startup("app_log.txt");
    string service, message;
    int severityOption;
    cout << "Enter the service name: ";
    getline(cin, service);
    while (true) 
    {
        cout << "\nEnter severity level (0=WARNING, 1=ERROR, 2=UNRECOVERABLE, -1=Exit): ";
        cin >> severityOption;
        if (severityOption == -1) break;
        if (severityOption < 0 || severityOption > 2) continue;
        cout << "Enter the message: ";
        cin.ignore();
        getline(cin, message);
        logger.LogMessage(static_cast<Severity>(severityOption), service, message);
        cout << "Message logged.\n";
    }
    logger.Shutdown();
    return 0;
}
