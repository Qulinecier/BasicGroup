class DirectProduct:
    def __init__(self, list_group):
        self.n = len(list_group)
        self.list_group = list(list_group)
    
    def __str__(self):
        string = "(" + str(self.list_group[0])
        for i in range(1,self.n, 1):
            string += ", "
            string += str(self.list_group[i])
        string += ")"
        return string
    
    def __mul__(self, other):
        if self.n == other.n:
            new_list = []
            for i in range(self.n):
                try:
                    product = self.list_group[i] * other.list_group[i]
                except Exception as e:
                    raise TypeError(f"Multiplication failed at index {i}: {e}")
                new_list.append(product)
            return DirectProduct(new_list)
        else:
            return ValueError("Not same group")

    def __repr__(self):
        string = "(" + str(self.list_group[0])
        for i in range(1,self.n, 1):
            string += ", "
            string += str(self.list_group[i])
        string += ")"
        return string
    
    def __eq__(self, other):
        if self.list_group == other.list_group:
            return True
        else:
            return False
        
    def __hash__(self):
        return hash(tuple(self.list_group))
    
    def inverse(self):
        inv_list = [item.inverse() for item in self.list_group]
        return DirectProduct(inv_list)