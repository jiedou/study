/*
  申请一块连续的内存空间使用 new TYPE[]
                    释放使用 delete[] 
*/

#include <iostream>
using namespace std;
int main()
{

    int *p=new int[8];
    int i=0;
    for(i=0;i<8;i++)
    {
        p[i]=i+1;
    }
    delete[] p;
    p=new int(2);
    cout<<"*p="<<*p<<endl;
    delete[] p;
    char ch[10]="abcdef";
    char *p_char=new(ch) char;
    cout<<"p_char="<<p_char<<endl;

    return 0;
}
