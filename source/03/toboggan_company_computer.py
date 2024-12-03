import re

regex_str = r"mul\([0-9]{1,6},[0-9]{1,6}\)"
multiply_regex = re.compile(regex_str)

def multiply_line(line):
    matches = multiply_regex.findall(line)
    total = 0
    for item in matches:
        x,y = item[4:].replace(")", "").split(",")
        # print(x,y)
        total += (int(x) * int(y))
        # print(int(x) * int(y))
    return total


def part_1():
    """
    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    Expected to equal 161
    """
    with open("input1.txt") as f:
        total = 0
        for line in f.readlines():
            total += multiply_line(line)
        print(total)


def part_2():
    """
    #xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
    expected to equal 48"""
    with open("input1.txt") as f:

        total_2 = 0
        input_str = f.read()
        instruction_split = input_str.split("do")
        total_2 += multiply_line(instruction_split[0])
        for item in instruction_split[1:]:
            if item[0:5] == "n't()":
                continue
            elif item[0:2] == "()":
                total_2 += multiply_line(item)
        print(total_2)


if __name__ == "__main__":
    part_1()
    part_2()
