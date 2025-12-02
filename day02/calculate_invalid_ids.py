from typing import List, Tuple, Set

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

def calculate_ivalid_ids2(data_file) -> int:
    result = 0
    data = open(data_file).read().strip()
    parts = [p.strip() for p in data.split(",") if p.strip()]
    ranges: List[Tuple[int, int]] = []
    for p in parts:
        lo_str, hi_str = p.split("-")
        ranges.append((int(lo_str), int(hi_str)))    


    result = sum_invalid_ids_in_range2(ranges)
    return result

def sum_invalid_ids_in_range2(ranges: List[Tuple[int, int]]) -> int:
    """
    We flip this around this time. We generate all kinds of invalid IDs and then check to see if they are in any range.
    """
    global_min = min(lo for lo, _ in ranges)
    global_max = max(hi for _, hi in ranges)

    invalid_ids: Set[int] = set()

    max_len = len(str(global_max))  # max digits any ID can have

    # Block length k to test for
    for k in range(1, max_len + 1):
        start_B = 10 ** (k - 1)   # first k-digit number (no leading zero)
        end_B   = 10 ** k - 1     # last  k-digit number

        # maximum repeats for this block length so we don't exceed max_len of the number
        max_repeats = max_len // k
        if max_repeats < 2:
            continue  # can't even repeat twice, skip
        # B is the actual k-length number
        for B in range(start_B, end_B + 1):
            sB = str(B)
            # repeat count m (>=2)
            for m in range(2, max_repeats + 1):
                s = sB * m
                N = int(s)

                if N > global_max:
                    # for larger m with same B, N will only get bigger -> break inner loop
                    break

                if N < global_min:
                    continue

                # for each "invalid" number we generated, we then test if it's inside any range.
                if in_any_range(N, ranges):
                    invalid_ids.add(N)
    return sum(invalid_ids)

def in_any_range(n: int, ranges: List[Tuple[int, int]]) -> bool:
    """
    Check if n lies inside at least one of the given ranges [lo, hi].
    """
    for lo, hi in ranges:
        if lo <= n <= hi:
            return True
    return False

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

def is_invalid_id(n: int) -> bool:
    """
    Evtl. als Alternative.
    Prüft, ob n aus einem Wiederholungsmuster besteht:
    Dezimaldarstellung = Block * m, mit m >= 2.
    """
    s = str(n)
    L = len(s)

    # m >= 2  → daher kann block_length maximal L // 2 sein
    for k in range(1, L // 2 + 1):
        if L % k != 0:
            # Nur sinnvoll, wenn die Länge exakt durch k teilbar ist
            continue

        block = s[:k]
        m = L // k

        if block * m == s:
            return True

    return False


if __name__ == "__main__":
    # print(calculate_invalid_ids(sample_file))
    # print(calculate_invalid_ids(input_file))
    print(calculate_ivalid_ids2(sample_file))
    print(calculate_ivalid_ids2(input_file))
