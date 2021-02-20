public /**
* Definition for singly-linked list.
* public class ListNode {
*     int val;
*     ListNode next;
*     ListNode() {}
*     ListNode(int val) { this.val = val; }
*     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
* }
*/
class Solution {
   public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
       ListNode n = l1;
       int count = 0;
       while (n != null) {
           count++;
           n = n.next;
       }
       int count2 = 0;
       n = l2;
       while (n != null) {
           count2++;
           n = n.next;
       }
       int c = Math.max(count, count2);
       int[] list1 = new int[c];
       int[] list2 = new int[c];
       n = l1;
       for (int i=c-1-(c-count); i>= 0; i--) {
           list1[i] = n.val;
           n = n.next;
       }
       n = l2;
       for (int i=c-1-(c-count2); i>= 0; i--) {
           list2[i] = n.val;
           n = n.next;
       }
       int value = 0;
       n = new ListNode(0);
       for (int i=0; i < c; i++) {
           value += list1[i] + list2[i];
           n.val = value % 10;
           value /= 10;
           ListNode head = new ListNode(value);
           
           head.next = n;
           n = head;
       }
       
       return n.val == 0 ? n.next : n;
   }
}class 445_add_two_numbers_2 {
    
}
