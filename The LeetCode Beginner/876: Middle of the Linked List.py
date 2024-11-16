"""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.


Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNodeHandler:
    def __init__(self):
        pass

    @staticmethod
    def create_linked_list(element: List[int]) -> ListNode | None:
        """
        Convierte una lista de Python en una lista enlazada.
        """
        if not element:
            return None

        head = ListNode(element[0])
        current = head
        for value in element[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    @staticmethod
    def linked_list_to_list(head):
        """
        Convierte una lista enlazada en una lista de Python.
        """
        elements = []
        current = head
        while current:
            elements.append(current.val)
            current = current.next
        return elements

    @staticmethod
    def print_linked_list(head):
        """
        Imprime la lista enlazada desde un nodo en formato amigable.
        """
        elements = ListNodeHandler.linked_list_to_list(head)
        print(" -> ".join(map(str, elements)) + " -> None")

    @staticmethod
    def length_of_linked_list(head):
        """
        Calcula la longitud de una lista enlazada.
        """
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length


def list_to_linked_list(elements):
    if not elements:
        return None

    # Crear el nodo inicial (cabeza de la lista enlazada)
    head = ListNode(elements[0])
    current = head

    # Iterar por los elementos restantes y enlazarlos
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# Ejemplo de uso:


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":
    # Crear una instancia del manejador
    handler = ListNodeHandler()

    # Crear una lista enlazada desde una lista de Python
    elements = [1, 2, 3, 4, 5, 6]
    linked_list = handler.create_linked_list(elements)

    # Imprimir la lista enlazada
    print("Lista enlazada original:")
    handler.print_linked_list(linked_list)

    # Llamar a la solución para encontrar el nodo medio
    solution = Solution()
    middle_node = solution.middleNode(linked_list)

    # Imprimir la lista enlazada desde el nodo medio
    print("Lista enlazada desde el nodo medio:")
    handler.print_linked_list(middle_node)

    # Calcular y mostrar la longitud de la lista enlazada
    print("Longitud de la lista enlazada:", handler.length_of_linked_list(linked_list))
