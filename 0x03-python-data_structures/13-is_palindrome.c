#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *next, *prev = NULL, *fast = *head, *slow = *head;

	if (!*head)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	if (fast)
		slow = slow->next;
	while (prev && slow)
	{
		if (slow->n != prev->n)
			return (0);

		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}
