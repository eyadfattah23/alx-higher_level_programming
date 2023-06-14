#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	size_t len;
	size_t i = 0;
	size_t j;
	int *array;
	listint_t *c_node = *head;

	if (!*head)
		return (1);

	for (len = 0; c_node; len++)
		c_node = c_node->next;

	c_node = *head;
	array = (int *)malloc(sizeof(int) * len);
	if (!array)
		return (0);

	while (c_node)
	{
		array[i++] = c_node->n;
		c_node = c_node->next;
	}
	i--;
	for (j = 0; j < i; j++, i--)
	{
		if (array[j] != array[i])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
