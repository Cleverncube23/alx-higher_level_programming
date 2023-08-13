#!/usr/bin/python3

def print_matrix(integers_grid=[[]]):
  """
  Display a grid of integers to standard output  
  """

  for row_index in range(len(integers_grid)):
    
    row_length = len(integers_grid[row_index])

    for col_index in range(row_length):
    
      if col_index != row_length - 1:
      
        end_char = ' '
      
      else:
      
        end_char = ''
        
      print("{:d}".format(integers_grid[row_index][col_index]), end=end_char)

    print("")
