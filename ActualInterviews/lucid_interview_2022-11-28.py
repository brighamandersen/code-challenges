#!/usr/bin/python3

################################################################################
# CONFIDENTIAL
#
# The contents of this and other files used for interviews are confidential, and
# should not be shared outside of Lucid Software. Discussing or otherwise distributing
# the problems or questions used in your interviews may cause any future interviews
# to be cancelled or any potential offers to be revoked.
################################################################################

###############################################################################
# Part 1:
#
# Given a list of numbers, return the 3 largest numbers that are divisible by 7,
# sorted from largest to smallest.
#
#     Example:
#       Given: [14, 3, 21, 17, 7, 70]
#       Result: [70, 21, 14].
#
# Note: you can assume for the purposes of this problem that all inputs will
# have at least three integers that are divisible by 7
###############################################################################

def getThreeLargestNumbersDivisibleBySeven(inputList):
    inputList.sort(reverse=True)
    ans = []

    for num in inputList:
        if len(ans) == 3:
            break
        if num % 7 == 0:
            ans.append(num)

    return ans

# Test Cases
if __name__ == '__main__':
    print('Part 1:')
    testInputs = [
        [7, 4, 21, 49, 6, 20, 14],
        [7, 14, 21],
        [35, 7, 14, 28, 21, 42],
        [105, 7, 140, 11, 12, 13]
    ]
    expectedOutputs = [
        [49, 21, 14],
        [21, 14, 7],
        [42, 35, 28],
        [140, 105, 7]
    ]
    for testInput, expectedOutput in zip(testInputs, expectedOutputs):
        print(f'Given:    {testInput}')
        print(f'Result:   {getThreeLargestNumbersDivisibleBySeven(testInput)}')
        print(f'Expected: {expectedOutput}\n')
    print('')


##############################################################################
# Part 2:
#
# Given a string of space separated words, return a new string that is composed
# of the last letter of each word in the input.
#
#     Example:
#       Given: "sell emu anthropomorphic alveoli acid"
#       Result: "lucid"
##############################################################################

def decode(sentence):
    words = sentence.split(' ')
    last_letters = [word[-1] for word in words]
    return "".join(last_letters)

# Test Cases
if __name__ == '__main__':
    print('Part 2:')
    testInputs = [
        "sell emu anthropomorphic alveoli acid",
        "w o r d",
        "z",
        "correct horse battery staple"
    ]
    expectedOutputs = [
        "lucid",
        "word",
        "z",
        "teye"
    ]
    for testInput, expectedOutput in zip(testInputs, expectedOutputs):
        print(f'Given:    "{testInput}"')
        print(f'Result:   "{decode(testInput)}"')
        print(f'Expected: "{expectedOutput}"\n')
    print('')


################################################################################
# Part 3:
#
# Pente is a two-player game normally played on a 19x19 grid of intersections.
# For the purposes of this exercise we'll use a 9x9 board. This allows each grid
# space to be identified by a letter and number as shown in the diagram below.
#
#   a b c d e f g h i
# 1 . . . . . . . . .
# 2 . . . . . . W . .
# 3 . B . . . B . . .
# 4 . . W . B B . . .
# 5 . . . W . B . . .
# 6 . . B W W . . . .
# 7 . . . . . W . . .
# 8 . . . . . . . . .
# 9 . . . . . . . . .
#
# Players alternate placing stones of their symbol (B for Black or W for White)
# on any empty intersection, B plays first. The goal is to either:
#
# 1) Align five stones of the same symbol in any vertical, horizontal, or
#    diagonal direction
# - OR -
# 2) Make five captures, for a total of ten captured stones
#
# Stones are captured by flanking an adjacent pair of an opponent's stones
# directly on either side with your own stones. Captures consist of exactly two
# stones; flanking a single stone, or three or more stones, does not result in a
# capture.
#
# Given the board above, if B plays a stone at f6, it would result in the W
# stones at d6 and e6 being removed from the board. Captured stones are counted
# for each player, and first player to capture ten stones wins. The game board
# after B moves to f6 would be as follows:
#
#   a b c d e f g h i
# 1 . . . . . . . . .
# 2 . . . . . . W . .
# 3 . B . . . B . . .
# 4 . . W . B B . . .
# 5 . . . W . B . . .
# 6 . . B . . B . . .
# 7 . . . . . W . . .
# 8 . . . . . . . . .
# 9 . . . . . . . . .
#
# A stone may legally be played on any empty intersection, though even if it
# forms a pair between two enemy stones, it does not result in a capture.
# Captures occur only when a played stone flanks two stones of the opposing
# color. As an example, if W now plays at d6, followed by B playing at d7, the
# board would be as follows:
#
#   a b c d e f g h i
# 1 . . . . . . . . .
# 2 . . . . . . W . .
# 3 . B . . . B . . .
# 4 . . W . B B . . .
# 5 . . . W . B . . .
# 6 . . B W . B . . .
# 7 . . . B . W . . .
# 8 . . . . . . . . .
# 9 . . . . . . . . .
#
# If W now plays at e6, no capture occurs. The board instead is as follows:
#
#   a b c d e f g h i
# 1 . . . . . . . . .
# 2 . . . . . . W . .
# 3 . B . . . B . . .
# 4 . . W . B B . . .
# 5 . . . W . B . . .
# 6 . . B W W B . . .
# 7 . . . B . W . . .
# 8 . . . . . . . . .
# 9 . . . . . . . . .
#
# In the diagram above, a win for W occurs if W plays at g8. If it were B's
# turn, B could prevent the win by either playing at g8 (which would block W
# from playing there for the win) or playing at d4 (this would capture the
# stones at d5 and d6 and break the string of four W stones) or playing at f2,
# which would result in a win for B.
#
# There is also one more constraint for the player that went first's second move. When the player
# that went first places their second stone, it must be at least 3 spaces away from where their first
# stone was placed. For example, if the game board is as follows
#
#   a b c d e f g h i
# 1 . . W . . . . . .
# 2 . . . . . . . . .
# 3 . . . . . . . . .
# 4 . . . . . . . . .
# 5 . . . . B . . . .
# 6 . . . . . . . . .
# 7 . . . . . . . . .
# 8 . . . . . . . . .
# 9 . . . . . . . .
#
# If Black went first, they could not place their next move in the spaces that have an x in the
# diagram below because it would not be at least 3 spaces away
#
#   a b c d e f g h i
# 1 . . W . . . . . .
# 2 . . . . . . . . .
# 3 . . x x x x x . .
# 4 . . x x x x x . .
# 5 . . x x B x x . .
# 6 . . x x x x x . .
# 7 . . x x x x x . .
# 8 . . . . . . . . .
# 9 . . . . . . . . .
#
#
# Here is an online playable version https://jhenline-lucid.github.io/pente/
################################################################################

