from typing import List

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
    movement = {'L': -1, 'R': 1}
    rotations = 0

    for entry in data:
        direction, steps = entry[0], entry[1]
        clicks = movement[direction] * steps

        last_position = current_position
        distance = abs(clicks)

        if clicks == 0:
            cycle = 0
        else:
            # Abstand bis zur ersten Nullüberquerung
            if clicks > 0:
                # clockwise
                dist_to_first_zero = MAX if current_position == 0 else (MAX - current_position)
            else:
                # counterclockwise
                dist_to_first_zero = MAX if current_position == 0 else current_position

            if distance < dist_to_first_zero:
                # we stay in this circle
                cycle = 0
            else:
                remaining = distance - dist_to_first_zero
                # only calculate the turns minus the first distance to zero (which we add manually)
                cycle = 1 + remaining // MAX

        new_pos = current_position + clicks
        current_position = new_pos % MAX

        rotations += cycle

        print('{:3} {} {:4} {:3} {:1}'.format(
            last_position, direction, clicks, current_position, cycle
        ))

    return rotations

if __name__ == "__main__":
    # print(calculate_password(sample_file))
    # print(calculate_password(input_file))
    # print(calculate_password2(sample_file))
    print(calculate_password2(input_file))
