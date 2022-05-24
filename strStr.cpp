#include <iostream>
#include <cstring>
#include "KMP.h"
using namespace std;

int main()
{
    string haystack = "aaaaa", needle = "bba";
    Kmp kmp1(haystack, needle);
    
    return 0;
}