class Pente:
    BLACK = 'B'
    WHITE = 'W'
    EMPTY = '.'

    num_moves = 0  # Number of moves ALREADY COMPLETED
    curr_turn = BLACK
    first_x = None
    first_y = None

    def __init__(self):
        self.size = 9
        self.spaces = [[Pente.EMPTY] * self.size for _ in range(self.size)]

    def render(self):
        print(' ', *(chr(ord('a') + x) for x in range(self.size)))
        for y in range(self.size):
            print(y + 1, *(self.spaces[x][y] for x in range(self.size)))

    def getMoveInput(self):
        while True:
            try:
                row, col = input("Please enter move (e.g. a1): ")
                x = max(0, min(self.size - 1, ord(row) - ord('a')))
                y = max(0, min(self.size - 1, ord(col) - ord('1')))

                # Don't allow overwriting taken spots
                if self.spaces[x][y] != Pente.EMPTY:
                    raise ValueError('Space already taken')

                # Check that second move is far enough away
                if self.num_moves == 2 and self.curr_turn == Pente.BLACK:
                    if not self.isOutsideRadius(x, y):
                        raise ValueError("Black's second move must be at least 3 away from its first move")
            except ValueError as e:
                print(e)
            else:
                return x, y

    # Checks to see if the second move coordinates for black are outside the first move coordinates
    def isOutsideRadius(self, second_x, second_y):
        return second_x >= (self.first_x + 3) or second_y >= (self.first_y + 3)

    def isDraw(self):
        for x in range(len(self.spaces)):
            for y in range(len(self.spaces[0])):
                # If there's still an empty spot, keep playing
                if self.spaces[x][y] == Pente.EMPTY:
                    return False
        return True

    # Checks for a winner. None if no one won, BLACK if black won, WHITE if white won
    def getWinner(self):
        matchingSpace = None
        matchingRow = None
        numMatches = 0
        for x in range(len(self.spaces)):
            for y in range(len(self.spaces[0])):
                # FIXME - Ideally insert DP here where once it finds a space that is filled, check all 8 directions to see if there's a streak of 5 in a row
                # Ran out of time so for now I'll just check the winner on 1 case, if they're straight across

                if matchingSpace and matchingRow == y and self.spaces[x][y] == matchingSpace:
                    numMatches += 1

                if not matchingSpace and self.spaces[x][y] != Pente.EMPTY:
                    matchingSpace = self.spaces[x][y]
                    matchingRow = y
                    numMatches += 1

                if numMatches >= 5:
                    return matchingSpace

        return None



    # —––——––—–—–—–——–——–———––––—––——––
    # TODO: Implement this function.
    # A fully-working solution must do the following:
    #   1. Alternate turns between BLACK and WHITE (DONE)
    #   2. Only allow valid moves including the condition for the second move of the first player (DONE)
    #   3. Properly identify and remove captured stones
    #   4. Determine win condition of 5 or more captures (10 or more captured stones)
    #   5. Determine win condition of 5 or more stones in a row
    #   6. If there are no open locations to move, and neither player has satisfied either (DONE)
    #      win condition, end the game as a draw
    # Extra Credit:
    #   - Create an AI to play randomly
    #   - Create an AI that plays with some type of strategy
    def play(self):

        while True:
            self.render()
            x, y = self.getMoveInput()

            # Mark first move
            if self.num_moves == 0 and self.curr_turn == Pente.BLACK:
                self.first_x = x
                self.first_y = y

            # Record current move
            self.spaces[x][y] = self.curr_turn

            # Check for winner
            winner = self.getWinner()
            if winner:
                if winner == Pente.BLACK:
                    print('Black won!')
                else:
                    print('White won!')
                return

            # Check for draw
            if self.isDraw():
                print("No spaces left, no winners... It's a draw")
                return

            # Switch turns
            if self.curr_turn == Pente.BLACK:
                self.curr_turn = Pente.WHITE
            else:
                self.curr_turn = Pente.BLACK
            self.num_moves += 1

# Run the game
if __name__ == '__main__':
    print('Part 3:')
    pente = Pente()
    pente.play()
    print()

################################################################################
# CONFIDENTIAL
#
# The contents of this and other files used for interviews are confidential, and
# should not be shared outside of Lucid Software. Discussing or otherwise distributing
# the problems or questions used in your interviews may cause any future interviews
# to be cancelled or any potential offers to be revoked.
################################################################################
