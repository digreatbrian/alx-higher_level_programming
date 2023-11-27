#include "lists.h"

/**
   * check_cycle - checks if a linked list is a cycle
   * @list: first element in linked list / head
   * Return (1 or 0)
   */
int check_cycle(listint_t *list)
{
	int ret = 0;
	listint_t *first_node = list;
	listint_t *temp_node;
	
	temp_node = first_node;
	while (1)
	{
		temp_node = temp_node->next;
		
		if (temp_node == first_node)
		{
			/* this is a cycle linked list */
			ret = 1;
			break;
		}
		else if (!temp_node->next)
		{
			break;
		}
	}
	return (ret);
}
