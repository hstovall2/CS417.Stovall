/* Hudson Stovall
CS 417
Exam 2
Question 1 */

#include <string>

using namespace std;

enum class ErrorLevel { SEVERE, ERROR, WARNING, INFO };
struct ErrorContext 
{
    ErrorLevel errlevel;
    const char* logmsg;
};
extern void SDAOSlogger(ErrorContext& logcontext);

class Logger 
{
public:
    static Logger& getInstance() 
    {
        static Logger instance;
        return instance;
    }
    void logSevere(const std::string& message) { log(ErrorLevel::SEVERE, message); }
    void logError(const std::string& message) { log(ErrorLevel::ERROR, message); }
    void logWarning(const std::string& message) { log(ErrorLevel::WARNING, message); }
    void logInfo(const std::string& message) { log(ErrorLevel::INFO, message); }
private:
    Logger() = default;
    Logger(const Logger&) = delete;
    Logger& operator=(const Logger&) = delete;
    void log(ErrorLevel level, const std::string& message) 
    {
        ErrorContext context{level, message.c_str()};
    }
};

int main() 
{
    auto& logger = Logger::getInstance();
    logger.logSevere("SEVERE");
    logger.logError("ERROR");
    logger.logWarning("WARNING");
    logger.logInfo("INFO");
    return 0;
}
