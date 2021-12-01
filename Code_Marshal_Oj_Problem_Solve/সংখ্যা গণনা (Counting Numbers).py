# Language Solution: C++.

#include<iostream>
using namespace std;

int main()
{
    int testcase;
    cin >> testcase;

    for(int i = 1; i <= testcase; i++)
    {
        int n, c[101] = {0}, tmp;
        cin >> n;
        for(int j = 0; j < n; j++)
        {
          cin>>tmp;
          c[tmp]++;
        }

        int h = 0,m;
        for(int j = 0; j <= 100; j++)
        {
            if(c[j] >= h)
            {
                h = c[j];
                m = j;
            }
        }
        cout<<"Case "<< i <<": "<< m <<" "<< h <<endl;
    }

}
