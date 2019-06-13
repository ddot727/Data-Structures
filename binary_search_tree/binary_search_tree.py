class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
        # Dont forget to wrap the value in a node
        # 1. compare the element against the current node's value
        # 2. based on the result of the comparison, go left or right
        # 3. if we find an empty spot, park the value there
        # 4. otherwise, go back to step 1

        # What is the base case?
        # base case: we've found an empty spot where we can add the value
        if value < self.value:
            # if value is less, we go left
            # if there isnot left child, we can park the node here
            if not self.left:
                self.left = BinarySearchTree(value)
            # recure on the left child
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        pass
        # searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not
        # 1. compare target to current node
        # 2. if matched, return true
        # 3. if not matched, go the child elements and compare target
        # 4. keep going until matched
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                if self.left.value == target:
                    return True
                else:
                    return self.left.contains(target)
        elif target >= self.value:
            if self.right:
                if self.right.value == target:
                    return True
                else:
                    return self.right.contains(target)
        else:
            return False

    def get_max(self):
        pass
        # returns the maximum value in the binary search tree

    def for_each(self, cb):
        pass
        # performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work
