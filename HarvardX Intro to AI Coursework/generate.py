import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        print(self.domains)
        input()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for var in self.domains:
            Set = set()
            for word in self.domains[var]:
                if len(word) != var.length:
                    Set.add(word)
            for element in Set:
                self.domains[var].remove(element)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        change = 0
        if self.crossword.overlaps[x, y] == None:
            if len(self.domains[y]) == 1 and x.length == y.length:
                for element in self.domains[y]:
                    temp = None
                    for value in self.domains[x]:
                        if element == value:
                            temp = value
                            break
                    if temp != None:
                        change = 1
                        self.domains[x].remove(temp)
                        
        else:
            Tuple = self.crossword.overlaps[x, y]
            Set = self.domains[x].copy()
            
            for element in self.domains[x]:
                for value in self.domains[y]:
                    if element != value and element[Tuple[0]] == value[Tuple[1]]:
                        Set.remove(element)
                        break
            for element in Set:
                change = 1
                self.domains[x].remove(element)
        if change == 1:
            return True
        else:
            return False
                    
                    
                    

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs == None:
            queue = []
            for x in self.domains.keys():
                for y in self.domains.keys():
                    if x != y:
                        queue.append((x, y))
        else:
            queue = arcs
        while len(queue) != 0:
            Element = queue.pop()
            Bool = self.revise(Element[0],Element[1])
            if Bool == True:
                for x in self.domains.keys():
                    for y in self.domains.keys():
                        if x != y and (x, y) not in queue and (x, y) != Element:
                            queue.append((x, y))

        for var in self.domains:
            if len(self.domains[var]) == 0:
                return False
        return True
                    
                    
        raise NotImplementedError

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        if len(self.domains) != len(assignment):
            return False
        for element in assignment.keys():
            if assignment[element] == None or assignment[element] == "":
                return False
        return True
        raise NotImplementedError

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        for variable in assignment:
            if variable.length != len(assignment[variable]):
                return False
            for variable2 in assignment:
                if variable != variable2:
                    if assignment[variable] == assignment[variable2]:
                        return False
            for variable3 in self.crossword.neighbors(variable):
                if assignment[variable][self.crossword.overlaps[variable, variable3][0]] != assignment[variable3][self.crossword.overlaps[variable, variable3][1]]:
                    return False
        return True
        raise NotImplementedError

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        counts = {}
        for word in self.domains[var]:
            count = 0
            for variable in self.crossword.neighbors(var):
                if variable not in assignment.keys():
                    for word2 in self.domains[variable]:
                        if word == word2 or word[self.crossword.overlaps[var, variable][0]] != word2[self.crossword.overlaps[var, variable][1]]:
                            count += 1
            counts.update({word : count})
        List = []
        for i in range(len(counts)):
            Min = None
            for element in counts:
                if Min == None or counts[element] < counts[Min]:
                    Min = element
            List.append(element)
            counts.pop(element)
        return List
            
        

        raise NotImplementedError

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        unassigned = []
        for key in self.domains:
            if key not in assignment:
                unassigned.append(key)
        best = [unassigned[0]]      
        for i in range(len(unassigned)-2):
            if len(self.domains[unassigned[i+1]]) < len(self.domains[unassigned[i]]):
                best = [unassigned[i+1]]
            elif len(self.domains[unassigned[i+1]]) == len(self.domains[unassigned[i]]):
                best.append(unassigned[i+1])
        if len(best) == 1:
            return best[0]
        else:
            bestest = best[0]
            for i in range(len(best)-2):
                if len(self.crossword.neighbors(best[i+1])) > len(self.crossword.neighbors(bestest)):
                    bestest = best[i+1]
            return bestest
        raise NotImplementedError

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            if self.consistent(assignment):
                return assignment
            else:
                return None
        var = self.select_unassigned_variable(assignment)
        order = self.order_domain_values(var, assignment)
        counter = 0
        assignment.update({var : order[counter]})
        while self.backtrack(assignment) == None:
            print(counter)
            if counter < len(order)-1:
                counter += 1
                assignment.update({var : order[counter]})    
            else:
                assignment.pop(var)
                return None
        return assignment
                
            
            
            
        raise NotImplementedError


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
