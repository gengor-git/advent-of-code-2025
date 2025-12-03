from typing import List

input_file = "day03/input.txt"
sample_file = "day03/sample.txt"


def calculate_joltage_pt1(data_file) -> int:
    result = 0
    data = [[int(s) for s in line] for line in open(data_file).read().strip().splitlines()]
    for entry in data:
        result += get_joltage_large(entry, 2)
    return result

def calculate_joltage_pt2(data_file) -> int:
    result = 0
    data = [[int(s) for s in line] for line in open(data_file).read().strip().splitlines()]
    for entry in data:
        result += get_joltage_large(entry, 12)
    return result

def find_max_index(lst, start=0):
    '''Finds the index of the max value in a list of integers.
    @lst: the list of integer values.
    @start: the first index to look for (in case we want to skip parts at the beginning).
    '''
    max_index, max_value = start, lst[start]
    for index, value in enumerate(lst):
        if index < start:
            continue
        if value > max_value:
            max_value, max_index = value, index
    return max_index


def get_joltage_large(bank: List[int], pack_size=12) -> int:
    '''Returns the joltage for a battery bank with dynamic size.
    @bank: the battery bank to select the best batteries from.
    @pack_size: the size of the result battery amount to pick from the pack.
    '''
    remaining_size = pack_size
    length = len(bank)
    joltage = 0
    idx_start = 0

    print('Size: {}: {}'.format(pack_size, bank))
    # k = die jeweiligen Stellen der Zielzahl (=Batterien)
    for k in range(pack_size):
        print('k: {:2}'.format(k))

        idx_stop = length - (pack_size - k) +1
        idx_k_max = find_max_index(bank[:idx_stop], idx_start)
        idx_start = idx_k_max + 1 # next numbers must be after this index

        # result.append(bank[idx_k_max])
        joltage += bank[idx_k_max] * 10 ** (pack_size-k-1)

        print('MAX at index {}, value {}'.format(idx_k_max, bank[idx_k_max]))
        print('Remaing {}'.format(bank[idx_start:]))

    print('Joltage: {}'.format(joltage))
    print('')

    return joltage

if __name__ == "__main__":
    # print('Result: {}'.format(calculate_joltage_pt1(sample_file)))
    # print('Result: {}'.format(calculate_joltage_pt1(input_file)))
    # print('Result: {}'.format(calculate_joltage_pt2(sample_file)))
    print('Result: {}'.format(calculate_joltage_pt2(input_file)))
