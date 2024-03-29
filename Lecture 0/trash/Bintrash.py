import sys

def calculate_movements(bins, order):
    total_movements = 0
    for i, color in enumerate('BGC'):
        for j, bin_counts in enumerate(bins[i]):
            if color != order[j]:
                total_movements += bin_counts
    return total_movements

def find_min_movements(bins):
    min_movements = float('inf')
    min_order = None
    for order in ['BCG', 'BGC', 'CBG', 'CGB', 'GBC', 'GCB']:
        movements = calculate_movements(bins, order)
        if movements < min_movements or (movements == min_movements and order < min_order):
            min_movements = movements
            min_order = order
    return min_order, min_movements

bottles = [list(map(int, line.split())) for line in sys.stdin.readlines()]
results = []

for bins in bottles:
    bins = [bins[:3], bins[3:6], bins[6:]]
    order, movements = find_min_movements(bins)
    results.append((order, movements))

for order, movements in results:
    print(order, movements)
