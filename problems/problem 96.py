print("Starting")

file = open("sudoku.txt")
import math

def solveSudoku(grid):
    footNoteGrid = []
    for row in range(0,9):
        line = []
        for col in range(0,9):
            if grid[row][col] != 0:
                line.append(set())
                continue
            notes = set()
            for i in range(1,10):
                good = True
                if i in grid[row]:
                    good = False
                if good:
                    for j in range(0,9):
                        if grid[j][col] == i:
                            good = False
                if good:
                    for row2 in range(row-(row%3),row-(row%3)+3):
                        for col2 in range(col-(col%3),col-(col%3)+3):
                            if grid[row2][col2] == i:
                                good = False
                if good:
                    notes.add(i)
            line.append(notes)
        footNoteGrid.append(line)
    while not checkGrid(grid):
        found = True
        while found:
            found = False
            for row in range(0,9):
                for col in range(0,9):
                    if len(footNoteGrid[row][col]) == 1:
                        found = True
                        value = footNoteGrid[row][col].pop()
                        grid[row][col] = value
                        footNoteGrid = removeNotes(footNoteGrid,value,row,col)
            for i in range(1,10):
                for row in range(0,9):
                    counter = 0
                    onlyRowCol = []
                    for col in range(0,9):
                        if i in footNoteGrid[row][col]:
                            counter+=1
                            onlyRowCol = [row,col]
                        if counter == 2:
                            break
                    if counter == 1:
                        found = True
                        grid[onlyRowCol[0]][onlyRowCol[1]] = i
                        footNoteGrid[onlyRowCol[0]][onlyRowCol[1]] = set()
                        footNoteGrid = removeNotes(footNoteGrid,i,onlyRowCol[0],onlyRowCol[1])            
                for col in range(0,9):
                    counter = 0
                    onlyRowCol = []
                    for row in range(0,9):
                        if i in footNoteGrid[row][col]:
                            counter+=1
                            onlyRowCol = [row,col]
                        if counter == 2:
                            break
                    if counter == 1:
                        found = True
                        grid[onlyRowCol[0]][onlyRowCol[1]] = i
                        footNoteGrid[onlyRowCol[0]][onlyRowCol[1]] = set()
                        footNoteGrid = removeNotes(footNoteGrid,i,onlyRowCol[0],onlyRowCol[1])   
                for r in range(0,3):
                    for c in range(0,3):
                        counter = 0
                        onlyRowCol = []
                        for row in range(3*r,3*(r+1)):
                            for col in range(3*c,3*(c+1)):
                                if i in footNoteGrid[row][col]:
                                    counter += 1
                                    onlyRowCol = [row,col]
                                if counter == 2:
                                    break
                        if counter == 1:
                            found = True
                            grid[onlyRowCol[0]][onlyRowCol[1]] = i
                            footNoteGrid[onlyRowCol[0]][onlyRowCol[1]] = set()
                            footNoteGrid = removeNotes(footNoteGrid,i,onlyRowCol[0],onlyRowCol[1])
        footNoteGrid = updateNotes(footNoteGrid)
    return grid
                
def checkGrid(grid):
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col] == 0:
                return False
    return True

