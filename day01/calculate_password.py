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

def calculate_password2(data_file) -> int:
    result = 0
    data = [[line[0], int(line[1:])] for line in open(data_file).read().strip().splitlines()]
    MAX = 100

    start_position = 50
    current_position = start_position
    movement = {'L': int(-1), 'R': int(1)}
    rotations = 0

    for entry in data:
        clicks = (movement[entry[0]] * entry[1])
        rotations = 0
        last_position = current_position
        current_position = current_position + clicks
    
        if (clicks > 0):
            rotations += current_position // MAX
        elif (clicks < 0 and current_position > -99):
            rotations += 1
        else:
            rotations += abs(current_position) // MAX
        
        current_position = current_position % MAX

        print('{:2} >> {}{:2} >> {:2} >> {:2}'.format(last_position, entry[0], entry[1], current_position, rotations))

        result += rotations

    return result

if __name__ == "__main__":
    # print(calculate_password(sample_file))
    # print(calculate_password(input_file))
    print(calculate_password2(sample_file))
    # print(calculate_password2(input_file))
