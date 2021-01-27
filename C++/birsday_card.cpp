#include<iostream>
using namespace std;
int main()
{
    char name1[50], name2[50]; //生明语句，name1，2为字符数组
    cin>>name1>>name2; //先声明后使用
    cout<<"##################"<<endl;
    cout<<name1<<endl;
    cout<<endl;
    cout<<"happy birthday to you"<<endl;
    cout<<endl;
    cout<<"            sincerely yours"<<name2<<endl;
    cout<<"##########"<<endl;
    return 0;
}