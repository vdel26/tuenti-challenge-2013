import fileinput
from string import *


def main(numbers):
    numbers = [int(i) for i in numbers]
    print sum(numbers)


if __name__ == '__main__':
    for line in fileinput.input():
        line1 = line.rstrip('\n')
        line2 = line1.split()
        main(line2)
