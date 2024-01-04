import numpy as np
from copy import deepcopy


def cost_aux(a):
    return a.size - len(np.unique(a))

def rand2rows(mask, col, n):
    while True:
        i1, i2 = np.random.randint(n), np.random.randint(n)
        if i1 != i2 and not mask[i1, col] and not mask[i2, col]:
            break
    return i1, i2

class Sudoku:
    def __init__(self, init, r=None, seed=None):
        if not isinstance(init, (int, Sudoku)):
            raise Exception('provide a valid argument')
        
        if seed is not None:
            np.random.seed(seed)
            
        if isinstance(init, int):
            if r is not None:
                raise Exception('need a valid puzzle first')
            n = init
            if (np.ceil(np.sqrt(n)) != np.floor(np.sqrt(n))):
                raise Exception('provide a perfect square')
            self.table = (np.ones((n,n), dtype=int)*np.array([i for i in range(n)])).T
            self.n = n
            self.sn = int(np.sqrt(n))
            self.mask = np.zeros((n,n), dtype=bool) 
        
        else: 
            if r is None:
                raise Exception('provide a probability')
            if init.cost() != 0:
                raise Exception('this Sudoku is not valid')
            n = init.n
            self.n = n
            self.sn = int(np.sqrt(n))
            self.table = init.table.copy()
            
            table = self.table
            mask = np.random.random(size=(n,n)) < r 
            
            self.mask = mask
            
            for j in range(n):
                if sum(mask[:,j]) == n-1: 
                    mask[:,j] = True
                    
            for j in range(n): 
                mj = ~mask[:,j]
                v = table[mj, j]
                np.random.shuffle(v)
                table[mj, j] = v
                     
    def init_config(self):
        n, table, mask = self.n, self.table, self.mask
        for j in range(n):
            mj = ~mask[:,j]
            v = table[mj, j]
            np.random.shuffle(v)
            table[mj, j] = v
        
    def __repr__(self):
        s = ""
        n, sn, table = self.n, self.sn, self.table
        pad = len(str(n-1)) 
        for i in range(n):
            if i > 0 and i % sn == 0:
                for j in range(n):
                    if j > 0 and j % sn == 0:
                        s += "+-"
                    s += "-" * (pad+1)
                s += "\n"
            for j in range(n):
                if j > 0 and j % sn == 0:
                    s += "| "
                s += "{:>{width}} ".format(table[i,j], width=pad)
            s += "\n"
        return "Sudoku:\n" + s
    
    def showpuzzle(self):
        s = ""
        n, sn, table, mask = self.n, self.sn, self.table, self.mask
        pad = int(np.ceil(np.log10(n-1)))
        for i in range(n):
            if i > 0 and i % sn == 0:
                for j in range(n):
                    if j > 0 and j % sn == 0:
                        s += "+-"
                    s += "-" * (pad+1)
                s += "\n"
            for j in range(n):
                if j > 0 and j % sn == 0:
                    s += "| "
                if mask[i,j]:
                    v = table[i,j]
                else:
                    v = '?'
                s += "{:>{width}} ".format(v, width=pad)
            s += "\n"
        print("Sudoku puzzle:\n" + s)
    
    def display(self):
        pass
    
    def cost(self):
        n = self.n
        table = self.table
        c = 0
        for row in range(n):
            c += cost_aux(table[row,:])
            
        sn = int(np.sqrt(n))
        for si in range(0,n,sn):
            for sj in range(0,n,sn):
                c += cost_aux(table[si:si+sn, sj:sj+sn])
            
        return c
    
    def propose_move(self):
        n, mask = self.n, self.mask
        
        while True:
            c = np.random.randint(0, n) 
            if mask[:, c].sum() < n: 
                break
        r1, r2 = rand2rows(mask, c, n) 
        
        return (c, r1, r2)
    
    def compute_delta_cost(self, move):
        c, i, j = move
        table = self.table
        n = self.n
        sn = int(np.sqrt(n))
        
        q1 = ((i//sn), (c//sn))
        q2 = ((j//sn), (c//sn))

        r1 = table[i, :]
        r2 = table[j, :]
        
        c_old1 = cost_aux(r1)
        c_old2 = cost_aux(r2)
        
        if q1 == q2:
            cost_old = c_old1 + c_old2
        
            table[[i,j],c] = table[[j,i],c]
        
            c_new1 = cost_aux(r1)
            c_new2 = cost_aux(r2)
            cost_new = c_new1 + c_new2
            
        else: 
            c_q1_old = cost_aux(table[q1[0]*sn:q1[0]*sn+sn, q1[1]*sn:q1[1]*sn+sn])
            c_q2_old = cost_aux(table[q2[0]*sn:q2[0]*sn+sn, q2[1]*sn:q2[1]*sn+sn])
            cost_old = c_old1 + c_old2 + c_q1_old + c_q2_old
        
            table[[i,j],c] = table[[j,i],c]
        
            c_new1 = cost_aux(r1)
            c_new2 = cost_aux(r2)
            c_q1_new = cost_aux(table[q1[0]*sn:q1[0]*sn+sn, q1[1]*sn:q1[1]*sn+sn])
            c_q2_new = cost_aux(table[q2[0]*sn:q2[0]*sn+sn, q2[1]*sn:q2[1]*sn+sn])
            cost_new = c_new1 + c_new2 + c_q1_new + c_q2_new 
            
        delta_c = cost_new - cost_old
        
        table[[i,j],c] = table[[j,i],c] 
        
        return delta_c        
        
    def accept_move(self, move):
        c, i, j = move
        table = self.table
        
        aux = table[i, c]
        table[i, c] = table[j, c]
        table[j, c] = aux
        
    def copy(self):
        return deepcopy(self)
