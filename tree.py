class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None
        
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
    
    def print_tree_by_level(self):
        if not self:
            return
        
        current_level = [self]
        
        while current_level:
            next_level = []
            for node in current_level:
                print(node.value, end=" ")
                next_level.extend(node.get_children())
            print()
            current_level = next_level