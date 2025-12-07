import operator
from functools import reduce

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,  # oder operator.truediv
}


input_file = "day06/input.txt"
sample_file = "day06/sample.txt"


def calculate_math_homework_pt1(data_file) -> int:
    result = 0
    data = [line.split() for line in open(data_file).read().strip().splitlines()]

    print(data)

    cols = len(data[0])
    rows = len(data)

    transposed = list(map(list, zip(*data)))

    for row in transposed:
        result += eval_row(row)

    return result

def eval_row(row: list[str]) -> int:
    *nums_str, op = row             # alle bis auf die letzte Spalte, letzte Spalte
    nums = list(map(int, nums_str)) # in ints umwandeln
    func = OPS[op]                  # passende Operator-Funktion holen

    # falls genau 2 Operanden (typischer Fall):
    if len(nums) == 2:
        a, b = nums
        return func(a, b)

    # falls mehr als 2 Operanden: linksassoziativ reduzieren
    return reduce(func, nums)


def calculate_math_homework_pt2(data_file) -> int:
    result = 0
    data = [[int(s) for s in line.split()] for line in open(data_file).read().strip().splitlines()]
    for entry in data:
        pass
    return result

if __name__ == "__main__":
    # print(calculate_math_homework_pt1(sample_file))
    print(calculate_math_homework_pt1(input_file))
    # print(calculate_math_homework_pt2(sample_file))
    # print(calculate_math_homework_pt2(input_file))
