class Node:
    def __init__(self,x):
        self.left = None
        self.right = None
        self.val = x

class BinarySearchTree():
    def __init__(self):
        self.tree = None

    def insert(self,val):
        """
        二分探索木に要素を挿入

        Parameters
        ----------
        val : int
            挿入したい数字

        Returns
        -------
        None
        """

        if self.tree is None:
            self.tree = Node(val)
            return

        node = self.tree

        while True:
            if node.val <= val:
                if not node.left:
                    node.left = Node(val)
                    return
                else:
                    node = node.left

            if node.val > val:
                if not node.right:
                    node.right = Node(val)
                    return
                else:
                    node = node.right
        

    def find(self,val):
        """
        二分探索木から要素を検索

        Parameters
        ----------
        val : int
            検索したい数字

        Returns
        -------
        is_exist: bool
            存在するかどうか
        """ 
        if self.tree is None:
            return False

        node = self.tree

        while True:
            if node.val < val:
                if not node.left:
                    return False
                else:
                    node = node.left
            elif node.val > val:
                if not node.right:
                    return False
                else:
                    node = node.right
            else:
                return True

    # def delete(self, key):
    #     if self.tree is None:
    #         return None

    #     root = self.tree

    #     if key < root.val:
    #         root = root.left
    #     elif key > root.val:
    #         root = root.right
    #     else:
    #         # 子を持たない場合、自身をnullで置き換える
    #         if root.left is None and root.right is None:
    #             root = None
    #         # 1つの子を持つ場合、自身をその子で置き換える
    #         elif root.left is None or root.right is None:
    #             root = root.left or root.right            
    #         else:
    #             # 2つの子を持つ場合、削除する値の位置へ、次に大きい値を移動。
    #             root.val = self._successor(root)

    #     return root

    # def _successor(self, node):
    #     pre = node
    #     node = node.right
    #     while node.left:
    #         node = node.left
    #     return node.val

#################################################################
BST = BinarySearchTree()
BST.insert(5)
BST.insert(3)
BST.insert(20)
BST.insert(40)
BST.insert(4)
BST.insert(1)

# should return True
print(BST.find(3))
print(BST.find(5))
print(BST.find(40))

# should return False
print(BST.find(0))
print(BST.find(2))
print(BST.find(10))
print(BST.find(41))