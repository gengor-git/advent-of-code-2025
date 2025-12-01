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

    start_position = 50
    current_position = start_position
    movement = {'L': int(-1), 'R': int(1)}
    rotations = 0    

    for entry in data:
        clicks = (movement[entry[0]] * entry[1])
        rotations = 0

        # calculate the relative position on the dial
        last_position = current_position
        current_position = current_position + clicks

        if (current_position == 0):
            # we are exactly at 0
            rotations += 1
        while (current_position < 0):
            # left way is more difficult
            current_position = current_position + 100
            if (last_position != 0):
                # simple version, we know we passed 0 at least once
                rotations += 1
            elif (last_position == 0 and clicks < -99):
                rotations += 1
        while (current_position > 99):
            current_position = current_position - 100
            rotations += 1

        result += rotations
        print("{:3} -> {:3} via {}{:3} with {:3} rotations".format(last_position, current_position, entry[0], entry[1], rotations))
                
    return result

if __name__ == "__main__":
    # print(calculate_password(sample_file))
    # print(calculate_password(input_file))
    # print(calculate_password2(sample_file))
    print(calculate_password2(input_file))
