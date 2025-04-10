class Cyclic:
    def __init__(self, i, n):
        self.n = n
        self.index = i % n
    
    def __str__(self):
        if self.index == 0:
            return "e"
        else:
            return "g^" + str(self.index)

    def __repr__(self):
        if self.index == 0:
            return "e"
        else:
            return "g^" + str(self.index)

    def __mul__(self, other):
        if self.n == other.n:
            return Cyclic(self.index + other.index, self.n)
        else:
            return ValueError("Not same group")
    
    def __eq__(self, other):
        if isinstance(other, Cyclic):
            if self.n == other.n:
                return self.index == other.index
            else:
                return ValueError("Not same group")
        else:
            return TypeError("Not in cyclic group")
    
    def __hash__(self):
        return hash((self.index, self.n))
    
    def inverse(self):
        return Cyclic(-self.index, self.n)