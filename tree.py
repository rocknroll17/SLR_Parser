#Description: This file contains the Tree class which is used to create a tree data structure.
#and print the tree in a readable format.
class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None
        self.level = None
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)
    
    def add_child(self, child, index=None):
        if index is not None:
            self.children.insert(index, child)
        else:
            self.children.append(child)
        child.parent = self

    def add_parent(self, parent):
        self.parent = parent
    
    def get_children(self):
        return self.children
    
    def get_parent(self):
        return self.parent
    
    #set parent of the children recursively
    def set_parent(self):
        for i in self.children:
            i.parent = self
            i.set_parent()

    #set level of the children recursively
    def set_level(self, level):
        self.level = level
        for i in self.children:
            i.set_level(level+1)

    def print_tree(self, indent=0):
        indentation = ""
        me = self
        parent = self.parent
        for i in range(indent):
            #If the self is not the last child of the parent, add "├───" to the indentation
            if i == 0 and self.parent.children.index(self) < len(self.parent.children) - 1:
                indentation = "├───" + indentation
            #If the self is the last child of the parent, add "└───" to the indentation
            elif i == 0  and self.parent.children.index(self) == len(self.parent.children) - 1:
                indentation = "└───" + indentation
            #If the parent's parent has more children, add "│   " to the indentation
            elif parent.children.index(me) < len(parent.children) - 1:
                indentation = "│   " + indentation
            elif parent.children.index(me) == len(parent.children) - 1:
                indentation = "    " + indentation
            else:
                indentation = "    " + indentation
            #follow up to the parent
            me = parent
            parent = parent.parent
        else:
            print(indentation + str(self.value))
        #print children recursively
        for child in self.children:
            child.print_tree(indent + 1)