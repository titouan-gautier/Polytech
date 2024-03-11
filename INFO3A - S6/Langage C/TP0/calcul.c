//
// Created by titoug on 30/01/24.
//

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int x1 = 0;
    int y1 = 0;
    int x2 = 10;
    int y2 = 5;

    double a = abs(x1-x2)*abs(x1-x2);
    double b = abs(y1-y2)*abs(y1-y2);

    double dist = sqrt(a + b);

    printf("%f \n",dist);

}