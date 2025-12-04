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

def sum_accessible_rolls(grid: dict) -> int:
    result = 0
    for pos, value in grid.items():
        # print('Coord {}, {}'.format(pos, value))
        result += 1 if value == "@" and count_neighbor_values(grid, pos, "@") < 4 else 0

    return result

# def has_neighbor_value_dict(grid: dict, pos: tuple, target: str):
#     x, y = pos
#     for dx, dy in DIRS:
#         if grid.get((x+dx, y+dy)) == target:
#             return True
#     return False

def count_neighbor_values(grid: dict, pos: tuple[int, int], target: str) -> int:
    x, y = pos
    count = 0
    for dx, dy in DIRS:
        if grid.get((x + dx, y + dy)) == target:
            count += 1
    print('{} -> {}'.format(pos, count))
    return count


def calculate_something2(data_file) -> int:
    result = 0
    data = [[int(s) for s in line.split()] for line in open(data_file).read().strip().splitlines()]
    for entry in data:
        pass
    return result

if __name__ == "__main__":
    # print(calculate_paperrolls_pt1(sample_file))
    print(calculate_paperrolls_pt1(input_file))
    # print(calculate_something2(sample_file))
    # print(calculate_something2(input_file))
