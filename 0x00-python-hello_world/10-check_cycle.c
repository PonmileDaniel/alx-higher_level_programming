#include "lists.h"

/**
 * check_cycle - check if the siingly linked list is a cycle
 * @n: pointer to the slow
 * @p: pointer to the fast
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *n;
	listint_t *p;

	n = list;
	p = list;

	while (n != NULL && p != NULL && p->next != NULL)
	{
		n = n->next;
		p = p->next->next;

		if (n == p)
		{
			return (1);
		}
	}
	return (0);
}
