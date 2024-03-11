//
// Created by titoug on 27/02/24.
//


#include "liste.h"

#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

struct SCell {
    Data value;
    SCell *next;
    SCell *prev;
};

struct SList {
    SCell *head;
    SCell *tail;
};

SList* CreateList() {

    SCell *head = malloc(sizeof(SCell));
    head->value = 1;
    head->next = NULL;
    head->prev = NULL;

    SList *list = malloc(sizeof(SList));
    list->head = head;
    list->tail = head;

    return list;
}

SCell* AddElementBegin(SList *list,Data elem) {

    SCell *addCell  = malloc(sizeof(SCell));
    addCell->value = elem;
    addCell->next = list->head;
    addCell->prev = NULL;

    list->head = addCell;

    return addCell;

}

SCell* AddElementEnd(SList *list,Data elem) {

    SCell *addCell = malloc(sizeof(SCell));
    addCell->value = elem;
    addCell->next = NULL;
    addCell->prev = list->tail;

    list->tail->next = addCell;
    list->tail = addCell;

    return addCell;

}

SCell* AddElementAfter(SList *list,SCell *cell,Data elem) {

    SCell *newCell = malloc(sizeof(SCell));
    newCell->value = elem;
    newCell->next = cell->next;
    newCell->prev = cell;

    cell->next = newCell;
    newCell->next->prev = newCell;

    return newCell;

}

SCell* GetFirstElement(SList *list) {

    return list->head;

}

SCell* GetLastElement(SList *list) {

    return list->tail;

}

SCell* GetNextElement(SCell *cell) {

    return cell->next;

}

SCell* GetPrevElement(SCell *cell) {

    return cell->prev;

}

Data GetData(SCell *cell) {

    return cell->value;

}

void DeleteList(SList *list) {

    free(list);

}

void DeleteCell(SList *list,SCell *cell) {

    cell->prev->next = cell->next;
    cell->next->prev = cell->prev;
    free(cell);

}


