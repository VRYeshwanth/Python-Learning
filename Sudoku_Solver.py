def print_grid(grid):
    
    for i in range(9):
        for j in range(9):
            print(f"{grid[i][j]}", end=" ")
        print()

def is_valid_move(grid, row, col, num):
    if num in grid[row]:
        return False

    for i in range(9):
        if grid[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def read_sudoku_from_cmd():
    print("Enter the Sudoku puzzle row by row, with empty cells represented by 0.")
    grid = []
    for i in range(9):
        row = input(f"Enter row {i + 1}: ").strip()
        
        if len(row) != 9:
            print("Error: Each row must contain exactly 9 characters.")
            return None
        
        valid = all(char.isdigit() for char in row)
        if not valid:
            print("Error: Only digits (0-9) are allowed.")
            return None
        grid.append([int(char) for char in row])
    return grid

grid = read_sudoku_from_cmd()
if grid is not None:
    print("\nInput Sudoku grid:")
    print_grid(grid)
    print("--------------------\n")
    if solve_sudoku(grid):
        print("Solution:")
        print_grid(grid)
    else:
        print("No solution exists.")
