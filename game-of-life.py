#!/usr/bin/env python

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

# Set up two grids to hold the old and new configurations.
# This assumes an N*N grid of points.
# Each point is either alive or dead, represented by integer values of 1 and 0, respectively.
N = 100
old_grid = numpy.zeros(N*N, dtype='i').reshape(N,N)
new_grid = numpy.zeros(N*N, dtype='i').reshape(N,N)

def seed(grid):
   ''' Set up a random initial configuration for the grid. '''
   for i in range(0, N):
      for j in range(0, N):
         if(random.randint(0, 100) < 15):
            grid[i][j] = 1
         else:
            grid[i][j] = 0
         
def live_neighbours(grid, i, j):
   ''' Count the number of live neighbours around point (i, j). '''
   s = 0 # The total number of live neighbours.
   # Loop over all the neighbours.
   for x in [i-1, i, i+1]:
      for y in [j-1, j, j+1]:
         if(x == i and y == j):
            continue # Skip the current point itself - we only want to count the neighbours!
         if(x != N and y != N):
            s += grid[x][y]
         # The remaining branches handle the case where the neighbour is off the end of the grid.
         # In this case, we loop back round such that the grid becomes a "toroidal array".
         elif(x == N and y != N):
            s += grid[0][y]
         elif(x != N and y == N):
            s += grid[x][0]
         else:
            s += grid[0][0]
   return s

# Seed an initial configuration for the grid
seed(old_grid)
pylab.pcolormesh(old_grid)
pylab.colorbar()
pylab.savefig('generation0.png')

t = 1; T = 200 # Time-stepping parameters.
write_frequency = 5 # How frequently we want to output a grid configuration.
while t <= T: # Evolve!
   print "At time level %d" % t
   # Loop over each cell of the grid and apply Conway's rules.
   for i in range(N):
      for j in range(N):
         live = live_neighbours(old_grid, i, j)
         if(old_grid[i][j] == 1 and live < 2):
            new_grid[i][j] = 0 # Dead from starvation.
         elif(old_grid[i][j] == 1 and (live == 2 or live == 3)):
            new_grid[i][j] = 1 # Continue living.
         elif(old_grid[i][j] == 1 and live > 3):
            new_grid[i][j] = 0 # Dead from overcrowding.
         elif(old_grid[i][j] == 0 and live == 3):
            new_grid[i][j] = 1 # Alive from reproduction.

   # Output the new configuration.
   if(t % write_frequency == 0):
      pylab.pcolormesh(new_grid)
      pylab.savefig('generation%d.png' % t)

   # The new configuration becomes the old configuration for the next generation.
   old_grid = new_grid.copy()

   # Move on to the next time level
   t += 1
       
