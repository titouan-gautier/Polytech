#include <stdlib.h>
#include <string.h>

// Define a structure for stack node
typedef struct StackNode {
    char* data;            // Dynamically allocated string
    struct StackNode* next; // Pointer to the next node
} StackNode;

// Define a structure for the stack
typedef struct {
    StackNode* top; // Pointer to the top of the stack
} Stack;

// Function to initialize an empty stack
void initStack(Stack* stack) {
    stack->top = NULL;
}

// Function to check if the stack is empty
int isEmpty(const Stack* stack) {
    return (stack->top == NULL);
}

// Function to push a string onto the stack
void push(Stack* stack, const char* data) {
    // Create a new node
    StackNode* newNode = malloc(sizeof(StackNode));
    if (newNode == NULL) {
        // Handle memory allocation error
        exit(EXIT_FAILURE);
    }

    // Allocate memory for the string and copy the data
    newNode->data = strdup(data);
    if (newNode->data == NULL) {
        // Handle memory allocation error
        free(newNode);
        exit(EXIT_FAILURE);
    }

    // Set the next pointer and update the top of the stack
    newNode->next = stack->top;
    stack->top = newNode;
}

// Function to pop a string from the stack
char* pop(Stack* stack) {
    if (isEmpty(stack)) {
        // Handle stack underflow error, return NULL, or take appropriate action.
        return NULL;
    }

    // Retrieve the top node and data
    StackNode* topNode = stack->top;
    char* poppedString = topNode->data;

    // Update the top of the stack and free the node (but not the string)
    stack->top = topNode->next;
    free(topNode);

    return poppedString;
}

// Function to free the memory allocated for the stack
void freeStack(Stack* stack) {
    while (!isEmpty(stack)) {
        char* poppedString = pop(stack);
        free(poppedString);  // Free the string
    }
}