import re
def part_one():

    array_of_strings = []

    with open("day1.txt") as file:
        for line in file:
            temp_array = []
            for character in line:
                if character.isdigit():
                    temp_array.append(character)
            array_of_strings.append(temp_array[0] + temp_array[-1])
    print(array_of_strings)
    array_of_numbers = [int(i) for i in array_of_strings]
    print(sum(array_of_numbers))

def part_two():

    array_of_strings = []

    with open("day1.txt") as file:
        for line in file:
            line = line.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r"). \
                        replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t"). \
                        replace("nine", "n9e")
            temp_array = []
            for character in line:
                if character.isdigit():
                    temp_array.append(character)
            array_of_strings.append(temp_array[0] + temp_array[-1])
    print(array_of_strings)
    array_of_numbers = [int(i) for i in array_of_strings]
    print(sum(array_of_numbers))

if __name__ == '__main__':
    part_one()
    part_two()
