#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: hed of the list
 * @number: number in the new node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p_node;
	listint_t *n_node = malloc(sizeof(listint_t));

	if (!n_node)
		return (NULL);

	if (!*head)
	{
		n_node = add_nodeint_end(head, number);
		return (n_node);
	}
	p_node = *head;
	n_node->n = number;
	n_node->next = NULL;

	if (p_node->n >= number)
	{
		n_node->next = p_node;
		*head = n_node;
		return (n_node);
	}
	
	for (; p_node->next; p_node = p_node->next)
	{
		if (p_node->next->n >= number)
		{
			n_node->next = p_node->next;
			p_node->next = n_node;
			return (n_node);
		}
	}
	if (p_node->n >= number)
	{
		n_node->next = *head;
		*head = n_node;
		return (n_node);
	}
	else
	{
		p_node->next = n_node;
		return (n_node);
	}
}
