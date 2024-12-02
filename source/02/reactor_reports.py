def is_line_safe(line):
    diffs = []
    index = 0

    # print(line)
    while index < (len(line) - 1):
        current = int(line[index])
        next = int(line[index+1])
        # print(next - current)
        diffs.append(next - current)
        index += 1

    if 0 in diffs:
        return False
    if min(diffs) < 0 < max(diffs):
        return False
    if min(diffs) < -3:
        return False
    if max(diffs) > 3:
        return False
    return True


def is_line_safe_part_2(line):
    """Part 2 test input expected: 4"""
    if is_line_safe(line):
        return True
    print(line)
    safe_after_removing_1 = False
    for i in range(len(line)):
        copy_line = line.copy()
        copy_line.pop(i)
        if is_line_safe(copy_line):
            safe_after_removing_1 = True

    return safe_after_removing_1


def part_1():
    """Part 1 test input expected: 2"""
    with open("input1.txt") as f:
        input_file = f.readlines()
        safe_part_1 = 0
        safe_part_2 = 0
        for line in input_file:
            is_safe = is_line_safe(line.strip().split())
            if is_safe:
                safe_part_1 += 1
            is_safe_2 = is_line_safe_part_2(line.strip().split())
            if is_safe_2:
                print(line)
                safe_part_2 += 1

        print(safe_part_1)
        print(safe_part_2)


if __name__ == "__main__":
    part_1()
