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
        self.generate_cells()
        
    def generate_cells(self): # generating random 2D array with values between 1 and 100, and then changing each cell to a 0 or 1 depending on if it's less than the cutoff value
        self.cells = [[random.randint(1, 100) for i in range(self.width)] for j in range(self.height)]
        for c in range(self.height):
                for r in range(self.width):
                    if self.cells[r][c] < self.cutoff: self.cells[r][c] = 0
                    else: self.cells[r][c] = 1
        

    def output_cells(self):
        for k in range(self.cells.__len__()):
            for i in range(self.cells[k].__len__()):
                
                if(self.cells[i][k]) == 1:
                    print(" # ", end="")
                else:
                    print(" . ", end="")
            print("")
    
    def search_adjacent_cells(self, row, column):
        delta_r = [-1, -1, -1, 0, 0, 1, 1, 1]
        delta_c = [-1, 0, 1, -1, 1, -1, 0, 1]
        length = delta_r.__len__()
        count = 0
        for k in range(length):
            
            if(self.cells[row+delta_r[k]][column+delta_c[k]] == 1):
                count += 1
        
        return count

    def iterate_cells(self):
        for column in range(self.height):
            for row in range(self.width):
                if(row!=0 and row!=self.width-1 and column!=0 and column!=self.height-1):
                    if(self.search_adjacent_cells(row, column) >= 4):
                        self.cells[row][column] = 1
                    else:
                        self.cells[row][column] = 0
                        
                    
    def raw_output(self):
        for k in range(self.cells.__len__()):
            for i in range(self.cells[k].__len__()):
                print(" " + self.cells[i][k].__str__() + " ", end="")
            print("")

            

                    
        



cell_automata = BasicCA(70, 70, 67)
cell_automata.output_cells()
print(" \n \n \n \n \n")

cell_automata.iterate_cells()
cell_automata.iterate_cells()
cell_automata.iterate_cells()
cell_automata.iterate_cells()


cell_automata.output_cells()


# cell_automata.output_cells()