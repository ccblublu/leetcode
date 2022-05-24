#include <iostream>
#include <vector>

using namespace std;

class str2num
{
private:
    /* data */
    const int MAX_WIDTH = 100;
public:
    str2num(/* args */);
    ~str2num();
    vector<int> numberOfLines(vector<int>& widths, string s){
        int lines = 1;
        int width = 0;
        for (auto & c : s) {
            cout << c-'a' << endl;
            int need = widths[c - 'a'];
            width += need;
            if (width > str2num::MAX_WIDTH) {
                lines++;
                width = need;
            }
        }
        return {lines, width};
    };
};

str2num::str2num(/* args */)
{
}

str2num::~str2num()
{
}

int main( ){
    vector<int> widths = {10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10};
    string S = "abcdefghijklmnopqrstuvwxyz";
    str2num str2 = str2num();
    vector<int> res = str2.numberOfLines(widths,S);
    cout << res[0] << endl;
    cout << res[1] << endl;
    return 0;
}