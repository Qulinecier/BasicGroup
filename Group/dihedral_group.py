class Dihedral:
    def __init__(self, string, n):
        self.string = string
        self.n = n
        r_id = "r" * n
        s_id = "ss"
        if not all(c in "rs" for c in self.string):
            return TypeError("Error: The input string should only contain 'r' and 's'.")
        while "sr" in self.string:
            self.string = self.string.replace("sr", "r" * (self.n-1) + "s")
        while r_id in self.string:
            self.string = self.string.replace(r_id, "")
        while s_id in self.string:
            self.string = self.string.replace(s_id, "")
    
    def __mul__(self, other):
        if isinstance(other, Dihedral):
            if self.n == other.n:
                string1 = self.string + other.string
                return Dihedral(string1, self.n)
            ValueError("n not equal")
        TypeError("not Dihedral")

    def __str__(self):
        if self.string == "":
            return "e"
        return self.string

    def __repr__(self):
        if self.string == "":
            return "e"
        return self.string

    def __eq__(self, other):
        if isinstance(other, Dihedral):
            if self.n != other.n:
                return ValueError("Not same D2n.")
            else:
                if self.string == other.string:
                    return True
                else:
                    return False
        else:
            return TypeError("Not in Dihedral group.")
    
    def __hash__(self):
        return hash((tuple(self.string), self.n))
    
    def inverse(self):
        new_str = ""
        for item in self.string[-1::-1]:
            if item == "r":
                new_str += "r" * (self.n - 1)
            elif item == "s":
                new_str += "s"
        return Dihedral(new_str, self.n)
    
    def __pow__(self, num):
        if num == 0:
            return Dihedral("", self.n)
        elif num >= 1:
            new = Dihedral("", self.n)
            for _ in range(0, num, 1):
                new = new * self
            return new
        elif num <= -1:
            abs_num = -num
            new = Dihedral("", self.n)
            for _ in range(0, abs_num, 1):
                new = new * self.inverse()
            return new
        else:
            TypeError("num is an integer")
    
    def conjugate(self, other):
        if isinstance(other, Dihedral):
            return other*self*other.inverse()
        else:
            TypeError("Not Dihedral")