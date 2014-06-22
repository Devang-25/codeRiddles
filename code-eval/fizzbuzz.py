"""
Replace input list elements with:
- 'F' if divisble by A.
- 'B' if divisble by B.
- 'FB' if divisible by both A & B.
"""

import fileinput


class FizzBuzz(object):
    '''
    play the fizz-buzz game as per the given rules.
    '''

    def __init__(self, IPLIST):
        self.state_1 = IPLIST[0]
        assert 1 <= self.state_1 <= 20
        self.state_2 = IPLIST[1]
        assert 1 <= self.state_2 <= 20
        self.ip_range = IPLIST[2]
        assert 21 <= self.ip_range <= 100

    def results(self):
        """
        map conditions to input list.
        """
        temp = range(1, self.ip_range + 1)
        for i, element in enumerate(temp):
            if element % self.state_1 == 0 and element % self.state_2 == 0:
                temp[i] = 'FB'
            elif element % self.state_1 == 0:
                temp[i] = 'F'
            elif element % self.state_2 == 0:
                temp[i] = 'B'
            else:
                continue
        return ' '.join([str(x) for x in temp])

if __name__ == '__main__':
    ANS = []
    for line in fileinput.input():
        FB = FizzBuzz([int(k) for k in line.split()])
        ANS.append(FB.results())
    for j in ANS:
        print j
