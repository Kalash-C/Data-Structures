#Qusetion 1

def printList(self):
  
    temp = self.head
  
    if self.head is not None:
        while(True):
  
            # Print nodes till we reach first node again
            print(temp.data, end=" ")
            temp = temp.next
            if (temp == self.head):
                print("The tansversing element has reached the first element")


#Question 2

#Answer 2
# Circular Linked Lists can be used to manage the computing resources of the computer.
# Data structures such as stacks and queues are implemented with the help of the circular linked lists.
# Circular Linked List is also used in the implementation of advanced data structures such as a Fibonacci Heap.
# It is also used in computer networking for token scheduling.

