# Language: C.
#include <stdio.h>
#include<math.h>

int main ()
{
    int i, j, n;
    scanf("%d", &n);

    for(i = 1; i <= n; i++)
    {
        double a, b, c;
        double s = 0, area = 0;
        scanf("%lf %lf %lf", &a, &b, &c);

        s = (a+b+c)/2;

        area = sqrt(s * (s-a) * (s-b) * (s-c));

        printf("Case %d: %.10lf\n", i, area);
    }

    return 0;
}
