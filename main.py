import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Side:
    def __init__(self):
        self.current_val = 1

    def fold_self(self):
        self.current_val = 1
    
    def fold_opposite(self):
        self.current_val += opposites[self].current_val

    def fold_adjacent(self):
        self.current_val += self.current_val

order = input()
side = input()

Up, Left, Down, Right = [Side() for i in range(4)]

opposites = {
    Right: Left,
    Left: Right,
    Up: Down,
    Down: Up
}

order_list = []

for letter in order:
    order_list.append((letter))

for i in order_list:
    if i == 'U':
        Left.fold_adjacent()
        Right.fold_adjacent()
        Down.fold_opposite()
        Up.fold_self()
    elif i == 'D':
        Left.fold_adjacent()
        Right.fold_adjacent()
        Up.fold_opposite()
        Down.fold_self()
    elif i == 'L':
        Down.fold_adjacent()
        Up.fold_adjacent()
        Right.fold_opposite()
        Left.fold_self()
    elif i == 'R':
        Down.fold_adjacent()
        Up.fold_adjacent()
        Left.fold_opposite()
        Right.fold_self()

if side == 'U':
    print(Up.current_val)
elif side == 'D':
    print(Down.current_val)
elif side == 'L':
    print(Left.current_val)
elif side == 'R':
    print(Right.current_val)



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

