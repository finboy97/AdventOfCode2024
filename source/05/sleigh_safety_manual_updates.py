def creates_rules_map(input_list):
    rules = dict()
    rule_keys = set()
    for element in input_list:
        k, v = element.split("|")
        if k in rule_keys:
            rules[k].append(v)
        else:
            rule_keys.add(k)
            rules[k] = [v]
    return rules


def is_update_valid(rules_map, update):

    for index in range(len(update)):
        page = update[index]
        page_rules = rules_map.get(page)
        previous_pages = update[:index]
        if page_rules:
            # print(f"Page: {page}")
            # print(f"Page rules:{page_rules}")
            # print(f"Previous pages:{previous_pages}")
            for item in page_rules:
                if item in previous_pages:
                    # print(f"{page} is invalid. Preceding pages are {previous_pages}")
                    return False
    return True


def part_1():
    """143"""
    with open("input1.txt") as f:
        all_lines = f.readlines()
        rules = all_lines[0:all_lines.index("\n")]
        updates = all_lines[all_lines.index("\n")+1:]
        rules = [rule.strip() for rule in rules]
        updates = [update.strip() for update in updates]
        rules_map = creates_rules_map(rules)
        middle_numbers = []
        fixed_middle_numbers = []
        for update in updates:
            update = update.split(",")
            if is_update_valid(rules_map, update):
                middle_numbers.append(int(update[(int(len(update)/2))]))
            else:
                fixed = part_2(update, rules_map)
                fixed_middle_numbers.append(int(fixed[(int(len(fixed)/2))]))

        total_middle_numbers = 0
        for num in middle_numbers:
            total_middle_numbers += num
        total_fixed_middle_numbers = 0
        for num in fixed_middle_numbers:
            total_fixed_middle_numbers += num
        print(total_middle_numbers)
        print(total_fixed_middle_numbers)


def find_invalid_index(line, rules_map):
    index = 1
    new_slice = line[:index]
    slice_valid = is_update_valid(rules_map, new_slice)
    if not slice_valid:
        return index
    while slice_valid:
        index += 1
        new_slice = line[:index]
        slice_valid = is_update_valid(rules_map, new_slice)
        if not slice_valid:
            return index -1


def part_2(update, rules_map):
    """123"""
    fixed = []
    for x in update:
        fixed.append(x)
    fix_found = False
    while not fix_found:
        print(fixed)
        is_fixed = is_update_valid(rules_map, fixed)
        if is_fixed:
            return fixed
        invalid_index = find_invalid_index(fixed, rules_map)
        swap = fixed[invalid_index]
        fixed[invalid_index] = fixed[invalid_index-1]
        fixed[invalid_index-1] = swap
    return update


if __name__ == "__main__":
    part_1()
