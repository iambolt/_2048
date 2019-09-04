

# Directions
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}
import random

def merge(line):
    """ this function merges the
    tiles in the game 2048"""
    number_merge = []
    zero_shift = []
    result = []
    counter = 0
    cache = 0
    for idx in range(len(line)):
        number_merge.append(0)
    for val in line:
        if val != 0:
            zero_shift.append(val)
        else:
            counter+=1
    for idx in range(counter):
        zero_shift.append(0)
    for idx,val in enumerate(zero_shift):# this is where the merging happens
        if val == cache and val != 0:
            number_merge[idx-1] = 2*val
            number_merge[idx] = 0
            cache = 0
        else:
            number_merge[idx] = val
            cache = val
    counter = 0
    for val in number_merge:
        if val != 0:
            result.append(val)
        else:

            counter += 1
    for idx in range(counter):
        result.append(0)
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()
        self._initial_tiles_dict = {UP :[],DOWN:[],LEFT :[],RIGHT:[]}
        for col in range(self._grid_width):
            self._initial_tiles_dict[UP].append((0, col))
            self._initial_tiles_dict[DOWN].append((self._grid_height - 1, col))
        for row in range(self._grid_height):
            self._initial_tiles_dict[LEFT].append((row, 0))
            self._initial_tiles_dict[RIGHT].append((row, self._grid_width - 1))

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._initial_grid = [[0 for dummy_col in range(self.get_grid_width())] for dummy_row in range(self.get_grid_height()) ]
        for dummy_idx in range(2):
            self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """

        return "{}".format(self._initial_grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction in (UP, DOWN):
            num_steps = self.get_grid_height()
        elif direction in (LEFT, RIGHT):
            num_steps = self.get_grid_width()
        moved = False
        temp_list = []
        for start_cell in self._initial_tiles_dict[direction]:
            # step 1: iterate through each line, write results to temp list
            for step in range(num_steps):
                row = start_cell[0] + step * OFFSETS[direction][0]
                col = start_cell[1] + step * OFFSETS[direction][1]
                temp_list.append(self._initial_grid[row][col])
            # step 2: merge temp list
            temp_list_snap = temp_list[:]
            temp_list = merge(temp_list)
            print(temp_list_snap, temp_list)
            if temp_list_snap != temp_list:
                moved = True
            # step 3: store merged temp list back on grid
            idx = 0
            for step in range(num_steps):
                row = start_cell[0] + step * OFFSETS[direction][0]
                col = start_cell[1] + step * OFFSETS[direction][1]
                if direction in (UP, DOWN):
                    self._initial_grid[row][col] = temp_list[idx]
                    idx += 1
                elif direction in (LEFT, RIGHT):
                    self._initial_grid[row][col] = temp_list[idx]
                    idx += 1
            temp_list = []
        if moved:
            self.new_tile()
            moved = False

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        zero_list = []
        zero_cell = ()
        # self._cells = [[0 for col in range(self._grid_width)] for row in range(self._grid_height)]
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                if self._initial_grid[row][col] == 0:
                    zero_cell = (row, col)
                    zero_list.append(zero_cell)
        if len(zero_list) > 0:
            chance = random.randrange(0,10)
            cell_idx = random.randrange(len(zero_list))
            if chance == 9:
                self._initial_grid[zero_list[cell_idx][0]][zero_list[cell_idx][1]] = 4
            else:
                self._initial_grid[zero_list[cell_idx][0]][zero_list[cell_idx][1]] = 2
        else:
            print('Better luck next time')

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._initial_grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._initial_grid[row][col]

