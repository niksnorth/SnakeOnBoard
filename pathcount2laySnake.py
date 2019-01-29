# Python code to find number of possible paths to  
# lay a snake on a matrix of n x n grid. 

GRID_SIZE = 4
pathcount = 0
pathways = 0

def	reset_grid(grid):

	for i in range(GRID_SIZE):
		for j in range(GRID_SIZE):
			grid[i][j]=0

def traverse_grid(grid, i, j, snakelength):	
	
	global pathcount
	
	grid[i][j]=1
			
	snakelength=snakelength+1
	
	if snakelength == GRID_SIZE*GRID_SIZE:
		pathcount=pathcount+1
		return
		
	if (j<GRID_SIZE-1) and (grid[i][j+1]==0):
		traverse_grid(grid, i, j+1, snakelength)
		grid[i][j+1] = 0
		
	if (i<GRID_SIZE-1) and (grid[i+1][j]==0):
		traverse_grid(grid, i+1, j, snakelength)
		grid[i+1][j] = 0

	if (i>0) and (grid[i-1][j] == 0):
		traverse_grid(grid, i-1, j, snakelength)
		grid[i-1][j] = 0		

	if (j>0) and (grid[i][j-1] == 0):
		traverse_grid(grid, i, j-1, snakelength)
		grid[i][j-1] = 0
	
# main driver Code 
def main():
	
	grid = [[0] * GRID_SIZE for i in range(GRID_SIZE)]
	
	for i in range(GRID_SIZE):
		for j in range(GRID_SIZE):
			reset_grid(grid)
			traverse_grid(grid, i, j, pathways)
			
	print("Number of possible pathways:",	pathcount)
		
if __name__ == '__main__':
   main()
		
