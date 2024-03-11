#ifndef STACK_H
#define STACK_H

#include <stdio.h>
#include <string.h>

#define MAX_SIZE 100
#define MAX_STRING_LENGTH 50

typedef struct {
    char items[MAX_SIZE][MAX_STRING_LENGTH + 1]; // +1 for the null terminator
    int top;
} Stack;

void initStack(Stack *stack);

int isEmpty(Stack *stack);

int isFull(Stack *stack);

void push(Stack *stack, const char *value);

const char* pop(Stack *stack);

#endif // STACK_H
