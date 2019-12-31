# Ishita Kumar
# Assignment 5
# Applied Algorithms 
# Implement a Binary Search Tree data structure as a class which supports the following queries. You can
# assume that all keys are integer numbers and there are no duplicates.
#  insert(key) { inserts key into the tree.
#  contains(key) { returns True if key is in the tree, otherwise False.
#  inorder() { prints elements of the tree inorder.
#  size() { returns the number of nodes in the tree.
#  smallest() { returns the smallest element in the tree.
#  largest() { returns the largest element in the tree.
#  successor(key) { returns the smallest element in the tree whose value is greater than key.
#  predecessor(key) { returns the largest element in the tree whose value is less than key.
# Discuss the worst-case time and space complexities of each of the queries.

class Total:
    # Total sum of inorder Constructor
    def __init__(self, val):

        self.total = val


class Node(object):
    # BST Class Cnstructor
    def __init__(self, key):

        self.key = key
        self.left = None
        self.right = None
        self.total = 0

    # Function to insert a key into the BST
    # Code Motivated by: CLRS page 294

    def insert(self, key):
        if self.key:
            if key < self.key:
                # Adding key to the left
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insert(key)
            elif key > self.key:
                # Adding key to the right
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insert(key)
        else:
            self.key = key

    # Function to check if a key is present in the 
    # Code Motivated by : CLRS page 290

    def contains(self, key):

        if key == self.key:
            return True
        elif key < self.key:
            if self.left is None:
                return False
            else:
                return self.left.contains(key)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(key)

    # Function to print in-order traversal of tree
    # Code Motivated by: CLRS page 288
    def inorder(self):
        # Traverse Left
        if self.left:
            self.left.inorder()
        print(self.key, end=" ")
        # Traverse Right
        if self.right:
            self.right.inorder()

    # Function gets the size of the BST
    # Code Motivated by: CLRS page 291
    def size(self):
        size = 0
        if self != None:
            size += 1
            if self.left != None:
                size += self.left.size()
            if self.right != None:
                size += self.right.size()
        return size

    # Function to find the MINIMIUM value of BST
    # Code Motivated by: CLRS page 291
    def smallest(self):

        if self.left:
            return self.left.smallest()
        else:
            return self.key

    # Function to find the MAXIMUM value of BST
    # Code Motivated by: CLRS page 292
    def largest(self):

        if self.right:
            return self.right.largest()
        else:
            return self.key

    # Function to find the successor node of key
    # Code Motivated by: CLRS page 292
    def successor(self, key):

        successor = None
        while self != None:
            if self.key > key:
                # Set the left subtree
                successor = self
                self = self.left
            else:
                # Set the right subtree
                self = self.right
        return successor.key

    # Function to find the predecessor node of given key
    # Code Motivated by: CLRS page 292
    def predecessor(self, key):

        predecessor = None
        while self != None:
            if self.key < key:
                # Set the right subtree
                predecessor = self
                self = self.right
            else:
                self = self.left
        return predecessor.key

    # Function that returns sum of all the nodes greater than the key value node
    # Code Motivated by: https://www.geeksforgeeks.org/transform-bst-sum-tree/
    def greaterSumTree(self, root, sum):

        if root == None:
            return
        self.greaterSumTree(root.right, sum)
        prev = root.key
        root.key = sum.total
        sum.total = sum.total + prev
        self.greaterSumTree(root.left, sum)

# Main function
def main():
    # Initializing the root node
    node = Node(5)
    #  Inserting into tree
    node.insert(10)
    node.insert(15)
    node.insert(18)
    node.insert(20)
    node.insert(21)
    node.insert(7)
    node.insert(12)
    print("Nodes inserted are:\n")
    node.inorder()
    print("\n##### Binary Search Tree Functions ######")
    # Contains key Function
    print("\nContains(7)", node.contains(7))
    print("\nContains(100)", node.contains(100))
    # Size of BST Function
    print("\nSize of Binary Search Tree is:", node.size())
    # Smallest node in BST
    print("\nThe smallest node in Binary search Tree is:", node.smallest())
    # Largest node in BST
    print("\nThe Largest node in Binary search Tree is:", node.largest())
    # Successror of Key in BST
    print("\nThe successor of Node 12 is:", node.successor(12))
    # Predecessor of Key in BST
    print("\nThe predecessor of Node 18 is:", node.predecessor(18))
    print('\nInorder Traversal of Binary Search Tree():')
    node.inorder()
    # Object instance for total
    gstTotalValue = Total(0)
    #  Function for greaterSumTree
    node.greaterSumTree(node, gstTotalValue)
    print("\nInorder traversal of greaterSumTree()")
    node.inorder()


if __name__ == '__main__':
    main()
