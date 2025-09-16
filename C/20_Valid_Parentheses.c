#include <stdio.h>

typedef struct Stack{
    struct Stack* next;
    char c;
} Stack;

void push(Stack** top, char chr)
{
    Stack* newNode = malloc(sizeof(Stack));
    newNode->next = *top;
    *top = newNode;
    newNode->c = chr;
}

char pop(Stack** top)
{
    if (*top == NULL) return '\0';

    char chr = (*top)->c;

    Stack* temp = *top;
    *top = temp->next;
    free(temp);
    return chr;
}

void freeStack(Stack* top)
{
    Stack* temp = top;

    while (top != NULL)
    {
        top = top->next;
        free(temp);
        temp = top;
    }
}

int isValid(char* s)
{
    Stack* top = NULL;

    for (int i = 0; s[i] != '\0'; i++)
    {
        char ch = s[i];
        if ((ch == '(') || (ch == '[') || (ch == '{')) push(&top, ch);
        else if ((ch == ')') || (ch == ']') || (ch == '}'))
        {
            char open = pop(&top);

            if ((ch == ')' && open != '(') || (ch == ']' && open != '[') || (ch == '}' && open != '{')) 
            {
                freeStack(top);
                return 0;
            }
        }
    }
    int valid = (top == NULL);
    freeStack(top);
    return valid;
}