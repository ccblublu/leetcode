#include <iostream>
#include <cstring>
class Kmp {
public:
    Kmp();
    ~Kmp();
    int match (const std::string P, const std::string S);
    int match (char* P, char* S);
    int* buildNext(const std::string P);
private:
    
    int* buildNext(char* P);
};
