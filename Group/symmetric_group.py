class Sym:
    def __init__(self, list, n, cycles = True):
        self.n = n
        if cycles:
            self.originlist = list
            self.perlist = [self.initial_permute(i) for i in range(1, n+1, 1)]
        else:
            self.perlist = list
        self.list = self.disjoint()
    
    def __str__(self):
        string = ""
        for item in self.list:
            if len(item) != 1:
                string += str(item)
        if string == "":
            string = "e"
        return string
    
    def __eq__(self, other):
        if isinstance(other, Sym):
            if self.n != other.n:
                return ValueError("Not same Sn.")
            else:
                if self.perlist == other.perlist:
                    return True
                else:
                    return False
        else:
            return TypeError("Not in symmetric group.")
    
    def __hash__(self):
        return hash((tuple(self.perlist), self.n))

    def initial_permute(self, number):
        num = number
        cycle_list = self.originlist.copy()
        cycle_list.reverse()
        for cycle in cycle_list:
            if num in cycle:
                index = cycle.index(num)
                if index == len(cycle)-1:
                    num = cycle[0]
                else:
                    num = cycle[index + 1]
        return num
    def permute(self, number):
        return self.perlist[number-1]
    def inverse_permute(self, number, cycle):
        return self.perlist.index(number) + 1
    def new_num(self, list):
        for i in range(1, self.n+1, 1):
            b = True
            for item in list:
                if i in item:
                    b = False
            if b:
                return True, i
        return False, 0 
    def __mul__(self, other):
        if isinstance(other, Sym):
            if self.n == other.n:
                list = []
                b, num = self.new_num(list)
                while b:
                    new_cycle = [num]
                    new_permute = self.permute(other.permute(num))
                    while new_permute != num:
                        new_cycle.append(new_permute)
                        new_permute = self.permute(other.permute(new_permute))
                    list.append(tuple(new_cycle))
                    b, num = self.new_num(list)
                return Sym(list, self.n)
            ValueError("n not equal")
        TypeError("not Sym")
    def disjoint(self):
        list = []
        b, num = self.new_num(list)
        while b:
            new_cycle = [num]
            new_permute = self.permute(num)
            while new_permute != num:
                new_cycle.append(new_permute)
                new_permute = self.permute(new_permute)
            list.append(tuple(new_cycle))
            b, num = self.new_num(list)
        return list
    def inverse(self):
        list = []
        for cycle in self.list:
            if len(cycle) != 1:
                num = cycle[0]
                new_cycle = [num]
                new_inverse = self.inverse_permute(num, cycle)
                while new_inverse != num:
                    new_cycle.append(new_inverse)
                    new_inverse = self.inverse_permute(new_inverse, cycle)
                list.append(tuple(new_cycle))
        return Sym(list, self.n)
    def conjugate(self, other):
        if isinstance(other, Sym):
            if self.n == other.n:
                return other * self * other.inverse()
            else:
                ValueError("n not equal")
        else:
            TypeError("Not Sn")
    def iseven(self):
        prod = 1
        for cycle in self.list:
            if len(cycle) % 2 == 0:
                prod *= -1
        if prod == -1:
            return False
        else:
            return True