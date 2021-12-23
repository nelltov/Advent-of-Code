import pathlib
import sys
from typing import List, Tuple


def update_board(number_drawn, board_list, marked_board):
    """ Based on the number drawn and the given boards, updates the list of marked values appropriately"""
    num_rows = 5
    for board_idx in range(len(marked_board)):  # Iterating through individual boards
        for row_idx in range(num_rows):  # Iterating through rows of one board
            for col_idx in range(num_rows):  # Iterating through values of one row
                if int(board_list[board_idx][row_idx][col_idx]) == int(number_drawn):
                    marked_board[board_idx][row_idx][col_idx] = True
    return marked_board


def is_winner(marked_board: List[List[str]]) -> bool:
    """ Returns true if all numbers in any row or any column of the inputted board are marked (board is a winner)"""
    # checking each row
    for row in marked_board:
        if False not in row:
            return True

    # checking each column
    num_cols = 5
    for col in range(num_cols):
        marked_list = []
        for row in range(num_cols):
            marked_list += [marked_board[row][col]]
        if False not in marked_list:
            return True

    return False


def calculate_score(number_drawn, winning_board: List[List[str]], marked_board: List[List[str]]) -> int:
    """ Start by finding the sum of all unmarked numbers on that board.
    Then, multiply that sum by the number that was just called when the board won"""
    num_rows = 5
    unmarked_sum = 0
    for row_idx in range(num_rows):
        for col_idx in range(num_rows):
            if not marked_board[row_idx][col_idx]:
                unmarked_sum += int(winning_board[row_idx][col_idx])

    return unmarked_sum * int(number_drawn)


def parse(puzzle_input_str: str) -> Tuple[List[str], List[List[List[str]]], List[List[List[bool]]]]:
    """Parse input -- bingo number draw order and set of boards"""
    draw_order: List[str] = puzzle_input_str.splitlines()[0].split(',')
    board_rows: List[str] = [row for row in puzzle_input_str.split('\n')[1:] if len(row) > 0]
    num_rows = 5
    num_boards: int = len(board_rows) // num_rows

    # each index is a individual board, each of which is a 2D list of strings
    board_list: List[List[List[str]]] = [[[''] * num_rows] * num_rows for _ in range(num_boards)]

    # entry is False if the value is unmarked, and true if the number has been drawn
    marked_list = [[[False for _ in range(num_rows)] for _ in range(num_rows)] for _ in range(num_boards)]

    for i in range(0, len(board_rows), num_rows):
        current_board: List[List[str]] = board_list[i//num_rows]
        for j in range(num_rows):
            board_row_index = i + j
            row_num_list: List[str] = board_rows[board_row_index].split()
            current_board[j] = row_num_list
        board_list[i//num_rows] = current_board

    return draw_order, board_list, marked_list


def part1(data: Tuple[List[str], List[List[List[str]]], List[List[List[bool]]]]) -> int:
    """Solve part 1 -- To guarantee victory against the giant squid, figure out which board will win first.
    What will your final score be if you choose that board?"""
    draw_order, board_list, marked_list = data

    for number_drawn in draw_order:
        marked_list = update_board(number_drawn, board_list, marked_list)
        for board_idx in range(len(marked_list)):
            if is_winner(marked_list[board_idx]):
                return calculate_score(number_drawn, board_list[board_idx], marked_list[board_idx])

    return -1


def part2(data: Tuple[List[str], List[List[List[str]]], List[List[List[bool]]]]) -> int:
    """Solve part 2 -- Figure out which board will win last. Once it wins, what would its final score be?"""
    draw_order, board_list, marked_list = data

    winning_boards = []

    for number_drawn in draw_order:
        marked_list = update_board(number_drawn, board_list, marked_list)
        for board_idx in range(len(marked_list)):
            if is_winner(marked_list[board_idx]) and marked_list[board_idx] not in winning_boards:
                winning_boards += [marked_list[board_idx]]

                # if the board that was added was the last one to win, return its score
                if len(winning_boards) == len(board_list):
                    return calculate_score(number_drawn, board_list[board_idx], marked_list[board_idx])

    return -1


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()

        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
