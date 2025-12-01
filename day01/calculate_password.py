input_file = "day03/input.txt"
sample_file = "day03/sample.txt"


def calculate_password(data_file) -> int:
    result = 0
    data = [[int(s) for s in line.split()] for line in open(data_file).read().strip().splitlines()]
    for entry in data:
        pass
    return result

def calculate_something2(data_file) -> int:
    result = 0
    data = [[int(s) for s in line.split()] for line in open(data_file).read().strip().splitlines()]
    for entry in data:
        pass
    return result

if __name__ == "__main__":
    print(calculate_password(sample_file))
    print(calculate_password(input_file))
    print(calculate_something2(sample_file))
    print(calculate_something2(input_file))
