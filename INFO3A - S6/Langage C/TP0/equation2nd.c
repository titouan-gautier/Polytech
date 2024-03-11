//
// Created by titoug on 30/01/24.
//

#include <stdio.h>
#include <math.h>

int main() {

    double a;
    double b;
    double c;

    scanf("%lf", &a);
    scanf("%lf", &b);
    scanf("%lf", &c);

    double delta = (b*b) - 4 * a * c;

    if (delta > 0) {

        double r1 = (-b + sqrt(delta)) / 2 * a;
        double r2 = (-b - sqrt(delta)) / 2 * a;

        printf("r1: %f, r2: %f \n",r1,r2);

    }
    else if (delta == 0) {

        double r = -b / 2 * a;
        printf("r: %f \n",r);

    }
    else {

        printf("Delta négatif donc il n'y a pas de racine \n");

    }


}