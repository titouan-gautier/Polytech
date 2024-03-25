//
// Created by titoug on 18/03/24.
//

#include "arbre.h"

#include <stdbool.h>
#include <stdlib.h>

struct DoublePointer {

    SNode *left;
    SNode *right;

};

struct SNode {

    int val;
    bool isLeaf;

    union {

        unsigned char code;
        DoublePointer *children;

    };

};

SNode* CreateLeaf(int val) {

    DoublePointer *children = malloc(sizeof(DoublePointer));
    children -> left = NULL;
    children -> right = NULL;

    SNode *leaf = malloc(sizeof(SNode));
    leaf->val = val;
    leaf->isLeaf = true;
    leaf->children = children;

    return leaf;

}

SNode* AssocierNoeud(SNode *node1, SNode *node2) {

    DoublePointer *children = malloc(sizeof(DoublePointer));
    children->left = node1;
    children->right = node2;

    SNode *newNode = malloc(sizeof(SNode));
    newNode->val = node1->val + node2->val;
    newNode->isLeaf = false;
    newNode->children = children;

    return newNode;

}

void swap(SNode *a, SNode *b) {
    const SNode t = *a;
    *a = *b;
    *b = t;
}

int* DeuxPlusPetit(SNode *tabNode, int len) {

    int *min = malloc(sizeof(int) * 2);

    for (int i = 0; i < len; i++) {
        if (tabNode[i].val < min[0]) {
            min[0] = i;
        } else if (tabNode[i].val < min[1]) {
            min[1] = i;
        }
    }

    return min;

}

SNode* EtapeGlouton(SNode *tabNode, int len) {

    int *min = DeuxPlusPetit(tabNode, len);

    SNode *newNode = AssocierNoeud(&tabNode[min[0]], &tabNode[min[1]]);

    tabNode[min[0]] = *newNode;
    tabNode[min[1]] = NULL;

    return newNode;

}
