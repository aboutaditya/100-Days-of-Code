#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
    
        


# } Driver Code Ends
#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        mp=set()
        while head2:
            mp.add(head2.data)
            head2=head2.next
        c=0
        while head1:
            if x-(head1.data) in mp:
                c+=1
            head1=head1.next
        return c
        '''
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        '''

#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        
        n1=int(input())
        ll1 = LinkedList() # create a new linked list 'll1'.
        nodes_ll1 = list(map(int, input().strip().split()))
        for nodes in nodes_ll1:
            ll1.append(nodes)  # add to the end of the list
        
        n2=int(input())
        ll2=LinkedList()  #create a new linked list 'll1'.
        nodes_ll2 = list(map(int, input().strip().split()))
        for nodes in nodes_ll2:
            ll2.append(nodes)  # add to the end of the list
        
        x=int(input())
        
        
        print(Solution().countPair(ll1.head,ll2.head,n1,n2,x))


# } Driver Code Ends