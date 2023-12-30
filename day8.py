from math import lcm

LR_instruction = "LRRLRLRRLRRRLRLRLRRLRRRLRRRLRRLRRRLRLRLRLRLRLRLRRRLRRLRRRLLLLRRRLRLLLRRRLLRLLRRRLRRRLRLRRLRRRLRRRLLRRRLRLRRRLLRRRLRLLRRRLRRLLRLRLRLRRRLRLLRLRLRRRLRLLRLRLRRRLLRRRLRRLRRRLRLRRLRLRRLRLRRLRRRLLRRRLLLRRRLLRRLRRLRRLRLLRRLRRRLRRLRLRLRRLRRLLLRRLRLRRRLRRRLRRRLLLRLRRRLLRRRLRLLRRRR"

def part_one():
    with open("input.txt") as file:
        LUT = {}
        for line in file:
            LUT[line[:3]] = line[7:15].split(", ")
    curr_node = "AAA"
    steps_count = 0
    while curr_node != "ZZZ":
        for instruction in LR_instruction:
            if instruction == "L":
                next_node = LUT[curr_node][0]
            else:
                next_node = LUT[curr_node][1]
            curr_node = next_node
            steps_count += 1
            if curr_node == "ZZZ":
                break
    print(steps_count)


def part_two():
    with open("input.txt") as file:
        starting_nodes = []
        LUT = {}
        for line in file:
            cut_line = line[:3]
            LUT[cut_line] = line[7:15].split(", ")
            if cut_line.endswith("A"):
                starting_nodes.append(cut_line)
    steps_for_each_node = []
    for node in starting_nodes:
        curr_node = node
        steps_count = 0
        while curr_node.endswith("Z") is not True:
            for instruction in LR_instruction:
                if instruction == "L":
                    next_node = LUT[curr_node][0]
                else:
                    next_node = LUT[curr_node][1]
                curr_node = next_node
                steps_count += 1
                if curr_node.endswith("Z"):
                    break
        steps_for_each_node.append(steps_count)
    print(lcm(*steps_for_each_node))


if __name__ == '__main__':
    part_one()
    part_two()
