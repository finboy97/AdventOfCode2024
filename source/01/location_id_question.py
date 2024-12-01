from collections import Counter
def part_1():
    """
    Answer with test input is 11
    :return:
    """
    with open("input_part_1.txt") as f:
        location_lists = f.readlines()
        list_1 = []
        list_2 = []
        for line in location_lists:
            split_line = line.strip("\n").split(" ")
            list_1.append(int(split_line[0]))
            list_2.append(int(split_line[-1]))
        # print(sorted(list_1))
        # print(sorted(list_2))
        difference = 0
        for x, y in zip(sorted(list_1), sorted(list_2)):
            # print(max(x,y) - min(x,y))
            difference += (max(x,y) - min(x,y))
            # print(difference)
        print(difference)
        part_2(list_1, list_2)


def part_2(list_1, list_2):
    """
    Answer with test input is 31
    """
    counted_2 = Counter(list_2)
    similarity = 0
    for item in list_1:
        similarity += (item * counted_2[item])
    print(similarity)


if __name__ == "__main__":
    part_1()
