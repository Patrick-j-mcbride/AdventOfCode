
def part1(input_string):
    nums = []
    for i in range(len(input_string)):
        if input_string[i].isdigit():
            nums.append(input_string[i])
    return int(str(nums[0]) + str(nums[-1]))


def part2(input_string):
    nums = []
    number_words = {
        "zero": "0", "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6", "seven": "7",
        "eight": "8", "nine": "9"
    }
    for i in range(len(input_string)):
        if input_string[i].isdigit():
            nums.append(input_string[i])
        else:
            for word, digit in number_words.items():
                if input_string[i:i+len(word)] == word:
                    nums.append(digit)
    return int(str(nums[0]) + str(nums[-1]))


with open('data.txt') as f:
    pt1, pt2 = [], []
    for line in f.readlines():
        pt1.append(part1(line))
        pt2.append(part2(line))
    print("Part 1: ", sum(pt1))
    print("Part 2: ", sum(pt2))
