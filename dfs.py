from support_function import*
import time
'''
//========================//
//          DFS           //
//        ALGORITHM       //
//     IMPLEMENTATION     //
//========================//
'''
def DFS_search(initial_board, list_check_point):
    """Perform Depth-First Search to find the solution."""
    start_time = time.time()
    list_state = [start_state]
    stack = []
    start_state = state(initial_board, None, list_check_point)
    stack.append(start_state)
    
    visited = set()

    while stack:
        # Get the last state from the stack 
        current_state = stack.pop()
        
        # Check if the current board configuration has been visited
        board_tuple = tuple(tuple(row) for row in current_state.board)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)
        
        # Check if the current state is a goal state
        if check_win(current_state.board, list_check_point):
            return current_state.get_line()  # Return the path to the solution
        
        # Find the player's current position
        cur_pos = find_position_player(current_state.board)
        ''' 
        THIS WILL PRINT THE STEP-BY-STEP IMPLEMENTATION OF HOW THE ALGORITHM WORKS, 
        UNCOMMENT TO USE IF NECCESSARY 
        '''
        '''
        time.sleep(1)
        clear = lambda: os.system('cls')
        clear()
        print_matrix(now_state.board)
        print("State visited : {}".format(len(list_state)))
        print("State in queue : {}".format(len(list_visit)))
        '''
        # Get possible next positions
        next_positions = get_next_pos(current_state.board, cur_pos)
        
        for next_pos in next_positions:
            ''' MAKE NEW BOARD '''
            new_board = move(current_state.board, next_pos, cur_pos, list_check_point)
            ''' IF THIS BOARD DON'T HAVE IN LIST BEFORE --> SKIP THE STATE '''
            if is_board_exist(new_board, list_state):
                continue
            ''' IF ONE OR MORE BOXES ARE STUCK IN THE CORNER --> SKIP THE STATE '''
            if is_board_can_not_win(new_board, list_check_point):
                continue
            ''' IF ALL BOXES ARE STUCK --> SKIP THE STATE '''
            if is_all_boxes_stuck(new_board, list_check_point):
                continue

            ''' MAKE NEW STATE '''
            new_state = state(new_board, current_state, list_check_point)
            ''' CHECK WHETHER THE NEW STATE IS GOAL OR NOT '''
            if check_win(new_board, list_check_point):
                print("Found win")
                return (new_state.get_line(), len(list_state))
            
            ''' APPEND NEW STATE TO PRIORITY QUEUE AND TRAVERSED LIST '''
            list_state.append(new_state)
            stack.append(new_state)  # Add new state to the stack

            ''' COMPUTE THE TIMEOUT '''
            end_time = time.time()
            if end_time - start_time > TIME_OUT:
                return []
        end_time = time.time()
        if end_time - start_time > TIME_OUT:
            return []
    print("Not Found")
    return []
