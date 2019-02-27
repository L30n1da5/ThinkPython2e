def print_grid(n           = 3,
               square_size = 3,
               corner_char = '+',
               row_char    = '-',
               col_char    = '|',
               space_char  = ' '
               ):
    border = corner_char 
    for i in range(n):
        border = border + space_char + (row_char + space_char) * square_size + corner_char
    filler = col_char
    for i in range(n):
        filler = filler + space_char + space_char * (square_size * 2) + col_char        
    for i in range(n):
        print(border)
        for j in range(square_size):
            print(filler)
    print(border)

print_grid()
