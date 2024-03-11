//
// Created by titoug on 27/02/24.
//

#include "listeBlocMemoire.h"
#include <stdio.h>
#include <stdlib.h>

// Taille des blocs
#define BLOC_SIZE 5

// Structure de la cellule
struct SCell {
    Data value;
    SCell *next;
    SCell *prev;
};

// Structure du block
struct Block {
    SCell* cells;
    int nbCell;
    Block* next;
};

// Structure de la liste
struct SList {
    Block *curBlock;
    SCell *head;
    SCell *tail;
    Recycle *recycle;
};

// Structure de la cellule recyclé
struct Recycle {
    Block* block;
    int nbCellUsed;
};

// Fonction qui alloue de la mémoire par bloc
SCell* AllocMemory(SList *list) {

    SCell *newCell;

    // Si il y a des cell recyclé er que le nombre de cell utilisé est différent du nombre de cell disponible
    if (list->recycle->block->nbCell > 0 && list->recycle->block->nbCell != list->recycle->nbCellUsed) {

        newCell = &list->recycle->block->cells[list->recycle->nbCellUsed];
        list->curBlock->nbCell += 1;
        list->recycle->nbCellUsed += 1;
        return newCell;

    }

    //Si le block courant n'est pas rempli
    if (list->curBlock->nbCell < BLOC_SIZE) {

        newCell = &list->curBlock->cells[list->curBlock->nbCell];
        list->curBlock->nbCell += 1;
        return newCell;

    }

    //Sinon on recré un block et on ajoute la nouvelle cell
    Block *block = malloc(sizeof(Block));
    block->cells = malloc(sizeof(SCell) * BLOC_SIZE);
    block->next = NULL;
    block->nbCell = 0;

    list->curBlock->next = block;
    list->curBlock = block;

    newCell = &list->curBlock->cells[list->curBlock->nbCell];
    list->curBlock->nbCell += 1;
    return newCell;

}

// Fonction qui crée une liste
SList* CreateList() {

    // Allocation de la mémoire pour la liste de cellules
    SCell *memory = malloc(sizeof(SCell) * BLOC_SIZE - 1);

    //Création de la première cellule
    SCell *head = &memory[0];
    head->value = 0;
    head->next = NULL;
    head->prev = NULL;

    //Création du premier block
    Block *block = malloc(sizeof(Block));
    block->cells = memory;
    block->next = NULL;
    block->nbCell = 1;

    //Création de la liste
    SList *list = malloc(sizeof(SList));
    list->head = head;
    list->tail = head;
    list->curBlock = block;

    //Création de la liste de cellules recyclées
    list->recycle = malloc(sizeof(Recycle));
    list->recycle->block = malloc(sizeof(Block));
    list->recycle->block->cells = malloc(sizeof(SCell) * BLOC_SIZE);
    list->recycle->block->next = NULL;
    list->recycle->block->nbCell = 0;

    return list;
}

// Fonction qui ajoute une cellule au début de la liste
SCell* AddElementBegin(SList *list,Data elem) {

    // Allocation de la mémoire pour la nouvelle cellule
    SCell *addCell = AllocMemory(list);
    addCell->value = elem;
    addCell->next = list->head;
    addCell->prev = NULL;

    // Mise à jour de la liste
    list->head->prev = addCell;
    list->head = addCell;

    return addCell;

}

// Fonction qui ajoute une cellule à la fin de la liste
SCell* AddElementEnd(SList *list,Data elem) {

    // Allocation de la mémoire pour la nouvelle cellule
    SCell *addCell = AllocMemory(list);
    addCell->value = elem;
    addCell->next = NULL;
    addCell->prev = list->tail;

    // Mise à jour de la liste
    list->tail->next = addCell;
    list->tail = addCell;

    return addCell;

}

// Fonction qui ajoute une cellule après une autre cellule
SCell* AddElementAfter(SList *list,SCell *cell,Data elem) {

    // Allocation de la mémoire pour la nouvelle cellule
    SCell *newCell = AllocMemory(list);
    newCell->value = elem;
    newCell->next = cell->next;
    newCell->prev = cell;

    // Mise à jour de la liste
    cell->next = newCell;
    newCell->next->prev = newCell;

    return newCell;

}

// Fonction qui retourne la première cellule de la liste
SCell* GetFirstElement(SList *list) {

    return list->head;

}

// Fonction qui retourne la dernière cellule de la liste
SCell* GetLastElement(SList *list) {

    return list->tail;

}

// Fonction qui retourne la cellule suivante
SCell* GetNextElement(SCell *cell) {

    return cell->next;

}

// Fonction qui retourne la cellule précédente
SCell* GetPrevElement(SCell *cell) {

    return cell->prev;

}

// Fonction qui retourne la valeur de la cellule
Data GetData(SCell *cell) {

    return cell->value;

}

// Fonction qui supprime la liste
void DeleteList(SList *list) {

    free(list);

}

// Fonction qui supprime une cellule
void DeleteCell(SList *list,SCell *cell) {

    // Si la cellule n'est pas la première ou la dernière
    if (cell->prev != NULL && cell->next != NULL) {

        cell->prev->next = cell->next;
        cell->next->prev = cell->prev;

        // Si la cellule est la première
    } else if (cell->prev == NULL) {

        cell->next->prev = NULL;
        list->head = cell->next;

        // Si la cellule est la dernière
    } else if (cell->next == NULL) {

        list->tail = cell->prev;
        cell->prev->next = NULL;

    }

    // On ajoute la cellule à la liste de cellules recyclées
    list->recycle->block->cells[list->recycle->block->nbCell] = *cell;
    list->recycle->block->nbCell += 1;

}


