input_file = "day05/input.txt"
sample_file = "day05/sample.txt"


def calculate_freshness_pt1(data_file) -> int:
    result = 0
    data = open(data_file).read().strip().split("\n\n")

    ranges = [tuple(map(int, line.split("-"))) for line in data[0].splitlines()]
    ingredients = [int(s) for s in data[1].splitlines()]

    for ingredient in ingredients:
        result += 1 if is_in_ranges(ingredient, ranges) else 0
    return result

def is_in_ranges(n: int, ranges: list[tuple[int, int]]) -> bool:
    return any(a <= n <= b for a, b in ranges)

def calculate_freshness_pt2(data_file) -> int:
    result = 0
    data = open(data_file).read().strip().split("\n\n")

    ranges = [tuple(map(int, line.split("-"))) for line in data[0].splitlines()]

    merged_ranges = merge_ranges(ranges)

    return sum(end - start + 1 for start, end in merged_ranges)
    
def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not ranges:
        return []

    # Nach Start sortieren
    ranges = sorted(ranges, key=lambda r: r[0])
    merged: list[tuple[int, int]] = []
    cur_start, cur_end = ranges[0] # first tuple

    for start, end in ranges[1:]:
        if start <= cur_end + 1:  # überlappt oder berührt
            # zusammenführen: Endpunkt anpassen
            cur_end = max(cur_end, end)
        else:
            # aktuelle Range abschließen
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end

    # letzte Range nicht vergessen
    merged.append((cur_start, cur_end))
    return merged
    



    return result

if __name__ == "__main__":
    # print(calculate_freshness_pt1(sample_file))
    # print(calculate_freshness_pt1(input_file))
    print(calculate_freshness_pt2(sample_file))
    print(calculate_freshness_pt2(input_file))
