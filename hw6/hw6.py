#Got help from 
#https://docs.python.org/2/tutorial/classes.html
#http://www.cs.uml.edu/~jlu1/doc/source/report/BinarySearchTree1.html
#http://stackoverflow.com/questions/5471731/in-order-successor-in-binary-search-tree
#http://www.algolist.net/Data_structures/Binary_search_tree/Removal
#https://docs.python.org/2/tutorial/inputoutput.html
#https://docs.python.org/2/library/stdtypes.html#set
#http://www.tutorialspoint.com/python/string_split.htm
import heapq
class Node:
	def __init__(self,key,value,parent=None,left=None,right=None): #Initializes the Node class
		self.key=key
		self.value=value
		self.parent=parent
		self.left=left
		self.right=right
class BSTree:
	def __init__(self):
		self.root=None
	def find(self,key,nd=0): #recursively finds the node with given key
		if nd==0:
			nd=self.root
		if nd is None or key == nd.key: #Return the node if its None or if its the one we're trying to find
			return nd
		elif key<nd.key:  #Otherwise recursively call on the left or right node, depending on if its greater than or less than the desired key
			return self.find(key,nd.left)
		else:
			return self.find(key,nd.right)
	def insert(self,key,value):
		if self.root is None: #If the tree is empty, just add this as the root
			self.root=Node(key,value)
			return
		curr_nd=self.root
		while curr_nd:
			if curr_nd.key==key: #if you find it, just update its value
				curr_nd.value+=value
				return True
			elif key<curr_nd.key: #if the key is less than current nodes key, navigate left
				if curr_nd.left:
					curr_nd=curr_nd.left
				else:
					curr_nd.left=Node(key,value,curr_nd)
					return True
			else:  #otherwise, navigate right
				if curr_nd.right:
					curr_nd=curr_nd.right
				else:
					curr_nd.right=Node(key,value,curr_nd)
					return True
	def successor(self,key):
		nd = self.find(key)
		if nd is None:
			return None
		if nd.right: #if it has a right child...
			nd=nd.right
			while nd.left: #the leftmost node of its right subtree is its successor
				nd=nd.left
			return nd
		else:
			while nd.parent: #otherwise, it's the first ancestor who has a left child in it's ancestry
				if nd is nd.parent.left:
					return nd.parent
				else:
					nd=nd.parent
		return nd
	def delete(self,key):
		nd=self.find(key)
		if nd is None:
			return False
		elif (nd.left is None) and (nd.right is None): #if it has no children, just delete it
			nd==None
			return True
		elif nd.left is None: #if it has a right child but no left child...
			ndright=nd.right
			if nd.parent:
				if nd.parent.left is nd: #if it's a left child...
					ndright.parent=nd.parent
					nd.parent.left=ndright
				else: #if it's a right child...
					ndright.parent=nd.parent
					nd.parent.right=ndright
				nd=None
				return True
		elif nd.right is None: #if it has a left child but no right child, basically same thing as above
			ndleft=nd.left
			if nd.parent:
				if nd.parent.left is nd: #if it's a left child...
					ndleft.parent=nd.parent
					nd.parent.left=ndleft
				else: #if it's a right child...
					ndleft.parent=nd.parent
					nd.parent.right=ndleft
				nd=None
				return True
		else: #if it has both children...
			succ=self.successor(nd.key) #Find it's successor and swap with it. Then delete the key you want to delete.
			nd.key=succ.key
			nd.value=succ.value
			if succ.parent:	
				if succ is succ.parent.left: 
					succ.parent.left = None
				else:
					succ.parent.right= None
	def inOrderTraversal(self,nd=0):
		if nd==0:
			nd=self.root
		if nd is None:
			return
		if nd.left: #Do left subtree
			self.inOrderTraversal(nd.left)
		print(nd.key)#Then the node
		if nd.right:#Then right subtree
			self.inOrderTraversal(nd.right)
	def doHeap(self,nd=0): #Basically just makes an array of tuples of values and keys and returns it
		self.lst=[]
		if nd==0:
			nd=self.root
		if nd is None:
			return
		if nd.left:
			self.doHeap(nd.left)
		self.lst=self.lst+[(nd.value,nd.key)]
		if nd.right:
			self.doHeap(nd.right)
		return self.lst

# bad=BSTree()
# good=BSTree()
# f=open('stopwords.txt','r')
# words = set([line.split('\n')[0] for line in f])
# g=open('finefoods_cleaned.txt','r')

# for line in g:
# 	#w=words in line
# 	w=line.split(' ')
# 	w.remove(w[0])
# 	w[len(w)-1]=w[len(w)-1].split('\n')[0]
# 	if int(line.split(': ')[0])<4: #bad reviews
# 		for x in w:
# 			if x not in words:
# 				bad.insert(x,1)
# 	else: #good reviews
# 		for x in w:
# 			if x not in words:
# 				good.insert(x,1)
# f.close()
# g.close()


# badlist=bad.doHeap()
# goodlist=good.doHeap()
# f=open('frequent.txt','w')
# f.write('Top 20 most frequent words in bad reviews: \n')
# twentybad=heapq.nlargest(20,badlist)
# for i in twentybad:
# 	f.write(str(i)+'\n')
# f.write('Top 20 most frequent words in good reviews: \n')
# twentygood=heapq.nlargest(20,goodlist)
# for i in twentygood:
# 	f.write(str(i)+'\n')	
# for q in twentybad:
# 	good.delete(q[1])
# newgoodlist=good.doHeap()
# f.write('New 20 most frequent in good reviews: \n')
# newtwentygood=heapq.nlargest(20,newgoodlist)
# for j in newtwentygood:
# 	f.write(str(j)+'\n')
# t=open('finds.txt','w')
# wordstofind=['asymptotic','binary','complexity','depth','mergesort','quicksort','structure','theta']
# for w in wordstofind:
# 	b=bad.find(w)
# 	g=good.find(w)
# 	t.write(w+': \n')
# 	if b:
# 		t.write('Bad review frequency: ' + str(b.value)+'\n')
# 	else:
# 		bad.insert(w,1)
# 		s=bad.successor(w)
# 		t.write('Key not found in bad reviews. Successor: ' + str(s.key) + ' with frequncy ' + str(s.value) + '\n')
# 	if g:
# 		t.write('Good review frequncy: ' + str(g.value)+'\n')
# 	else:
# 		good.insert(w,1)
# 		s=good.successor(w)
# 		t.write('Key not found in good reviews. Successor: ' + str(s.key) + ' with frequency ' + str(s.value) + '\n')
# t.close()
# f.close()
# g.close()