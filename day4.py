def part_one():
    with open("input.txt") as file:
        answer = 0
        for line in file:
            winning_numbers = set([int(number) for number in line.split(":")[1].split("|")[0].split()])
            scratched_numbers = set([int(number) for number in line.split(":")[1].split("|")[1].split()])
            set_difference = 25 - len(scratched_numbers - winning_numbers)
            if set_difference:
                answer += 2 ** (set_difference-1)
        print(answer)


def part_two():
    with open("input.txt") as file:
        multiplier = [1 for _ in range(194)]
        answer = 0
        for count, line in enumerate(file):
            winning_numbers = set([int(number) for number in line.split(":")[1].split("|")[0].split()])
            scratched_numbers = set([int(number) for number in line.split(":")[1].split("|")[1].split()])
            set_difference = 25 - len(scratched_numbers - winning_numbers)

            temp = multiplier[count]
            for i in range(count + 1, count + 1 + set_difference):
                multiplier[i] += temp
            answer += temp
        print(answer)


if __name__ == '__main__':
    part_one()
    part_two()
