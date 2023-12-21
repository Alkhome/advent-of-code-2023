import matplotlib.pyplot as plt
import numpy as np


def part_one():
    with open("input.txt") as file:

        answer = []

        race_time = list(map(int, file.readline().split(":")[1].split()))
        record_distance = list(map(int, file.readline().split(":")[1].split()))

        for race in range(len(record_distance)):
            different_ways_to_beat = 0
            plt.axhline(y=record_distance[race], linestyle='-')
            for release_time in range(race_time[race] + 1):

                race_time_left = race_time[race] - release_time

                x = race_time_left
                y = release_time * x  # a = release_time
                plt.plot(x, y, 'r*')
                if y > record_distance[race]:
                    different_ways_to_beat += 1

            answer.append(different_ways_to_beat)
            plt.plot()
            plt.show()

        print(np.prod(answer))


def part_two():
    with open("input.txt") as file:
        answer = 0

        race_time = int("".join(file.readline().split(":")[1].split()))
        record_distance = int("".join(file.readline().split(":")[1].split()))

        for release_time in range(race_time + 1):
            race_time_left = race_time - release_time

            x = race_time_left
            y = release_time * x  # a = release_time
            if y > record_distance:
                answer += 1
    print(answer)


if __name__ == '__main__':
    # part_one()
    part_two()
