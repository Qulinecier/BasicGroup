from itertools import permutations
class Aut:
    def __init__(self, list_elements):
        self.list_elem = list_elements
        self.aut = self.generate()
        self.size = len(self.aut)
    
    def bijective_fun(self, perm_elems):
        # Return a function f such that f(x) = perm[original_index_of(x)]
        def f(x, perm=perm_elems):
            index_x = self.list_elem.index(x)
            return perm[index_x]
        return f
    
    def check_hom(self, f):
        for i in self.list_elem:
            for j in self.list_elem:
                if f(i*j) != f(i)*f(j):
                    return False
        return True

    def generate(self):
        # Store a list of all permutations of elements in self.list_elem
        perms = list(permutations(self.list_elem))
        len_perms = len(perms)
        # Store aut as a list of all bijective functions f(x)
        aut = []
        for perm in perms:
            if self.check_hom(self.bijective_fun(perm)):
                aut.append(self.bijective_fun(perm))
        return aut
    
    
    def inn(self):
        inner_list = []
        def inner_perm(g, perm = self.list_elem):
            return [g*x*g.inverse() for x in perm]
        inner_perm_set = set([tuple(inner_perm(g)) for g in self.list_elem])
        for perm in inner_perm_set:
            perm_list = list(perm)
            inner_list.append(self.bijective_fun(perm_list))
        return inner_list
    
    def inner_size(self):
        return len(self.inn())
