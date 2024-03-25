//
// Created by titoug on 18/03/24.
//

#ifndef STATS_H
#define STATS_H

typedef struct Stats Stats;

Stats* StatistiquesFichiers(const char *nameFile);
int GetOccurence(Stats *stats, char c);

#endif //STATS_H
