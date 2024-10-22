// 標準入力・出力を行うためのライブラリをインクルード
#include <iostream> 

// 名前空間stdを使用することで、std::cout や std::cin を省略して使用可能にする
using namespace std; 

// プログラムのエントリーポイントであるmain関数を定義
int main() { 
    // 整数型の変数aとbを宣言
    int a, b; 
    // 標準入力（キーボード入力）からaとbに値を代入
    cin >> a >> b; 
    // aとbの積を計算し、その結果を変数cに代入
    int c = a * b; 
    // cを2で割った余りが0なら（cが偶数であるなら）
    if (c % 2 == 0) 
        // "Even"（偶数）を出力し、改行する
        cout << "Even" << endl; 
    else 
        // "Odd"（奇数）を出力し、改行する
        cout << "Odd" << endl; 
}
