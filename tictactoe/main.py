from ziz_utils import clear, validate_param, isInt
from collections.abc import Container
import random

def isAllSame(container: Container) -> bool:
    """
    Check if all the items in an Container are the same. If empty, return false.
    """
    validate_param(container, "container", Container)
    return True if container and all(container[0] == i for i in container) else False

def getDiagonal(grid: Container) -> list[list[str]]:
    """
    Get the center diagonal line of a 2D grid, assuming the grid is a square. 
    """
    diagonal: list[str] = []
    counter_diagonal: list[str] = []

    for i in range(len(grid)):
        diagonal.append(grid[i][i])
        counter_diagonal.append(list(reversed(grid[i]))[i])
        
    return [diagonal, counter_diagonal]

def main() -> None:
    """
    The main function.
    """
    clear()
    while True:
        board: list[str] = [*"#" * 9]
        players: list[str] = [*"XO"]
        cmd: str = input("1. Start game. \n2. End game. \nYour input: ").strip()
        clear()
        
        if cmd not in [*"12"]:
            print("Invalid input: Option does not exist. \n")
            continue
        elif not cmd:
            print("Invalid input: Empty input. \n")
            continue
        elif cmd == "2":
            exit(0)

        current = random.choice(players)
        turn: int = 0
        print(f"Player {current} go first! \n")
        while True:
            rows: list[list[str]] = [board[i:i+3] for i in range(0, 9, 3)]
            columns: list[list[str]] = [[board[i] for i in range(col, 9, 3)] for col in range(3)]
            diagonal: list[list[str]] = getDiagonal(rows)
            display_board: str = "\n---------\n".join([" | ".join(i) for i in rows])

            if turn >= 3:
                temp: list[list[list[str]]] = [rows, columns, diagonal]
                winner: str = "#"
                for i in temp:
                    for k in i:
                        if isAllSame(k):
                            winner = k[0]
                            break
                
                if winner != "#":
                    print(f"{winner} wins! \n")
                    break
                elif board.count("#") == 0:
                    print("It's a tie!")
                    break

            move = input(f"{display_board}\n{current}'s move: ").strip()
            clear()

            if not isInt(move):
                print("Invalid input: Input has to be a valid integer. \n")
                continue
            elif not move:
                print("Invalid input: Empty input. \n")
                continue
            elif int(move) not in range(1, 9):
                print("Invalid input: Input has to be from 1 to 9. \n")
                continue
            elif board[int(move) - 1] != "#":
                print("Invalid input: Tile's already occupied, please choose again. \n")
                continue

            board[int(move) - 1] = current
            turn += 1
            current = "XO".strip(current)

if __name__ == "__main__":
    main()