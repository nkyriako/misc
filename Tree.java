import static java.lang.System.*;

class Tree {

    private class Node {
        String key;
        Queue<Integer> value;	
        Node left = null;		
        Node right = null;
    }
    private Node root;
    public int nNodes = 0;
   // private Node yah = root;

    private void debugHelper(Node tree, int depth) {
        // Your code here might be recursive
        throw new UnsupportedOperationException();
    }

    private void outputHelper(Node tree) {
        // Your code here might be recursive
        throw new UnsupportedOperationException();
    }
    
	private int compare(String a, String b) {
		int comp = a.compareTo(b);
		if (comp < 0) {
			return 1;
		}else if (comp > 0) {
			return 2;
		} else {
			return 3;
		}
	}

    public void insert(String key, Integer linenum) {
        // Insert a word into the tree
	Node iNode = new Node();
	iNode.key = key;
	iNode.value = new Queue();
	iNode.value.insert(linenum);
	System.out.println(iNode.key);
	//iNode.left = null;
	//iNode.right = null;
	if(root == null) {
		root = iNode;
		System.out.println("OK");
		nNodes++;
	} else {
		Node yah = root;						//stands for: you are here
		Node parent;
		while(true){
			parent = yah;
		
			if(compare(iNode.key, yah.key) == 1) {			//iNode.key < yah.key
				yah = yah.left;
				if(yah == null) {
					parent.left = iNode;
					System.out.println("left");
					nNodes++;
					return;
				}
				
			} else if (compare(iNode.key, yah.key) == 2) {		//iNode.key > yah.key
				yah = yah.right;
				if(yah == null) {
					parent.right = iNode;
					System.out.println("right");

					nNodes++;
					return;
				}
			} else if (compare(iNode.key, yah.key) == 3) {		//iNode.key == yah.key
				yah.value.insert(linenum);
				System.out.println("add");
				return;
				//throw new UnsupportedOperationException();
			}
		} // end while loop
	} // end else
       // throw new UnsupportedOperationException();
    }

    public void debug() {
        // Show debug output of tree
       debugHelper(root, 0);
    }

    public void output() {
        // Show sorted words with lines where each word appears
        outputHelper(root);
    }

}
