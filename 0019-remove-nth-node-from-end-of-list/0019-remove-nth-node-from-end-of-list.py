class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a=[]
        a.append(head.val)
        while head.next:
            head=head.next
            a.append(head.val)
        a.pop(-n)
        new_Head=None
        for i in a:
            if new_Head is None:
                new_Head=ListNode(i)
                b=new_Head
            else:
                b.next=ListNode(i)
                b=b.next
        return new_Head