#  An implementation of Conway's Game of Life in Python.

#  Copyright (C) 2013 Christian Jacobs.

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy
import pylab
import random

N = 100
old_board = numpy.zeros(N*N).reshape(N,N)
new_board = numpy.zeros(N*N).reshape(N,N)

# Time-stepping parameters
t = 1
T = 200

def seed(board):
   for i in range(0, N):
      for j in range(0, N):
         if(random.randint(0, 100) < 7):
            board[i][j] = 1
         else:
            board[i][j] = 0
         
def live_neighbours(board, i, j):
   s = 0
   for a in range(i-1, i+2):
      for b in range(j-1, j+2):
         if(a == i and b == j):
            continue # Skip the cell itself - we only want to count the neighbours!
         if(a != N and b != N):
            s += board[a][b]
         elif(a == N and b != N):
            s += board[0][b]
         elif(a != N and b == N):
            s += board[a][0]
         else:
            s += board[0][0]
   return s

# Seed an initial configuration for the board
seed(old_board)
pylab.pcolormesh(old_board)
pylab.colorbar()
pylab.savefig('generation0.png')

while t <= T:
   print "Time level %d" % t
   # Loop over each cell of the board and apply Conway's rules.
   for i in range(N):
      for j in range(N):
         live = int(live_neighbours(old_board, i, j))
         if(old_board[i][j] == 1 and live < 2):
            new_board[i][j] = 0
         elif(old_board[i][j] == 1 and (live == 2 or live == 3)):
            new_board[i][j] = 1
         elif(old_board[i][j] == 1 and live > 3):
            new_board[i][j] = 0
         elif(old_board[i][j] == 0 and live == 3):
            new_board[i][j] = 1

   # Output the new board
   pylab.pcolormesh(new_board)
   pylab.savefig('generation%d.png' % t)

   # The new board becomes the old board.
   old_board = new_board.copy()   

   # Move on to the next time level
   t += 1
       

