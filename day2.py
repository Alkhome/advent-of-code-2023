import re


def part_one():
    all_reds = 12
    all_greens = 13
    all_blues = 14

    answer = 0
    with open("day2.txt") as file:
        for line in file:
            line = line.split(":")
            draws = line[1].split(";")
            possible = 1
            for draw in draws:
                red = re.findall("\d+ red", draw)
                green = re.findall("\d+ green", draw)
                blue = re.findall("\d+ blue", draw)

                if red and int(red[0].split(" ")[0]) > all_reds:
                    possible = 0

                if green and int(green[0].split(" ")[0]) > all_greens:
                    possible = 0

                if blue and int(blue[0].split(" ")[0]) > all_blues:
                    possible = 0

            if possible:
                answer += int(line[0].split(" ")[1])
        print(answer)


def part_two():
    answer = 0
    with open("day2.txt") as file:
        for line in file:
            line = line.split(":")
            draws = line[1].split(";")
            max_red = 0
            max_green = 0
            max_blue = 0
            for draw in draws:
                red = re.findall("\d+ red", draw)
                green = re.findall("\d+ green", draw)
                blue = re.findall("\d+ blue", draw)

                if red and int(red[0].split(" ")[0]) > max_red:
                    max_red = int(red[0].split(" ")[0])

                if green and int(green[0].split(" ")[0]) > max_green:
                    max_green = int(green[0].split(" ")[0])

                if blue and int(blue[0].split(" ")[0]) > max_blue:
                    max_blue = int(blue[0].split(" ")[0])

            answer += max_red * max_green * max_blue
        print(answer)


if __name__ == '__main__':
    part_one()
    part_two()
