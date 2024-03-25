#include <stdio.h>

#include "stats.h"

int main(void) {

    Stats *stats = StatistiquesFichiers("test.txt");

    printf("%d \n", GetOccurence(stats,'a'));
    printf("%d \n", GetOccurence(stats,'b'));

}
