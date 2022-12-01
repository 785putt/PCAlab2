
with open("users1000.txt") as f: 
    content = f.readlines()
    contents = ''.join(content)
    #Appending turned-int element into list
    password_in = []
    username_in = []
    abc = []
    #a = Node(username_in, password_in)
    for l in content:
        for i in l.split():
            if i.isdigit():
                password_in.append(int(i))
                #print(i, end="")
            if i.isalpha():
                username_in.append(str(i))

    for k in range(300):
        a = tuple([username_in[k], password_in[k]])
        #print(a)

class BST: 
    def __init__(self, new_node): 
        self.new_node = new_node
        #self.username_in = new_node[0] #Username
        #self.password_in = new_node[1] #Password
        self.left = None 
        self.right = None 
    
    def insert_node(self, new_node):
        if new_node[1] == self.new_node:
            return # node already exist
        
        if new_node[1] < self.new_node[1]:
            if self.left:
                self.left.insert_node(new_node)
            else:
                self.left = BST(new_node)
        else:
            if self.right:
                self.right.insert_node(new_node)
            else:
                self.right = BST(new_node)
    # Prioritize this
    def findval(self, new_node): 
        if new_node[1] < self.new_node[1]:
            if self.left is None:
                print("Users "+str(new_node[0])+" is not Found")
            print(self.left.findval(new_node[1]))
        elif new_node[1] > self.new_node[1]:
            if self.right is None:
                print("Users "+str(new_node[0])+" is not Found")
            print(self.right.findval(new_node[1]))
        else:
            print(str(self.new_node[0]) + " is found")
 
    def delete_Node(self, root, key):
    # if root doesn't exist, just return it
        if not root: 
            return root
        # Find the node in the left subtree	if key value is less than root value
        if root.new_node > key: 
            root.left = self.delete_Node(root.left, key)
        # Find the node in right subtree if key value is greater than root value, 
        elif root.new_node < key: 
            root.right= self.delete_Node(root.right, key)
        # Delete the node if root.value == key
        else: 
        # If there is no right children delete the node and new root would be root.left
            if not root.right:
                return root.left
        # If there is no left children delete the node and new root would be root.right	
            if not root.left:
                return root.right
    # If both left and right children exist in the node replace its value with 
    # the minmimum value in the right subtree. Now delete that minimum node
    # in the right subtree
            temp_val = root.right
            mini_val = temp_val.new_node
            while temp_val.left:
                temp_val = temp_val.left
                mini_val = temp_val.new_node
    # Delete the minimum node in right subtree
            root.right = self.deleteNode(root.right,root.new_node)
        return root

 
    def is_empty(self): 
        # your code here 
        pass
 
    def preorder(self): 
        print(self.new_node[0], self.new_node[1], end=', ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
 
    def inorder(self): 
        if self.left is not None:
            self.left.inorder()
        print(self.new_node[0], self.new_node[1], end=', ')
        if self.right is not None:
            self.right.inorder() 
 
    def postorder(self): 
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.new_node[0], self.new_node[1], end=', ')

    def get_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.username_in, current.password_in
    
    def get_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.username_in, current.password_in
 
    def print(self): 
        if self.left:
            self.left.print()
        print(self.new_node)
        if self.right:
            self.right.print()

        
tree = BST(new_node=('snickers', 93352))
print("Print out all nodes in BST:")
tree.insert_node(('sasha', 34920))
tree.insert_node(('kiki', 71649))
tree.insert_node(('garfield', 89124))
tree.insert_node(('sam', 16202))
tree.insert_node(('cat', 46891))
tree.insert_node(('lucy', 38456))
tree.insert_node(('marie', 85557))
tree.insert_node(('mimi', 33954))
tree.insert_node(('diana', 97969))
tree.insert_node(('muschi', 83318))
tree.insert_node(('sugar', 74045))
tree.insert_node(('millie', 25074))
tree.insert_node(('ziggy', 65274))
tree.print()
print("\nFinding user name & password:",str(tree.new_node[0]),str(tree.new_node[1]))
tree.findval(('snickers', 93352))
print()
# print("Preorder tranverse:"), tree.preorder()
print("Inorder tranverse:"), tree.inorder()
#print("Postorder tranverse:"), tree.postorder

print("\nLogin attempts system (as stated in canvas)")
attempts = 0   # Example: Setting garfield 89124 as correct username/password for this case
while attempts < 3:
    i1 = input('Enter username: ')
    i2 = int(input('Enter password: '))
    final = tuple([i1, i2])
    if final == ('garfield', 89124):
        print("Login with correct username/password!")
        break
    else:
        print("Waiii missed!!")
        attempts += 1   
        continue

# https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm
# https://blog.boot.dev/computer-science/binary-search-tree-in-python/
# https://algorithmtutor.com/Data-Structures/Tree/Binary-Search-Trees/
# https://www.digitalocean.com/community/tutorials/binary-search-tree-bst-search-insert-remove