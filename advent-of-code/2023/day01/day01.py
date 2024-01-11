word_to_num = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def find_first_num(line, reverse_order=False) -> int or None:
    line = reversed(line) if reverse_order else line
    search_string = ''
    for char in line:
        if char.isnumeric():  # Part 1
            return int(char)
        elif char.isalpha():  # Part 2
            search_string = char + search_string if reverse_order else search_string + char
            found_key = next(
                (key for key in word_to_num if key in search_string), None)
            if found_key:
                return word_to_num[found_key]
        else:
            search_string = ''
    return None


with open("actual_input.txt") as file:
    lines = file.read().splitlines()

combined_nums = []
for line in lines:
    first_num = find_first_num(line=line)
    second_num = find_first_num(line=line, reverse_order=True)
    combined_num = int(f'{first_num}{second_num}')
    # print(combined_num)
    combined_nums.append(combined_num)

answer = sum(combined_nums)
# print()
print(answer)
