import time
from copy import deepcopy

grid = [
    [None, None, 3, 9, None, 5, None, 8, 2],
    [1, None, None, None, None, None, 7, 9, 5],
    [5, 9, None, None, 8, None, None, None, None],
    [None, 3, 7, None, None, 1, None, None, None],
    [None, None, 9, 2, 3, 8, 5, None, None],
    [None, None, None, 7, None, None, 1, 2, None],
    [None, None, None, None, 6, None, None, 1, 7],
    [4, 6, 1, None, None, None, None, None, 8],
    [9, 7, None, 1, None, 4, 2, None, None],
]


def displayGrid(grid):
    for x in range(0, 9):
        print(list(map(lambda el: 0 if not el else el, grid[x])))
    print('\n')


def getBoxStart(x, y):
    possibleValues = [0, 3, 6]
    return {'x': possibleValues[x // 3], 'y': possibleValues[y // 3]}


def getBoxValues(grid, box):
    values = list()
    for x in range(box['x'], box['x'] + 3):
        for y in range(box['y'], box['y'] + 3):
            if grid[x][y]:
                values.append(grid[x][y])
    return values


def getRowValues(grid, x):
    values = list()
    for y in range(0, 9):
        if grid[x][y]:
            values.append(grid[x][y])
    return values


def getColValues(grid, y):
    values = list()
    for x in range(0, 9):
        if grid[x][y]:
            values.append(grid[x][y])
    return values


def getPossibleValues(grid, mem, x, y):
    if grid[x][y]:
        return [grid[x][y]]

    box = getBoxStart(x, y)
    boxKey = f"{box['x']}-{box['y']}"
    boxValues = []
    rowValues = []
    columnValues = []

    if boxKey in mem['box']:
        boxValues = mem['box'][boxKey]
    else:
        boxValues = getBoxValues(grid, box)
        mem['box'][boxKey] = boxValues

    if x in mem['row']:
        rowValues = mem['row'][x]
    else:
        rowValues = getRowValues(grid, x)
        mem['row'][x] = rowValues

    if y in mem['column']:
        columnValues = mem['column'][y]
    else:
        columnValues = getColValues(grid, y)
        mem['column'][y] = columnValues

    values = list()
    values.extend(boxValues)
    values.extend(rowValues)
    values.extend(columnValues)
    values = set(values)
    return [num for num in range(1, 10) if num not in values]


# Check sum of each box, row, and column to ensure it's equals to 45, hence valid
def isValidSolution(mem):
    validSum = 45  # 1 + 2 ... + 9 = 45
    for key in mem['box'].keys():
        sumBox = sum(mem['box'][key])
        if sumBox != validSum:
            return False
    for key in mem['row'].keys():
        sumRow = sum(mem['row'][key])
        if sumRow != validSum:
            return False
    for key in mem['column'].keys():
        sumCol = sum(mem['column'][key])
        if sumCol != validSum:
            return False
    return True


def solve(grid):
    # All possible values for a given cell
    possibleValues = [[None for j in range(0, 9)] for i in range(0, 9)]
    # Cache to enable quick access of adjacent values
    mem = {
        'box': dict(),
        'row': dict(),
        'column': dict(),
    }
    remaining = 81
    while remaining > 0:
        tempRemaining = deepcopy(remaining)
        remaining = 81
        for x in range(0, 9):
            for y in range(0, 9):
                box = getBoxStart(x, y)
                boxKey = f"{box['x']}-{box['y']}"
                possibleValues[x][y] = getPossibleValues(grid, mem, x, y)
                if possibleValues[x][y] and len(possibleValues[x][y]) == 1 and not grid[x][y]:
                    val = possibleValues[x][y][0]
                    mem['box'][boxKey].append(val)
                    mem['row'][x].append(val)
                    mem['column'][y].append(val)
                    possibleValues[x][y] = getPossibleValues(grid, mem, x, y)
                    grid[x][y] = val
                if grid[x][y]:
                    remaining -= 1
            if remaining == 0:
                break

        # If no number had been added, it means we're not able to solve the puzzle
        if remaining == tempRemaining:
            return False

    isValid = isValidSolution(mem)
    if not isValid:
        return False

    return True


# print('Before \n')

# displayGrid(grid)

# timestamp = time.time()
# solved = solve(grid)
# duration = (time.time() - timestamp) * 1000
# print('Result: ', 'Success' if solved else 'Failure')
# print(f'Duration: {duration} ms')
# displayGrid(grid)
# print('\n')
