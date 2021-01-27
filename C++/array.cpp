#include <iostream>    //输入输出流
using namespace std;
#include <iomanip>
using std::setw;  // setw() 函数来格式化输出
int main()
{
    int n[10];
    for (int i = 0; i < 10; i++)
    {
        n[i] = i + 100;

    }
    cout<<"element"<<setw(13)<<"value"<<endl;

    for (int j = 0; j < 10; j++)
    {
        cout << setw(7) << j << setw(13) << n[j] <<endl;
    }
    return 0;
}