# ## Power of Thor - Episode 1
#
# **Link to the problem :
# [CodinGame Power of Thor](https://www.codingame.com/training/easy/power-of-thor-episode-1)**
#
# ### **Problem Overview:**
#
# <span class="hljs-comment">In this puzzle, Thor needs to move toward the
# light's position. Each turn, you need to print the direction</span>
# <span class="hljs-comment">in which Thor should move: North (N), South (S),
# East (E), or West (W). Thor's initial position is
# defined</span>      <span class="hljs-comment">&nbsp;by
# <code>initial_tx</code> and <code>initial_ty</code>, while the light is
# located at <code>light_x</code> and <code>light_y</code>.</span>
#
# ### **Overview of the algorithm:**
#
# ![Sketch](thor.jpg)

# Read input from standard input
input_data = sys.stdin.readline().split()
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input_data]
import sys
import math 
# **Game loop** The loop calculates and prints the direction Thor must go on
# each turn.
while True:
    remaining_turns = int(input())  
    # **Determine Direction** Thor moves East or West depending on the position
    # of `light_x` relative to `initial_tx`.
    if light_x > initial_tx:
    # Move East if the light is further right.
        direction_x = "E"  
    elif light_x < initial_tx: 
     # Move West if the light is further left.
        direction_x = "W" 
    else:
     # No movement in the X direction if aligned.
        direction_x = "" 

    # Thor moves North or South depending on the position of `light_y` relative
    # to `initial_ty`.
    if light_y > initial_ty:
    # Move South if the light is below Thor.
        direction_y = "S"  
    elif light_y < initial_ty:
    # Move North if the light is above Thor.
        direction_y = "N"  
    else:
     # No movement in the Y direction if aligned.
        direction_y = "" 

    # **Update Thor's Position** Update Thor's Y position if there is movement
    # in the Y direction.
    if direction_y != "":
        if direction_y == "S":
        # Move South (increase Y).
            initial_ty += 1  
        else:
         # Move North (decrease Y).
            initial_ty -= 1 

    # Update Thor's X position if there is movement in the X direction.
    if direction_x != "":
        if direction_x == "E":
        # Move East (increase X).
            initial_tx += 1  
        else:
        # Move West (decrease X).
            initial_tx -= 1  

    # **Output Direction** Output the combined direction for Thor's movement
    # this turn.
    print(direction_y + direction_x)

# **Conclusion**
#
# This program ensures Thor moves optimally towards the light using the shortest
# path. Thor stops when his position matches the light's coordinates or when he
# runs out of moves.
f418596b856ecb1d16dab0ad608b99af8710b0b0