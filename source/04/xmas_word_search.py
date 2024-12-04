def xmas_in_row(row):
    total_xmas = 0
    for x in range(len(row)-3):
        if row[x:x+4] == "XMAS":
            total_xmas += 1
    return total_xmas


def reverse_xmas_in_row(row):
    reversed_row = row[::-1]
    return xmas_in_row(reversed_row)


def part_1():
    """18"""
    with open("input1.txt") as f:
        rows = []
        for line in f.readlines():
            rows.append(line.strip())
        row_total = 0
        for row in rows:
            row_total += xmas_in_row(row)
            row_total += reverse_xmas_in_row(row)

        col_total = 0
        for col_index in range(len(rows[0])):
            col_str = ""
            for row_index in range(len(rows)):
                col_str = col_str + rows[row_index][col_index]
            col_total += xmas_in_row(col_str)
            col_total += reverse_xmas_in_row(col_str)

        downwards_diag_total = 0
        for row_index in range(len(rows)):

            if (row_index +3) > (len(rows)-1):
                continue
            for column_index in range(len(rows[0])):

                if column_index + 3 > (len(rows[0])-1):
                    continue
                diag_str = (
                        rows[row_index][column_index]
                        + rows[row_index + 1][column_index + 1]
                        + rows[row_index + 2][column_index + 2]
                        + rows[row_index + 3][column_index + 3]
                )
                downwards_diag_total += xmas_in_row(diag_str)
                downwards_diag_total += reverse_xmas_in_row(diag_str)

        upwards_diag_total = 0
        for row_index in range(len(rows)):

            if (row_index - 3) < 0:
                continue
            for column_index in range(len(rows[0])):

                if column_index + 3 > (len(rows[0])-1):
                    continue
                diag_str = (
                        rows[row_index][column_index]
                        + rows[row_index - 1][column_index + 1]
                        + rows[row_index - 2][column_index + 2]
                        + rows[row_index - 3][column_index + 3]
                )
                upwards_diag_total += xmas_in_row(diag_str)
                upwards_diag_total += reverse_xmas_in_row(diag_str)
        print(row_total + col_total + downwards_diag_total + upwards_diag_total)
        part_2(rows)


def part_2(input_structure):
    """9"""
    rows = input_structure
    x_mas_total=0
    for row_index in range(1,len(rows)-1):
        for col_index in range(1, len(rows[0])-1):
            if rows[row_index][col_index] == "A":
                downward_diag = (
                    rows[row_index-1][col_index-1]
                    + "A"
                    + rows[row_index+1][col_index+1]
                )
                upwards_diag = (
                    rows[row_index-1][col_index+1]
                    + "A"
                    + rows[row_index+1][col_index-1]
                )
                if (
                        downward_diag == "MAS" or downward_diag == "SAM"
                ) and (
                    upwards_diag == "MAS" or upwards_diag == "SAM"
                ):
                    x_mas_total += 1
    print(x_mas_total)


if __name__ == "__main__":
    part_1()
