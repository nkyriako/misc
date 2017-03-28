
import java.util.Iterator;
import java.util.NoSuchElementException;

class Queue <Item> implements Iterable <Item> {

   private class Node {
      Item item;
      Node next;
   }
   private Node head = null;
   private Node tail = null;

   public boolean isempty() {
	if(head == null && tail == null) {
		return true;
	} else {
		return false;
	}     

// throw new RuntimeException("Replace this with working code");
   }

   public void insert(Item newitem) {
	Node n = new Node();
	n.item = newitem;
	if(head == null && tail == null) {
		head = n;
		tail = n;
	} else {
	tail.next = n;
//	tail.next.item = newitem;
	tail = tail.next;
	System.out.println("inserting fr");
	}
      //throw new RuntimeException("Replace this with working code");
   }

   public Iterator <Item> iterator() {
      return new Itor ();
   }

   class Itor implements Iterator <Item> {
      Node current = head;
      public boolean hasNext() {
         return current != null;
      }
      public Item next() {
         if (! hasNext ()) throw new NoSuchElementException();
         Item result = current.item;
         current = current.next;
         return result;
      }
      public void remove() {
         throw new UnsupportedOperationException();
      }
   }

}
