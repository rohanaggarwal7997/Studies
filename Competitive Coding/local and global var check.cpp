#include<iostream>
using namespace std;
int a=5;
void fun()
{
    int b=0;
    if(b)
    {
        int a=4;
        cout<<a;
    }
    else
    {
        cout<<a;            //C++ will still refer to global and local variable differently not in python
    }

}
int main()
{
    fun();
    cout<<a;
    return 0;
}
