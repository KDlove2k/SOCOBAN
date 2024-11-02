from queue import PriorityQueue
from support_function import*

def USC_search(initial_board, list_check_point):
    """Perform Uniform Cost Search to find the solution."""
    pq = PriorityQueue()
    
    start_state = state(initial_board, None, list_check_point)
    pq.put((0, start_state))  # Cost and state
    
    visited = set()

    while not pq.empty():
        current_cost, current_state = pq.get()
        
        board_tuple = tuple(tuple(row) for row in current_state.board)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)
        
        # Check if the current state is a goal state
        if check_win(current_state.board, list_check_point):
            return current_state.get_line()  # Return the path to the solution
        
        # Find the player's current position
        cur_pos = find_position_player(current_state.board)
        
        # Get possible next positions
        next_positions = get_next_pos(current_state.board, cur_pos)
        
        for next_pos in next_positions:
            # Move to the new position and get the new board state
            new_board = move(current_state.board, next_pos, cur_pos, list_check_point)
            
            if not is_board_exist(new_board, visited):
                new_cost = current_cost + 1  # Increment the cost
                new_state = state(new_board, current_state, list_check_point)
                pq.put((new_cost, new_state))
    
    return None  
