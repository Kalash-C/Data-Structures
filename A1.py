#Family Linked Lists 

class Node:  
    def __init__(self, name, age):  
        self.data = name, age; 
        self.previous = None;  
        self.next = None;  
          
class DoublyLinkedList:  
    #Head and Tail of the doubly linked list  
    def __init__(self):  
        self.head = None;  
        self.tail = None;  
          
     
    def addNode(self, name, age):             #adding a new node
        newNode = Node(name, age);            #creating a node           

          
        #If list is empty  
        if(self.head == None):  
            #Both head and tail will point to newNode  
            self.head = self.tail = newNode;  
            #head's previous will point to None  
            self.head.previous = None;  
            #tail's next will point to None
            self.tail.next = None;  
        else:  
            #newNode will be added after tail such that tail's next will point to newNode  
            self.tail.next = newNode;  
            #newNode's previous will point to tail  
            newNode.previous = self.tail;  
            #newNode will become new tail  
            self.tail = newNode;  
            #As it is last node, tail's next will point to None  
            self.tail.next = None;  
              
    #display() will print out the nodes of the list  
    def display(self):  
        #Node current will point to head  
        current = self.head;  
        if(self.head == None):  
            print("List is empty");  
            return;  
        print("Family Member Doubly linked list is: ");  
        while(current != None):   
            #Prints each node by incrementing pointer.  
            print(current.data),;  
            current = current.next;  
              
dList = DoublyLinkedList();  

a=int(input('Number of Family Members: '))
i=0
while i<a:
    b=input('Enter Family Member name: ')
    c=int(input('Enter Family Member age: '))
    dList.addNode(b, c)
    i=i+1

#Displays the nodes present in the list  
dList.display();  



#Bonus Question
#Ques: Try to find a way to link the family members' doubly-linked list based on their relationship. (is it possible?) 

#Ans: Yes, it is possibe to link the family members' doubly-linked list based on their relationship. One way to do this is to link the family members doubly-linked list is by sorting the doubly linked list according to age in decending order.By doing so we will get a doubly linked list in which older generation people will be close to head in double linked list and new generation people will be close to tail in doubly linked list.
