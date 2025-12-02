input_file = "day02/input.txt"
sample_file = "day02/sample.txt"


def calculate_invalid_ids(data_file) -> int:
    result = 0
    data = open(data_file).read().strip()
    parts = [p.strip() for p in data.split(",") if p.strip()]
    ranges: List[Tuple[int, int]] = []
    for p in parts:
        lo_str, hi_str = p.split("-")
        ranges.append((int(lo_str), int(hi_str)))    

    for lo, hi in ranges:
        print('{} to {}'.format(lo, hi))
        result += sum_invalid_ids_in_range(lo, hi)
    return result

def calculate_something2(data_file) -> int:
    result = 0
    data = [[int(s) for s in line.split()] for line in open(data_file).read().strip().splitlines()]
    for entry in data:
        pass
    return result

def sum_invalid_ids_in_range(start: int, stop: int) -> int:
    sum = 0

    for i in range(start, stop+1):
        sum += i if not is_valid(i) else 0
    return sum

def is_valid(number: int) -> bool:
    as_string = str(number)
    length = len(as_string)
    if ((length % 2) != 0):
        # only even length of figures can be invalid
        return True
    else:
        front = int( as_string[ 0 : int(length/2) ] )
        back = int( as_string[ int(length/2) : ] )
        return False if front == back else True


if __name__ == "__main__":
    # print(sum_invalid_ids_in_range(11, 22))
    print(calculate_invalid_ids(sample_file))
    print(calculate_invalid_ids(input_file))
    # print(calculate_something2(sample_file))
    # print(calculate_something2(input_file))