def updateNotes(hintGrid):
    footNoteGrid = hintGrid
    ##look for pointing doubles
    for i in range(1,10):
        for col in range(0,9):
            counter = 0
            bestBlock = -1
            for block in range(0,3):
                for row in range(block*3,block*3+3):
                    if i in footNoteGrid[row][col]:
                        counter += 1
                        bestBlock = block
                        break
            if counter == 1:
                for row2 in range(0,9):
                    if row2-(row2%3) == bestBlock*3:
                        continue
                    if i in footNoteGrid[row2][col]:
                        footNoteGrid[row2][col].remove(i)
                for row in range(bestBlock*3,bestBlock*3+3):
                    for col2 in range(col-(col%3),col-(col%3)+3):
                        if col2 == col:
                            continue
                        if i in footNoteGrid[row][col2]:
                            footNoteGrid[row][col2].remove(i)
        for row in range(0,9):
            counter = 0
            bestBlock = -1
            for block in range(0,3):
                for col in range(block*3,block*3+3):
                    if i in footNoteGrid[row][col]:
                        counter += 1
                        bestBlock = block
                        break
            if counter == 1:
                for col2 in range(0,9):
                    if col2-(col2%3) == bestBlock*3:
                        continue
                    if i in footNoteGrid[row][col2]:
                        footNoteGrid[row][col2].remove(i)
                for col in range(bestBlock*3,bestBlock*3+3):
                    for row2 in range(row-(row%3),row-(row%3)+3):
                        if row2 == row:
                            continue
                        if i in footNoteGrid[row2][col]:
                            footNoteGrid[row2][col].remove(i)
        for rowBlock in range(0,3):
            for colBlock in range(0,3):
                colIndices = []
                rowIndices = []
                for row in range(rowBlock*3,rowBlock*3+3):
                    for col in range(colBlock*3,colBlock*3+3):
                        if i in footNoteGrid[row][col]:
                            colIndices.append((col-colBlock*3)+3*(row-rowBlock*3)) ## for 4 4 for example, (col-colBlock*3)+3*(row-rowBlock*3)=(4-1*3)+3*(4-1*3)=1+3 = 4
                            rowIndices.append((row-rowBlock*3)+3*(col-colBlock*3))
                if len(colIndices) > 3:
                    continue
                modColIndices = set(x for x in map(lambda k: k%3,colIndices))
                modRowIndices = set(x for x in map(lambda k: k%3,rowIndices))
                if len(modColIndices) == 1:
                    column = modColIndices.pop()
                    for row2 in range(0,9):
                        if row2-(row2%3) == rowBlock*3:
                            continue
                        if i in footNoteGrid[row2][colBlock*3+column]:
                            footNoteGrid[row2][colBlock*3+column].remove(i)
                if len(modRowIndices) == 1:
                    theRow = modRowIndices.pop()
                    for col2 in range(0,9):
                        if col2-(col2%3) == colBlock*3:
                            continue
                        if i in footNoteGrid[rowBlock*3+theRow][col2]:
                            footNoteGrid[rowBlock*3+theRow][col2].remove(i)
    ##look for naked pairs
    for row in range(0,9):
        for col in range(0,9):
            if len(footNoteGrid[row][col]) == 2 and footNoteGrid[row].count(footNoteGrid[row][col]) == 2:
                values = list(footNoteGrid[row][col])
                for col2 in range(0,9):
                    if footNoteGrid[row][col2] != footNoteGrid[row][col]:
                        if values[0] in footNoteGrid[row][col2]:
                            footNoteGrid[row][col2].remove(values[0])
                        if values[1] in footNoteGrid[row][col2]:
                            footNoteGrid[row][col2].remove(values[1])
    for col in range(0,9):
        for row in range(0,9):
            if len(footNoteGrid[row][col]) == 2:
                counter = 0
                for countingRows in range(0,9):
                    if footNoteGrid[countingRows][col]== footNoteGrid[row][col]:
                        counter += 1
                if counter == 2:
                    values = list(footNoteGrid[row][col])
                    for row2 in range(0,9):
                        if footNoteGrid[row2][col] != footNoteGrid[row][col]:
                            if values[0] in footNoteGrid[row2][col]:
                                footNoteGrid[row2][col].remove(values[0])
                            if values[1] in footNoteGrid[row2][col]:
                                footNoteGrid[row2][col].remove(values[1])
    ##look for hidden pairs
    for col in range(0,9):
        for i in range(1,10):
            for j in range(1,10):
                if i == j:
                    continue
                goodRowsI = []
                goodRowsJ = []
                for row in range(0,9):
                    if i in footNoteGrid[row][col]:
                        goodRowsI.append(row)
                    if j in footNoteGrid[row][col]:
                        goodRowsJ.append(row)
                if len(goodRowsI) == 2 and len(goodRowsJ) == 2 and len(set(goodRowsI+goodRowsJ)) == 2:
                    for r in goodRowsI:
                        footNoteGrid[r][col] = set([i,j])
    for row in range(0,9):
        for i in range(1,10):
            for j in range(1,10):
                if i == j:
                    continue
                goodColsI = []
                goodColsJ = []
                for col in range(0,9):
                    if i in footNoteGrid[row][col]:
                        goodColsI.append(col)
                    if j in footNoteGrid[row][col]:
                        goodColsJ.append(col)
                if len(goodColsI) == 2 and len(goodColsJ) == 2 and len(set(goodColsI+goodColsJ)) == 2:
                    for c in goodColsI:
                        footNoteGrid[row][c] = set([i,j])
    ## look for xwing
    for i in range(1,10):
        columnsForEachRow = []
        for row in range(0,9):
            goodCols1 = []
            for col in range(0,9):
                if i in footNoteGrid[row][col]:
                    goodCols1.append(col)
            columnsForEachRow.append(goodCols1)
        for goodCols in columnsForEachRow:
            if len(goodCols) == 2 and columnsForEachRow.count(goodCols) == 2:
                for row2 in range(0,9):
                    if columnsForEachRow[row2] != goodCols:
                        if i in footNoteGrid[row2][goodCols[0]]:
                            footNoteGrid[row2][goodCols[0]].remove(i)
                        if i in footNoteGrid[row2][goodCols[1]]:
                            footNoteGrid[row2][goodCols[1]].remove(i)
        rowsForEachColumn = []
        for col in range(0,9):
            goodRows1 = []
            for row in range(0,9):
                if i in footNoteGrid[row][col]:
                    goodRows1.append(row)
            rowsForEachColumn.append(goodRows1)
        for goodRows in rowsForEachColumn:
            if len(goodRows) == 2 and rowsForEachColumn.count(goodRows) == 2:
                for col2 in range(0,9):
                    if rowsForEachColumn[col2] != goodRows:
                        if i in footNoteGrid[goodRows[0]][col2]:
                            footNoteGrid[goodRows[0]][col2].remove(i)
                        if i in footNoteGrid[goodRows[1]][col2]:
                            footNoteGrid[goodRows[1]][col2].remove(i)
    return footNoteGrid
                    
