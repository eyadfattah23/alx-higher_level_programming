#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: hed of the list
 * @number: number in the new node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *c_node = *head;
	listint_t *p_node;
	listint_t *n_node = malloc(sizeof(listint_t));

	if (!n_node)
		return NULL;

	if (!*head)
	{
		n_node = add_nodeint_end(head, number);
		return (n_node);
	}

	n_node->n = number;
	n_node->next = NULL;
	
	while (c_node)
	{
		if (((c_node->n <= number) && (c_node->next->n >= number)) || (c_node->n <= number && !(c_node->next)))
		{
			n_node->next = c_node->next;
			c_node->next = n_node;
			break;
		}
		if (!(c_node->next) && (c_node->n >= number))
		{
			
		}
		
		c_node = c_node->next;
	}
	return (n_node);
}
