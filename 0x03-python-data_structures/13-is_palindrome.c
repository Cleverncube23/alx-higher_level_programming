#include "lists.h"

#include <stdio.h>

/* Reverse linked list */
void reverse_list(listint_t **head);

/* Check if two lists are equivalent */  
int list_equiv(listint_t *l1, listint_t *l2);

/* Checks if linked list is palindrome */
int is_palindrome(listint_t **head)
{
  listint_t *skip_1, *skip_2, *prev_s1, *first_half, *second_half, *mid;

  /* Empty or single node lists are palindromes */
  if (!head || !(*head) || !((*head)->next))   
    return (1);

  first_half = skip_1 = skip_2 = prev_s1 = *head;
  second_half = mid = NULL;

  while (skip_1 && skip_2 && skip_2->next) {
    prev_s1 = skip_1;
    skip_1 = skip_1->next;
    skip_2 = skip_2->next->next;
  }

  if (skip_2 == NULL) { /* Even number of nodes */ 
    second_half = skip_1; 
  } else { /* Odd number of nodes */
    mid = skip_1;
    second_half = skip_1->next;
  }

  prev_s1->next = NULL; /* Null terminate first half */

  reverse_list(&second_half);
  
  if (list_equiv(first_half, second_half))
    return (1); /* Equivalent - palindrome */

  else  
    return (0); 
}

/* Check if two lists have equal data and length */
int list_equiv(listint_t *l1, listint_t *l2)
{
  while (l1 || l2) {
    if (l1->n != l2->n || !l1 || !l2)
      return (0);

    if (l1) l1 = l1->next; 
    if (l2) l2 = l2->next;
  }

  return (1);
}

/* Reverse a linked list */
void reverse_list(listint_t **head)
{
  listint_t *next = NULL, *prev = NULL, *cur;

  cur = *head; 
  while (cur) {
    next = cur->next;
    cur->next = prev;
    prev = cur;
    cur = next;
  }

  *head = prev;
}