def removeNotes(footNoteGrid,value,row,col):
    for row2 in range(0,9):
        if value in footNoteGrid[row2][col]:
            footNoteGrid[row2][col].remove(value)
    for col2 in range(0,9):   
        if value in footNoteGrid[row][col2]:
            footNoteGrid[row][col2].remove(value)
    for row3 in range(row-(row%3),row-(row%3)+3):
        for col3 in range(col-(col%3),col-(col%3)+3):
            if value in footNoteGrid[row3][col3]:
                footNoteGrid[row3][col3].remove(value)
    return footNoteGrid

def formatGrid(grid):
    newGrid = []
    for line in grid:
        newLine = []
        for x in line:
            newLine.append(int(x))
        newGrid.append(newLine)
    return newGrid
    
lineCounter = 0
answer = 0
gridCounter = 0
for line in file:
    if lineCounter == 0:
        gridCounter += 1
        print(gridCounter)
        currentGrid = []
        lineCounter+=1
        continue
    if lineCounter < 10:
        line = line.strip()
        currentGrid.append(line)
        lineCounter+=1
        if lineCounter == 10:
            currentGrid = formatGrid(currentGrid)
            currentGrid = solveSudoku(currentGrid)
            value = ""
            for i in currentGrid[0][:3]:
                value += str(i)
            answer += int(value)
            lineCounter = 0

print(answer)
input("done")
