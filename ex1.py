import fileinput
from string import *
import sys


class Investment(object):
    def __init__(self, money, seq):
        self.do = "hold"
        self.money = money
        self.bitcoins = 0
        self.seq = seq

    def main(self):
        numbers = self.seq
        numbers = [int(i) for i in numbers]
        for pos, i in enumerate(numbers):
            if pos == 0:
                local = numbers[pos:2]
                if local.index(max(local)) == 0:
                    pass
                else:
                    self.do = "buy"
                    self.buy(i)
            elif pos == (len(numbers)-1):
                local = numbers[-2:pos+1]
                if (local.index(max(local)) == len(local)-1) and self.do != "sell":
                    self.do = "sell"
                    self.sell(i)
                else:
                    self.do = "hold"
            else:
                local = numbers[pos-1:pos] + numbers[pos:pos+2]
                if (local.index(max(local)) == 1) and (local.count(max(local)) <= 1) and self.do != "sell":
                    self.do = "sell"
                    self.sell(i)
                elif (local.index(min(local)) == 1) and self.do != "buy":
                    self.do = "buy"
                    self.buy(i)
                else:
                    self.do = "hold"

    def sell(self, pos):
        self.money += (self.bitcoins*pos)
        self.bitcoins = 0

    def buy(self, pos):
        self.bitcoins += (self.money/pos)
        self.money = 0

    def result(self):
        print self.money

if __name__ == '__main__':
    for line in fileinput.input():
        linenum = int(fileinput.lineno())
        line_clean = line.rstrip('\n')
        if linenum == 1:
            numcases = int(line_clean)
        elif (linenum % 2 == 0) and linenum != 1:
            money = int(line_clean)
        else:
            line2 = line_clean.split()
            seq = [int(i) for i in line2]
            inv = Investment(money, seq)
            inv.main()
            inv.result()
