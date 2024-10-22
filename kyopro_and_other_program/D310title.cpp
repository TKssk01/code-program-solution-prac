#include <iostream>
using namespace std;
int main(void){
    // 自分の得意な言語で
    // Let's チャレンジ！！
    string s_1,s_2,s_3;
    getline(cin, s_1);
    getline(cin, s_2);
    getline(cin, s_3);
    
    char c1 = s_1[0];
    char c2 = s_2[0];
    char c3 = s_3[0];
    
    string abbreviation = "";
    abbreviation += c1;
    abbreviation += c2;
    abbreviation += c3;
    
    cout << abbreviation << endl;
    
    return 0;
}