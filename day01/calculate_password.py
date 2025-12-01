input_file = "day01/input.txt"
sample_file = "day01/sample.txt"


def calculate_password(data_file) -> int:
    result = 0
    data = [[line[0], int(line[1:])] for line in open(data_file).read().strip().splitlines()]

    start_position = 50
    current_position = start_position
    movement = {'L': int(-1), 'R': int(1)}

    for entry in data:
        interim_position = current_position + (movement[entry[0]] * entry[1])

        # calculate the relative position on the dial
        current_position = interim_position
        while (current_position < 0):
            current_position = current_position + 100
        while (current_position > 99):
            current_position = current_position - 100

        if (current_position == 0):
            result += 1

    return result

def calculate_something2(data_file) -> int:
    result = 0
    data = [[int(s) for s in line.split()] for line in open(data_file).read().strip().splitlines()]
    for entry in data:
        pass
    return result

if __name__ == "__main__":
    # print(calculate_password(sample_file))
    print(calculate_password(input_file))
    # print(calculate_something2(sample_file))
    # print(calculate_something2(input_file))
