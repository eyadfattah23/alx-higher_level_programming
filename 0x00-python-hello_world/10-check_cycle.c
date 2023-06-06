#include "lists.h"
#include "stdio.h"

/**
 * check_cycle - checks if there is a cycle in a linked list
 * @list: list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = NULL, *fast = NULL;

	fast = list;
	slow = list;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
