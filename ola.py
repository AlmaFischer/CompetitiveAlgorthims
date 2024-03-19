# Function to calculate the total number of movements for a given arrangement of bins
def calculate_movements(arrangement, bins):
    movements = 0
    for i in range(3):  # For each color
        for j in range(3):  # For each bin
            if j != arrangement[i]:  # If the bin is not the one designated for this color
                movements += bins[j][i]  # Add the number of bottles to movements
    return movements

# Function to find the optimal arrangement of bins
def find_optimal_arrangement(bins):
    min_movements = float('inf')
    optimal_arrangement = ''
    for a in range(3):
        for b in range(3):
            if b != a:
                c = 3 - a - b
                arrangement = (a, b, c)
                movements = calculate_movements(arrangement, bins)
                if movements < min_movements:
                    min_movements = movements
                    optimal_arrangement = arrangement
    return optimal_arrangement, min_movements

# Function to convert arrangement indices to color string
def indices_to_color(arrangement):
    colors = ['B', 'G', 'C']
    return ''.join(colors[i] for i in arrangement)

# Reading input
while True:
    try:
        bins_input = input().strip().split()
        bins = [[int(bins_input[i]), int(bins_input[i+1]), int(bins_input[i+2])] for i in range(0, len(bins_input), 3)]
        
        # Finding the optimal arrangement and minimum movements
        arrangement, min_movements = find_optimal_arrangement(bins)
        
        # Converting arrangement indices to color string
        color_arrangement = indices_to_color(arrangement)
        
        # Outputting result
        print(color_arrangement, min_movements)
        
    except EOFError:
        break  # Exit when there's no more input
