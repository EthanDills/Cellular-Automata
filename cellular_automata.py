'''
- generate random 2D Array (boolean values)

- iterate through the entire array a certain # of times, changing each cell depending on how many surrounding cells are empty/filled

- output
'''

import random

class BasicCA:
    
    def __init__(self, width, height, cutoff):
        self.width = int(width)
        self.height = int(height)
        self.cutoff = int(cutoff)
        self.cells = [[]]
        
    def generate_cells(self): # generating random 2D array
        self.cells = [[random.randint(1, 100) for i in range(self.width)] for j in range(self.height)]
        for c in range(self.height):
                for r in range(self.width):
                    if self.cells[r][c] < self.cutoff: self.cells[r][c] = 0
                    else: self.cells[r][c] = 1

    def output_cells(self): # outputing array
        for k in range(self.cells.__len__()):
            for i in range(self.cells[k].__len__()):
                
                if(self.cells[i][k]) == 1:
                    print(" # ", end="")
                else:
                    print(" . ", end="")
            print("")


cell_automata = BasicCA(60, 60, 57)
cell_automata.generate_cells()
cell_automata.output_cells()