
def can_fill_spaces(n, m, left_piece, right_piece, pieces):
    # Create a set to keep track of used pieces
    used_pieces = set()
    # Add the initial pieces to the used pieces set
    used_pieces.add(left_piece)
    used_pieces.add(right_piece)

    # Function to check if a piece can be placed
    def can_place_piece(piece, side):
        nonlocal used_pieces
        if piece in used_pieces:
            return False
        if side == 'left':
            return piece[1] == left_piece[0]
        elif side == 'right':
            return piece[0] == right_piece[1]

    # Recursive function to fill the spaces
    def fill_spaces(spaces_left):
        nonlocal used_pieces
        if spaces_left == 0:
            return True
        for piece in pieces:
            if piece not in used_pieces:
                if can_place_piece(piece, 'left'):
                    used_pieces.add(piece)
                    if fill_spaces(spaces_left - 1):
                        return True
                    used_pieces.remove(piece)
                elif can_place_piece(piece, 'right'):
                    used_pieces.add(piece)
                    if fill_spaces(spaces_left - 1):
                        return True
                    used_pieces.remove(piece)
        return False

    return fill_spaces(n - 1)

# Main loop to process input
while True:
    n = int(input())
    if n == 0:
        break
    m = int(input())
    left_piece = tuple(map(int, input().split()))
    right_piece = tuple(map(int, input().split()))
    pieces = [tuple(map(int, input().split())) for _ in range(m)]
    
    # Check if it's possible to fill the spaces
    if can_fill_spaces(n, m, left_piece, right_piece, pieces):
        print("NO")
    else:
        print("YES")
