player_o = True
player_x = False

class TicTacToeGame():

    def __init__(self, n, whose_turn):
        self._n = n
        self._grid = {}
        self._whose_turn = whose_turn

    def make_grid(self):
        for x_coor in range(self._n):
            for y_coor in range(self._n):
                self._grid[x_coor, y_coor] = None
        return self._grid

    def __str__(self):
        new = str(self._grid)
        return new

    def players_turn(self, row, column, whose_turn):
        """
        whoever's turn it is, you input where you want to play
        """
        if self._whose_turn == True:
            if self._grid[row, column] == True or False:
                return "Pick another spot"
            else:
                self._grid[row, column] = self._whose_turn
                self._whose_turn = False
        if self._whose_turn == False:
            if self._grid[row, column] == True or False:
                return "Pick another spot"
            else:
                self._grid[row, column] = self._whose_turn
                self._whose_turn = True

    def board_status(self):
        print(self._grid)

    def switch_player(self, whose_turn):

        if self._whose_turn == True:
            self._whose_turn = False
        else:
            self._whose_turn = True
        return self._whose_turn

    def who_is_winning(self):
        """
        get the keys and values for the grid
        check what player has each box
        if the box numbers are all the same, either the first or second value,
        indicating the same row or column return win
        0,0 1,1 2,2 and 2,0 1,1 0,2
        """

        player_o_box = []
        player_x_box = []
        for key, value in self._grid.items():
            if value == True:
                player_o_box.append(key)
            else:
                player_x_box.append(key)
            print(player_o_box)
        if len(player_o_box) > 3:
            for each in range(self._n):
                for box[0] in player_o_box:
                    if box[0] == each:  # checking for straight lines
                        continue
                return 'you won'


gan = TicTacToeGame(3, True)

print(gan.make_grid())
print(gan.players_turn(1, 0, True))
print(gan.board_status())
print(gan.switch_player(True))
print(player_o)
print(gan.who_is_winning())