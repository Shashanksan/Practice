# # You are using Python
# class Node:
#     def __intit__(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# class DoublyLinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail =None
#     def insert_front(self,value):
#         new_node=node(value)
#         if self.head is None:
#             self.head = self.tail= new_node
#         else:
#                 new_node.next=self.head
#                 self.head.prec=new_node
#                 self.head=new_node
#         print(f"Inserted {value} at the front.")
#     def insert_end(self,value):
#         new_node=Node(value)
            
#         if self.tail is None:
#                 self.head =self.tail = new_node
#         else:
#                 self.tail.next=new_node
#                 new_node.prev =self.tail
#                 self.tail = new_node
#         print(f"Inserted {value} at the end.")
#     def delete_front(self):
#         if self.head is None:
#             print("List is empty .Cannot delete from front.")
#             return 
#         deleted = self.head.next
#         if self.head == self.tail:
#             self.head = self.tail = None
#         else:
#             self.head = self.head.next
#             self.head.prev =None
#         print(f"Deleted {deleted} from front.")
#     def delete_end(self):
#         if self.tail is None:
#             print("List is empty. Cannot delete from end.")
#             return 
#         deleted= self.tail.data
#         if self.head == self.tail:
#             self.head= self.tail= None
#         else:
#             self.tail = self.tail.prev
#             self.next=None
#         print(f"Deleted{deleted} from end.")
        
#     def display_forward(self):
#         if self.head is None:
#             print("List is empty.")
#             return
#         print("List (forward): ",end="")
#         temp=self.head
#         while temp:
#             print(temp_data,end="")
#             temp=temp.next
#         print
#     def display_backward(self):
#         if self.tail is None:
#             print("List is empty.")
#             return
#         print("List (backward): ",end="")
#         temp=self.tail
#         while temp:
#             print(temp_data,end="")
#             temp=temp.prev
#         print()
# dll =DoublyLinkedList()
# while True:
#         try:
#             inp =input().split()
#             if not inp:
#                 continue
#             choice = int(inp[0])
#             if choice ==1:
#                 dll.insert_front(int(inp[1]))
#             elif choice ==2:
#                 dll.insert_end(int(inp[1]))
#             elif choice ==3:
#                 dll.delete_front()
#             elif choice ==4:
#                 dll.delete_end()
#             elif choice ==5:
#                 dll.display_forward()
#             elif choice ==6:
#                 dll.display_backward()
#             elif choice ==7:
#                 break
#             elif choice ==8:
#                 print("invalid Choice")
#         except EOFError:
#             break
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        print(f"Inserted {value} at the front.")

    def insert_end(self, value):
        new_node = Node(value)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        print(f"Inserted {value} at the end.")

    def delete_front(self):
        if self.head is None:
            print("List is empty. Cannot delete from front.")
            return

        deleted = self.head.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        print(f"Deleted {deleted} from front.")

    def delete_end(self):
        if self.tail is None:
            print("List is empty. Cannot delete from end.")
            return

        deleted = self.tail.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        print(f"Deleted {deleted} from end.")

    def display_forward(self):
        if self.head is None:
            print("List is empty.")
            return

        print("List (forward): ", end="")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def display_backward(self):
        if self.tail is None:
            print("List is empty.")
            return

        print("List (backward): ", end="")
        temp = self.tail
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()


dll = DoublyLinkedList()

while True:
    try:
        inp = input().split()

        if not inp:
            continue

        choice = int(inp[0])

        if choice == 1:
            dll.insert_front(int(inp[1]))

        elif choice == 2:
            dll.insert_end(int(inp[1]))

        elif choice == 3:
            dll.delete_front()

        elif choice == 4:
            dll.delete_end()

        elif choice == 5:
            dll.display_forward()

        elif choice == 6:
            dll.display_backward()

        elif choice == 7:
            break

    except EOFError:
        break
