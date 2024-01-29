
def toChar(n):
    return chr(ord('A') + n)

class Hanoi():
    def __init__(self, maxNumber) -> None:
        self.reset(maxNumber)

    def reset(self, maxNumber):
        if maxNumber > 29:
            print('[Warning] the tower may be tilted.')

        self.maxNumber = maxNumber
        self.towers = ([], [], [])
        for i in range(maxNumber, 0, -1):
            self.towers[0].append(i)

    def getBoardGraph(self, index):
        maxLength = self.maxNumber * 2 + 3

        air = ' '
        block = '-'
        if index == 0:
            return air * maxLength

        airs = air * (maxLength//2 - index + 1)
        strIndex = str(index)
        leftBoardBlocks = block * (index - 1 - len(strIndex) // 2)
        rightBoardBlocks = block * (index - 1 - (len(strIndex)-1) // 2)

        board = f'{airs}{leftBoardBlocks}{str(index)}{rightBoardBlocks}{airs}'

        return board
    
    def print(self):
        print(self.towers)
        maxHeight = self.maxNumber

        for i in range(maxHeight, -1, -1):
            for tower in self.towers:
                if i < len(tower):
                    print(f'{self.getBoardGraph(tower[i])}', end='')
                else:
                    print(f'{self.getBoardGraph(0)}', end='')
            print()


    def move(self, fromN, toN):
        if len(self.towers[fromN]) == 0 or \
            len(self.towers[toN]) != 0 and self.towers[fromN][-1] > self.towers[toN][-1]:
            raise RuntimeError('Invalid movement')
        
        index = self.towers[fromN].pop()
        self.towers[toN].append(index)

        print(f'move {index} from {toChar(fromN)} to {toChar(toN)}', end='\t')
        self.print()
        input()

hanoi = Hanoi(0)

def solve(number, fromN = 0, middle = 1, toN = 2):
    if number == 1:
        hanoi.move(fromN, toN)
    else:
        solve(number-1, fromN, toN, middle)
        solve(1, fromN, middle, toN)
        solve(number-1, middle, fromN, toN)
        

if __name__ == "__main__":
    number = int(input())
    hanoi.reset(number)
    solve(number, 0, 1, 2)