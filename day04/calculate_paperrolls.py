from itertools import batched

input_file = "day04/input.txt"
sample_file = "day04/sample.txt"


DIRS = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]


def calculate_paperrolls_pt1(data_file) -> int:
    result = 0
    data = [list(line) for line in open(data_file).read().strip().splitlines()]

    grid = {
        (x, y): data[y][x]
        for y in range(len(data))
        for x in range(len(data[0]))
    }    
    result = sum_accessible_rolls(grid)
        
    return result


def calculate_paperrolls_pt2(data_file) -> int:
    result = 0
    data = [list(line) for line in open(data_file).read().strip().splitlines()]

    grid = {
        (x, y): data[y][x]
        for y in range(len(data))
        for x in range(len(data[0]))
    }    
    while ((removal := sum_and_remove_accessible_rolls(grid)) > 0):
        result += removal
     
    return result

def sum_accessible_rolls(grid: dict) -> int:
    result = 0
    for pos, value in grid.items():
        # print('Coord {}, {}'.format(pos, value))
        result += 1 if value == "@" and count_neighbor_values(grid, pos, "@") < 4 else 0

    return result

def sum_and_remove_accessible_rolls(grid: dict) -> int:
    result = 0
    for pos, value in grid.items():
        # print('Coord {}, {}'.format(pos, value))
        if (value == "@" and count_neighbor_values(grid, pos, "@") < 4):
            result += 1
            grid[pos] = "."
        
    return result


def count_neighbor_values(grid: dict, pos: tuple[int, int], target: str) -> int:
    x, y = pos
    count = 0
    for dx, dy in DIRS:
        if grid.get((x + dx, y + dy)) == target:
            count += 1
    print('{} -> {}'.format(pos, count))
    return count


if __name__ == "__main__":
    # print(calculate_paperrolls_pt1(sample_file))
    # print(calculate_paperrolls_pt1(input_file))
    # print(calculate_paperrolls_pt2(sample_file))
    print(calculate_paperrolls_pt2(input_file))
